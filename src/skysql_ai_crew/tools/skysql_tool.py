# src/skysql_ai_crew/tools/skysql_tool.py

import os
import requests
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()
SKYSQL_API_KEY = os.getenv("SKYSQL_API_KEY")
SKYSQL_API_URL = "https://api.skysql.com"

@tool("list_db_agents")
def list_db_agents() -> str:
    """Lists available DB agents from SkySQL."""
    response = requests.get(
        f"{SKYSQL_API_URL}/copilot/v1/agent/",
        headers={"X-API-Key": SKYSQL_API_KEY, "Content-Type": "application/json"}
    )
    response.raise_for_status()
    agents = response.json()
    return "\n".join([
        f"{a['id']}: {a['name']} - {a['description']}" for a in agents
    ])

@tool("chat_with_db_agent")
def chat_with_db_agent(agent_id: str, prompt: str) -> str:
    """Chats with a SkySQL agent by providing a prompt and agent ID."""
    response = requests.post(
        f"{SKYSQL_API_URL}/copilot/v1/chat/",
        headers={"X-API-Key": SKYSQL_API_KEY, "Content-Type": "application/json"},
        json={"prompt": prompt, "agent_id": agent_id}
    )
    response.raise_for_status()
    result = response.json()
    content = result.get("response", {}).get("content", "No content.")
    sql = result.get("response", {}).get("sql_text")
    return f"{content}\n\n**SQL:**\n```\n{sql}\n```" if sql else content
