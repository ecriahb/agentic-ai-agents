# Deployment Pipeline Failure Guide

A deployment pipeline can fail during or after Terraform Apply when infrastructure validation detects an invalid or unreachable dependency. Always preserve the pipeline error output and the infrastructure change evidence before generating an RCA.

For networking-related failures, correlate the failed pipeline stage with the Terraform changes and the post-deployment connectivity checks. A failed validation is evidence of the observed symptom; the underlying cause must still be supported by configuration or change evidence.

Recommended evidence includes the pipeline stage, exact error text, Terraform plan/apply summary, environment, affected component and relevant infrastructure validation results.
