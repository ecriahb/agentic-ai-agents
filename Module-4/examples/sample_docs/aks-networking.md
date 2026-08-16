# AKS Networking Runbook

## Subnet and NSG Validation

If AKS workloads lose connectivity after a Terraform networking change, compare the applied Network Security Group rules with the approved AKS subnet requirements. Confirm that required inbound, outbound and intra-subnet paths were not removed unintentionally.

## Route Validation

Inspect route tables and effective routes for the affected subnet. A changed user-defined route can send traffic to the wrong next hop or block the expected path.

## DNS and Service Connectivity

If IP connectivity works but service names fail, validate cluster DNS behavior and the private DNS zones used by dependent Azure services.

## Safe Recovery

Restore the required network configuration through the controlled Infrastructure-as-Code process, validate connectivity, review the Terraform plan, and redeploy only after the expected network paths are confirmed.
