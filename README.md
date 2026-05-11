# Basic Agent Framework - Responses API

A basic Agent Framework agent hosted with the responses API.

## Prerequisites

- Python 3.10+
- An Azure AI Foundry project with a deployed model

## Getting Started

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Set the environment variables in the `.env` file with your project endpoint and model deployment name.

3. Log in to Azure:

   ```bash
   az login
   ```

4. Run the agent:

   ```bash
   python main.py
   ```

## Interacting with the Agent

Send a POST request to the server with a JSON body containing an `input` field:

```bash
curl -X POST http://localhost:8088/responses -H "Content-Type: application/json" -d '{"input": "Hi"}'
```

### Multi-turn Conversation

Use the previous response ID from the response body to continue the conversation:

```bash
curl -X POST http://localhost:8088/responses -H "Content-Type: application/json" -d '{"input": "How are you?", "previous_response_id": "<RESPONSE_ID>"}'
```

## Deploying to Microsoft Foundry

To deploy your agent to Microsoft Foundry:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Microsoft Foundry: Deploy Hosted Agent**.
3. The extension reads `agent.yaml` and auto-populates what it can. You may be prompted for:
   - **Agent name** -- the name registered with the hosting service.
   - **Dockerfile** -- auto-detected from workspace root, or select manually.
   - **Container registry** -- defaults to auto-created; optionally provide your own ACR.
   - **Resource size** -- CPU and memory allocation:

     | Option                        | CPU  | Memory |
     | ----------------------------- | ---- | ------ |
     | 0.25 CPU cores, 0.5 Gi memory | 0.25 | 0.5 Gi |
     | 0.5 CPU cores, 1 Gi memory    | 0.5  | 1.0 Gi |
     | 1 CPU cores, 2 Gi memory      | 1.0  | 2.0 Gi |
     | 2 CPU cores, 4 Gi memory      | 2.0  | 4.0 Gi |

4. The extension builds the container image in ACR, creates the agent version, and assigns required RBAC roles automatically.

## Troubleshooting

### Azure OpenAI Permission Denied (401)

The identity running the agent does not have the required RBAC roles on the Azure AI Foundry project. Assign the following roles:

- **Cognitive Services OpenAI User**
- **Azure AI User**

Use the Azure CLI to assign them:

```
az role assignment create \
  --assignee <principal-id> \
  --role "Cognitive Services OpenAI User" \
  --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.CognitiveServices/accounts/<ai-services-account-name>

az role assignment create \
  --assignee <principal-id> \
  --role "Azure AI User" \
  --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.CognitiveServices/accounts/<ai-services-account-name>
```

> **Note:** It may take a few minutes for role assignments to propagate. Retry the request after waiting.
