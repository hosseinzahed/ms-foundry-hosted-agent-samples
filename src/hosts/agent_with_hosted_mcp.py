import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ImageBasedHostedAgentDefinition, ProtocolVersionRecord, AgentProtocol
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv(override=True) # Load environment variables from .env file

azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai_api_version = os.getenv("OPENAI_API_VERSION")
project_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
api_key = os.getenv("AZURE_AI_PROJECT_API_KEY")
model_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
container_registry_name = os.getenv("AZURE_CONTAINER_REGISTRY_NAME")
agent_name="agent-with-hosted-mcp"

# Initialize the client
client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential()
)

# Create the agent from a container image
agent = client.agents.create_version(
    agent_name=agent_name,
    definition=ImageBasedHostedAgentDefinition(
        container_protocol_versions=[ProtocolVersionRecord(protocol=AgentProtocol.RESPONSES, version="v1")],
        cpu="1",
        memory="2Gi",
        image=f"{container_registry_name}.azurecr.io/{agent_name}:v1",
        environment_variables={
            "AZURE_OPENAI_ENDPOINT": azure_openai_endpoint,
            "OPENAI_API_VERSION": openai_api_version,
            "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME": model_name,
        }
    )
)

print (f"Created agent: {agent.id} with version: {agent.version}")