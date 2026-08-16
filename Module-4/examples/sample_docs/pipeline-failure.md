# Deployment Pipeline Failure Guide

## Terraform Apply Failure

When a deployment pipeline fails during Terraform Apply, preserve the pipeline logs and Terraform plan/apply output. Identify the first concrete error instead of relying only on the final pipeline failure message.

## Change Correlation

Compare the failure timestamp with recent infrastructure changes. Networking, identity, provider configuration and resource dependency changes are common areas to validate, but the RCA must be supported by collected evidence.

## Safe Retry

Do not repeatedly retry a failed infrastructure deployment without understanding whether the previous apply partially changed resources. Review current state and the next plan before another apply.
