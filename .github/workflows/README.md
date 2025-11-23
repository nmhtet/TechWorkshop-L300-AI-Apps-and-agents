# GitHub Actions Workflows

## Customer Loyalty Agent Deployment

The `customer-loyalty-agent.yml` workflow automatically deploys the Customer Loyalty Agent when relevant files are modified.

### Triggers

This workflow runs automatically when changes are pushed to any of the following files:
- `src/app/agents/customerLoyaltyAgent_initializer.py` - The main agent initialization script
- `src/prompts/CustomerLoyaltyAgentPrompt.txt` - The agent's prompt configuration
- `src/app/tools/discountLogic.py` - The discount calculation tool used by the agent

The workflow can also be triggered manually using the "workflow_dispatch" option in the GitHub Actions UI.

### Required GitHub Secrets

The following secrets must be configured in your repository settings (Settings → Secrets and variables → Actions):

#### Azure Authentication
- `AZURE_CLIENT_ID` - Azure Service Principal Client ID
- `AZURE_TENANT_ID` - Azure Tenant ID
- `AZURE_SUBSCRIPTION_ID` - Azure Subscription ID

#### Azure AI Agent Configuration
- `AZURE_AI_AGENT_ENDPOINT` - The endpoint URL for Azure AI Agent service
- `AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME` - The name of the deployed AI model

#### Azure OpenAI Configuration
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI service endpoint
- `AZURE_OPENAI_KEY` - Azure OpenAI API key
- `GPT_DEPLOYMENT` - The name of the GPT deployment

#### Application Insights
- `APPLICATIONINSIGHTS_CONNECTION_STRING` - Connection string for Azure Application Insights

### Workflow Steps

1. **Checkout repository** - Retrieves the latest code
2. **Set up Python** - Installs Python 3.11 with pip caching
3. **Install dependencies** - Installs Python packages from `src/requirements.txt`
4. **Azure Login** - Authenticates to Azure using the service principal
5. **Set up environment variables** - Configures required environment variables
6. **Execute Customer Loyalty Agent Initializer** - Runs the Python script to deploy/update the agent

### Azure Authentication Setup

The workflow uses Azure's federated identity credential (workload identity) for authentication. To set this up:

1. Create a service principal in Azure AD
2. Configure federated credentials for GitHub Actions
3. Grant the service principal appropriate permissions for Azure AI Projects
4. Add the service principal credentials as GitHub secrets

For detailed instructions, see: https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure
