# AKS Networking Runbook

AKS workload connectivity depends on valid subnet routing, NSG rules, DNS resolution and any required firewall paths. After network-related infrastructure changes, validate effective NSG rules and routes before assuming the application itself is broken.

If subnet connectivity validation becomes degraded after a security-rule change, compare the active network configuration with the approved Terraform design. This runbook is reference knowledge and does not prove the cause of a current incident without live evidence.
