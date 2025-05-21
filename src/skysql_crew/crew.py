from crewai import Crew, Process
from crewai.config import ConfigLoader
from crewai.agent import Agent
from crewai.task import Task
from skysql_crew.tools.skysql_tools import list_db_agents, chat_with_db_agent

config = ConfigLoader(path="src/skysql_crew/config")
agents = config.load_agents()
tasks = config.load_tasks()

# Inject tool functions manually
agents["db_chat_agent"].tools = [list_db_agents, chat_with_db_agent]
tasks["db_query_task"].agent = agents["db_chat_agent"]

crew = Crew(
    agents=[agents["db_chat_agent"]],
    tasks=[tasks["db_query_task"]],
    process=Process.sequential,
    verbose=True
)
