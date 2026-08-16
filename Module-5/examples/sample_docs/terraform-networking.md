# Terraform Networking Change Guide

Terraform networking changes can modify NSG rules, subnet associations, route tables and private endpoint related configuration. Review the Terraform plan carefully before apply and compare high-risk network changes with the expected architecture.

If an AKS deployment fails after Terraform Apply, inspect the exact resources changed. Pay special attention to removed NSG allow rules, subnet changes and route-table updates because those can affect cluster connectivity.

A recommended investigation sequence is: capture the Terraform plan/apply output, identify changed network resources, compare with the approved baseline, validate effective network configuration and only then prepare a rollback or corrective change.
