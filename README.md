# 🤖 Microsoft Foundry Hosted Agent Samples

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Azure AI](https://img.shields.io/badge/Azure-AI%20Foundry-0078D4.svg)](https://azure.microsoft.com/en-us/products/ai-services)

A collection of sample agents demonstrating how to build, host, and deploy AI agents using the [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) and [Azure AI AgentServer SDK](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.agentserver.agentframework-readme). These samples showcase different patterns for creating intelligent agents that can be deployed to Microsoft Foundry using Azure Developer CLI.

## ⚠️ Important Notice

All samples and other resources made available in this GitHub repository are designed to assist in accelerating development of agents, solutions, and agent workflows for various scenarios. Review all provided resources and carefully test output behavior in the context of your use case. AI responses may be inaccurate and AI actions should be monitored with human oversight. Learn more in the transparency documents for [Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/agents/transparency-note) and [Agent Framework](https://github.com/microsoft/agent-framework/blob/main/TRANSPARENCY_FAQ.md).

Agents, solutions, or other output you create may be subject to legal and regulatory requirements, may require licenses, or may not be suitable for all industries, scenarios, or use cases. By using any sample, you are acknowledging that any output created using those samples are solely your responsibility, and that you will comply with all applicable laws, regulations, and relevant safety standards, terms of service, and codes of conduct.

Third-party samples contained in this folder are subject to their own designated terms, and they have not been tested or verified by Microsoft or its affiliates.

Microsoft has no responsibility to you or others with respect to any of these samples or any resulting output.

## 📋 Table of Contents

- [Available Samples](#-available-samples)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Running Locally](#-running-locally)
- [Deployment](#-deployment)
- [Testing Your Agent](#-testing-your-agent)
- [Troubleshooting](#-troubleshooting)
- [Resources](#-resources)

## 🎯 Available Samples

This repository contains three agent samples, each demonstrating different capabilities:

### 1️⃣ Agent with Hosted MCP
**Location:** [`src/agent-with-hosted-mcp/`](src/agent-with-hosted-mcp/)

Demonstrates how to integrate a Hosted Model Context Protocol (MCP) server with your agent. This sample connects to Microsoft Learn's MCP server to answer documentation questions.

**Features:**
- 🔌 Hosted MCP Tool integration
- 📚 Microsoft Learn documentation search
- 🤖 Azure OpenAI-powered responses
- 🌐 REST API endpoint (OpenAI Responses protocol)

**Use Cases:**
- Documentation Q&A systems
- Knowledge base integration
- External tool/API integration through MCP

[📖 View detailed README](src/agent-with-hosted-mcp/README.md)

---

### 2️⃣ Custom Agent
**Location:** [`src/custom-agent/`](src/custom-agent/)

Shows how to create a completely custom agent by extending the `BaseAgent` class. This echo agent demonstrates the minimal implementation required for both streaming and non-streaming responses.

**Features:**
- 🛠️ Custom agent implementation from scratch
- 💬 Streaming and non-streaming support
- 🎨 Full control over agent behavior
- 📝 Message processing patterns

**Use Cases:**
- Custom business logic implementation
- Specialized agent behaviors
- Integration with proprietary systems
- Learning agent framework fundamentals

[📖 View detailed README](src/custom-agent/README.md)

---

### 3️⃣ Web Search Agent
**Location:** [`src/web-search-agent/`](src/web-search-agent/)

Demonstrates integration with Bing Grounding (web search) to create an agent that can search the web for current information.

**Features:**
- 🔍 Bing web search integration
- 🌍 Real-time information retrieval
- 📊 Source citation
- 🔗 Connection-based tool configuration

**Use Cases:**
- Current events queries
- Research assistants
- Fact-checking systems
- Information aggregation

[📖 View detailed README](src/web-search-agent/README.md)

## 🔧 Prerequisites

Before running these samples, ensure you have:

- ✅ **Python 3.10 or higher** installed
- ✅ **Azure CLI** installed and authenticated (`az login`)
- ✅ **Azure OpenAI** endpoint and deployment (for MCP and web search agents)
- ✅ **Azure AI Foundry project** (for deployment)
- ✅ **Bing Grounding connection** (for web search agent only)
- ✅ **Docker** (optional, for containerization)

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hosseinzahed/ms-foundry-hosted-agent-samples.git
   cd ms-foundry-hosted-agent-samples
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # For MCP agent
   export AZURE_OPENAI_ENDPOINT="https://your-openai-resource.openai.azure.com/"
   export AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="gpt-4o-mini"
   
   # For web search agent
   export AZURE_AI_PROJECT_ENDPOINT="https://your-project.api.azureml.ms"
   export AZURE_AI_MODEL_DEPLOYMENT_NAME="gpt-4o-mini"
   export BING_GROUNDING_CONNECTION_ID="your-bing-connection-id"
   ```

4. **Run a sample agent locally:**
   ```bash
   # Choose one:
   python src/agent-with-hosted-mcp/main.py
   python src/custom-agent/main.py
   python src/web-search-agent/main.py
   ```

5. **Test the agent:**
   ```bash
   curl -X POST http://localhost:8088/responses \
     -H "Content-Type: application/json" \
     -d '{"input": "Hello, how can you help me?", "stream": false}'
   ```

## 📁 Project Structure

```
ms-foundry-hosted-agent-samples/
├── 📄 README.md                          # This file
├── 📄 LICENSE                            # MIT License
├── 📄 requirements.txt                   # Root dependencies
├── 📂 src/
│   ├── 📄 chat.http                      # HTTP test requests
│   ├── 📂 agent-with-hosted-mcp/         # MCP integration sample
│   │   ├── 📄 main.py                    # Agent entry point
│   │   ├── 📄 agent.yaml                 # Agent configuration
│   │   ├── 📄 Dockerfile                 # Container definition
│   │   ├── 📄 requirements.txt           # Dependencies
│   │   └── 📄 README.md                  # Sample documentation
│   ├── 📂 custom-agent/                  # Custom agent sample
│   │   ├── 📄 main.py                    # Custom agent implementation
│   │   ├── 📄 agent.yaml                 # Agent configuration
│   │   ├── 📄 Dockerfile                 # Container definition
│   │   ├── 📄 requirements.txt           # Dependencies
│   │   └── 📄 README.md                  # Sample documentation
│   ├── 📂 web-search-agent/              # Web search sample
│   │   ├── 📄 main.py                    # Agent with Bing search
│   │   ├── 📄 agent.yaml                 # Agent configuration
│   │   ├── 📄 Dockerfile                 # Container definition
│   │   ├── 📄 requirements.txt           # Dependencies
│   │   └── 📄 README.md                  # Sample documentation
│   └── 📂 hosts/                         # Deployment scripts
│       ├── 📄 agent_with_hosted_mcp.py   # Deploy MCP agent
│       ├── 📄 custom_agent.py            # Deploy custom agent
│       └── 📄 web_search_agent.py        # Deploy web search agent
```

## 💻 Running Locally

Each sample can be run locally using Python. Navigate to the specific sample directory and follow its README for detailed instructions.

**General pattern:**

```bash
# Navigate to sample directory
cd src/<sample-name>/

# Install dependencies
pip install -r requirements.txt

# Set required environment variables (see sample README)
export AZURE_OPENAI_ENDPOINT="..."
export AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="..."

# Run the agent
python main.py
```

The agent will start on `http://localhost:8088/` by default.

### 🧪 Using Host Scripts

Alternatively, you can use the host scripts in [`src/hosts/`](src/hosts/) to deploy agents to Azure:

```bash
cd src/hosts/
python agent_with_hosted_mcp.py
python custom_agent.py
python web_search_agent.py
```

## 🚢 Deployment

Deploy your agents to Microsoft Foundry using the Azure Developer CLI with the [ai agent extension](https://aka.ms/azdaiagent/docs).

### Using Azure Developer CLI

```bash
# Install azd ai agent extension
azd extension install ai-agent

# Initialize and deploy
cd src/<sample-name>/
azd ai agent deploy
```

### Manual Container Deployment

1. **Build the container image:**
   ```bash
   docker build -t <your-registry>/<agent-name>:v1 .
   ```

2. **Push to Azure Container Registry:**
   ```bash
   docker push <your-registry>/<agent-name>:v1
   ```

3. **Deploy using the host script:**
   ```bash
   python src/hosts/<agent-host-script>.py
   ```

For complete deployment instructions, see the [official documentation](https://aka.ms/azdaiagent/docs).

## 🧪 Testing Your Agent

### Using cURL

```bash
# Non-streaming request
curl -X POST http://localhost:8088/responses \
  -H "Content-Type: application/json" \
  -d '{
    "input": "What is Azure AI Foundry?",
    "stream": false
  }'

# Streaming request
curl -X POST http://localhost:8088/responses \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Explain agent framework",
    "stream": true
  }'
```

### Using HTTP Files

The repository includes [`src/chat.http`](src/chat.http) for testing with REST Client extensions in VS Code or other IDEs.

### Using Python

```python
import requests

response = requests.post(
    "http://localhost:8088/responses",
    json={"input": "Hello!", "stream": False}
)
print(response.json())
```

## 🔍 Troubleshooting

### Images built on Apple Silicon or other ARM64 machines

**Problem:** Container images built on ARM64 machines (e.g., Apple Silicon Macs) don't work on Azure services.

**Solution:** Use cloud build with `azd` (recommended) or force `linux/amd64` platform:

```dockerfile
FROM --platform=linux/amd64 python:3.12-slim
```

### Authentication Issues

Ensure you're logged in to Azure CLI:
```bash
az login
az account show
```

### Port Already in Use

If port 8088 is already in use, modify the `host` parameter in `main.py`:

```python
from_agent_framework(lambda _: create_agent()).run(host="127.0.0.1", port=8089)
```

### Missing Environment Variables

Double-check that all required environment variables are set for your chosen sample. See each sample's README for specific requirements.

## 📚 Resources

- 📖 [Microsoft Agent Framework Documentation](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview)
- 🔧 [Azure AI AgentServer SDK](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.agentserver.agentframework-readme)
- 🚀 [Azure Developer CLI ai agent Extension](https://aka.ms/azdaiagent/docs)
- 🤖 [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-services)
- 📋 [Agent Service Transparency Note](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/agents/transparency-note)
- ❓ [Agent Framework Transparency FAQ](https://github.com/microsoft/agent-framework/blob/main/TRANSPARENCY_FAQ.md)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 💬 Support

For questions and support:
- 📝 Open an issue in this repository
- 📖 Check the [official documentation](https://learn.microsoft.com/en-us/agent-framework/)
- 💡 Review individual sample READMEs for specific guidance

---

**Made with ❤️ by the Microsoft AI Platform team**
