import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ToolSet
from dotenv import load_dotenv
from agent_processor import create_function_tool_for_agent
from agent_initializer import initialize_agent

load_dotenv()



CL_PROMPT_TARGET = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'prompts', 'CustomerLoyaltyAgentPrompt.txt')
with open(CL_PROMPT_TARGET, 'r', encoding='utf-8') as file:
    CL_PROMPT = file.read()



project_endpoint = os.environ["AZURE_AI_AGENT_ENDPOINT"]

project_client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),
)



# Define the set of user-defined callable functions to use as tools (from MCP client)
functions = create_function_tool_for_agent("customer_loyalty")
toolset = ToolSet()
toolset.add(functions)
project_client.agents.enable_auto_function_calls(tools=functions)




def initialize_agent(project_client : AIProjectClient, model : str, env_var_name : str, name : str, instructions : str, toolset : ToolSet):
    agent_id = os.environ[env_var_name]
    with project_client:
        agent_exists = False
        if agent_id:
            # Check if agent exists.
            agent = project_client.agents.get_agent(agent_id)
            print(f"Retrieved existing agent, ID: {agent.id}")
            agent_exists = True
        
        if agent_exists:
            agent = project_client.agents.update_agent(
                agent_id=agent.id,
                model=model,
                name=name,
                instructions=instructions,
                toolset=toolset
            )
            print(f"Updated {env_var_name} agent, ID: {agent.id}")
        else:
            agent = project_client.agents.create_agent(
            model=model,
            name=name,
            instructions=instructions,
            toolset=toolset
            )
            print(f"Created {env_var_name} agent, ID: {agent.id}")

