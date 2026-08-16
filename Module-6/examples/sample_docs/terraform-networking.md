# Terraform Networking Change Guide

Terraform network changes can modify NSG rules, route tables, private endpoint configuration and subnet associations. Review the plan for removed or replaced rules, not only added resources.

For AKS-related incidents, compare the applied Terraform change with expected subnet traffic requirements. A reference document describes what can cause a problem; the current incident still requires live plan/apply and platform evidence.
