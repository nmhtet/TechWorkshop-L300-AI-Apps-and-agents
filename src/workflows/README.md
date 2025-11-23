# GitHub Actions Workflow Examples

This directory contains example GitHub Actions workflow files for automating deployments in Exercise 05: Agentic DevOps.

## Overview

These workflow files are **examples/templates** that you should copy to your `.github/workflows/` directory and customize for your environment. They are not active workflows in their current location.

## Available Workflow Examples

### 1. `0501_deployment.yml` - Deploy to Azure Container Registry

**Purpose:** Automates deployment of the chat application to an Azure Container Registry.

**Triggered by:**
- Push to `main` branch with changes in `src/**`
- Manual workflow dispatch

**Required GitHub Secrets:**
- `AZURE_CONTAINER_REGISTRY` - The name of your Azure Container Registry (e.g., `myregistry.azurecr.io`)
- `AZURE_CONTAINER_REGISTRY_USERNAME` - The username for your Azure Container Registry
- `AZURE_CONTAINER_REGISTRY_PASSWORD` - The password for your Azure Container Registry
- `ENV` - The complete contents of your local `.env` file

**To use this workflow:**
1. Copy this file to `.github/workflows/deploy-to-acr.yml`
2. Configure the required secrets in your GitHub repository settings (Settings → Secrets and variables → Actions)
3. Adjust any environment-specific values as needed
4. Commit and push to trigger the workflow

### 2. `0502_sample_agent_deployment.yml` - Deploy Customer Loyalty Agent

**Purpose:** Automates deployment of the Customer Loyalty Agent to Azure AI Foundry.

**Triggered by:**
- Changes to agent initializer, prompts, tools, or workflow file
- Manual workflow dispatch

**Required GitHub Secrets:**
- `AZURE_CREDENTIALS` - The JSON output from creating a service principal (see instructions below)
- `ENV` - The complete contents of your local `.env` file

**To use this workflow:**
1. Create a service principal (see instructions below)
2. Copy this file to `.github/workflows/deploy-customer-loyalty-agent.yml`
3. Configure the required secrets in your GitHub repository settings
4. Create similar workflows for other agents (Shopping Assistant, Inventory, Order Management)
5. Commit and push to trigger the workflow

## Setting Up GitHub Secrets

### Creating GitHub Secrets

1. Navigate to your repository on GitHub
2. Go to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each required secret with its corresponding value

### Creating a Service Principal for Azure

To create the `AZURE_CREDENTIALS` secret, run the following Azure CLI command:

```bash
az ad sp create-for-rbac --name "TechWorkshopL300AzureAI" --sdk-auth --role contributor --scopes /subscriptions/{SUB_ID}/resourceGroups/{RG}
```

Replace `{SUB_ID}` with your Azure subscription ID and `{RG}` with your resource group name.

Copy the entire JSON output and paste it as the value for the `AZURE_CREDENTIALS` secret.

### Granting Service Principal Access

After creating the service principal, grant it the **Azure AI User** role on your Azure AI Foundry resource:

1. Navigate to your Azure AI Foundry resource in the Azure Portal
2. Go to **Access control (IAM)**
3. Click **+ Add** → **Add role assignment**
4. Select the **Azure AI User** role
5. Search for and select `TechWorkshopL300AzureAI`
6. Click **Review + assign**

## Additional Resources

- [Exercise 05 Documentation](../../docs/05_agentic_devops/05_agentic_devops.md)
- [Task 05_01: Automate container deployment](../../docs/05_agentic_devops/05_01.md)
- [Task 05_02: Automate agent deployment](../../docs/05_agentic_devops/05_02.md)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Azure Container Registry Documentation](https://docs.microsoft.com/azure/container-registry/)

## Customization Tips

1. **Adjust trigger paths:** Modify the `paths:` section to match your file structure
2. **Add more agents:** Create additional workflows based on `0502_sample_agent_deployment.yml` for each agent
3. **Environment-specific values:** Update registry names, image names, and other environment-specific values
4. **Branch protection:** Consider configuring branch protection rules to require successful workflow runs before merging

## Troubleshooting

- **Workflow not triggering:** Ensure the workflow file is in `.github/workflows/` directory
- **Authentication errors:** Verify that all secrets are correctly configured
- **Permission errors:** Confirm the service principal has the necessary permissions on your Azure resources
- **Build failures:** Check the workflow logs in the Actions tab for detailed error messages
