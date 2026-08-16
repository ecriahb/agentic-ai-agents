# AKS Networking Runbook

AKS workloads depend on correct subnet routing, Network Security Group rules, DNS resolution and any required private endpoint connectivity. After a networking change, validate the AKS subnet NSG rules, route table associations, effective routes and DNS resolution before assuming an application defect.

If workloads cannot reach an internal service, compare the current subnet configuration with the approved baseline. Check whether required allow rules were removed or whether a new deny rule has higher priority.

For production incidents, collect evidence first. Record the failing destination, namespace, pod, subnet, relevant NSG rules and route information before proposing remediation. Do not make destructive networking changes without normal change/approval controls.
