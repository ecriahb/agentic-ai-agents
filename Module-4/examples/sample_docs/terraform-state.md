# Terraform State Troubleshooting

## State Lock

When Terraform reports that state is locked, first determine whether another legitimate plan or apply operation is still running. Do not immediately force-unlock an active operation.

## Recovery

If the lock is stale, verify the backend and lock identity, confirm that no active Terraform operation owns it, and then use the approved recovery procedure for the backend in use.

## Prevention

Use a remote backend with appropriate locking and restrict concurrent infrastructure deployments for the same state. Pipeline concurrency controls can reduce accidental parallel applies.
