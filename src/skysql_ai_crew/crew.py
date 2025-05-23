import yaml
from crewai import Crew, Process, Agent, Task
from skysql_ai_crew.tools.skysql_tool import list_db_agents, chat_with_db_agent

def load_yaml_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

# Load agent from YAML
agent_cfg = load_yaml_config("src/skysql_ai_crew/config/agents.yaml")["db_chat_agent"]

db_chat_agent = Agent(
    role=agent_cfg["role"],
    goal=agent_cfg["goal"],
    backstory=agent_cfg["backstory"],
    tools=[list_db_agents, chat_with_db_agent],
    verbose=True
)

# Load task from YAML
task_cfg = load_yaml_config("src/skysql_ai_crew/config/tasks.yaml")["db_query_task"]

db_query_task = Task(
    description=task_cfg["description"],
    expected_output=task_cfg["expected_output"],
    agent=db_chat_agent
)

crew = Crew(
    agents=[db_chat_agent],
    tasks=[db_query_task],
    process=Process.sequential,
    verbose=True
)
