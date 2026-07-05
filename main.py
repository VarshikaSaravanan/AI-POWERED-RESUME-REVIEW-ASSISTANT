import os
import json
import time
import requests
from dotenv import load_dotenv

from tools import extract_pdf_text
from memory import load_memory, save_memory
from prompts import (
    MANAGER_PROMPT, ATS_AGENT_PROMPT, GRAMMAR_AGENT_PROMPT, 
    SKILLS_AGENT_PROMPT, IMPROVEMENT_AGENT_PROMPT, REPORT_AGENT_PROMPT
)

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openai/gpt-oss-20b:free" 
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

TOOLS = []

TOOL_FUNCTIONS = {}

def call_llm(messages, max_retries=5):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": messages,
        "tools": TOOLS
    }
    
    for attempt in range(max_retries):
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        
        if response.status_code == 429:
            # Rate limited, wait 10 seconds before trying again
            time.sleep(10)
            continue
            
        response.raise_for_status()
        return response.json()
        
    raise Exception("OpenRouter API Rate Limit Exceeded. The free tier is too busy. Please try again later.")

def run_tool(tool_call):
    tool_name = tool_call["function"]["name"]
    tool_args = json.loads(tool_call["function"]["arguments"])

    if tool_name in TOOL_FUNCTIONS:
        result = TOOL_FUNCTIONS[tool_name](**tool_args)
        return str(result)
    else:
        return f"Error: Tool '{tool_name}' not found."

def run_agent(system_prompt, user_content):
    """
    Runs a single agent step with a specific persona.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content}
    ]
    
    # We allow the agent to use tools if needed
    for step in range(3):
        result = call_llm(messages)
        
        if "choices" not in result:
            error_msg = result.get("error", "Unknown API Error: 'choices' key missing in response.")
            raise Exception(f"OpenRouter API Error: {error_msg}")
            
        message = result["choices"][0]["message"]
        messages.append(message)

        if "tool_calls" in message and message["tool_calls"]:
            for tool_call in message["tool_calls"]:
                tool_result = run_tool(tool_call)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "name": tool_call["function"]["name"],
                    "content": tool_result
                })
        else:
            return message.get("content", "No response generated.")
    return "Error: Agent did not produce a final response in time."

def process_resume_workflow(pdf_path, job_role, job_description=""):
    """
    Coordinates the Multi-Agent Workflow.
    """
    # 1. PDF Extraction Agent (Tool)
    resume_text = extract_pdf_text(pdf_path)
    if resume_text.startswith("Error"):
        return f"Failed to extract resume: {resume_text}"
        
    context = f"Target Role: {job_role}\nJob Description: {job_description}\n\nResume Text:\n{resume_text}"

    # 2. ATS Analysis Agent
    ats_output = run_agent(ATS_AGENT_PROMPT, context)
    time.sleep(3)  # Wait 3 seconds to avoid rate limits
    
    # 3. Grammar Agent
    grammar_output = run_agent(GRAMMAR_AGENT_PROMPT, context)
    time.sleep(3)
    
    # 4. Skills Matching Agent
    skills_output = run_agent(SKILLS_AGENT_PROMPT, context)
    time.sleep(3)
    
    # 5. Resume Improvement Agent
    improvement_output = run_agent(IMPROVEMENT_AGENT_PROMPT, context)
    time.sleep(3)
    
    # 6. Report Generation Agent
    report_context = f"""
    ATS Analysis: {ats_output}
    
    Grammar Issues: {grammar_output}
    
    Skills Matching: {skills_output}
    
    Improvement Suggestions: {improvement_output}
    """
    final_report = run_agent(REPORT_AGENT_PROMPT, report_context)
    
    return final_report

def chat_with_manager(user_input):
    """
    A simple chat interface to talk with the Manager agent after the report is generated.
    """
    memory = load_memory()
    messages = [{"role": "system", "content": MANAGER_PROMPT}]
    messages.extend(memory)
    messages.append({"role": "user", "content": user_input})

    result = call_llm(messages)
    message = result["choices"][0]["message"]
    final_answer = message.get("content", "No response generated.")
    
    messages.append(message)
    save_memory(messages[1:]) # skip system prompt
    return final_answer