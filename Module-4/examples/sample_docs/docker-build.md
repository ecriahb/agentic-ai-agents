# Docker Build Optimization

## Large Images

Use smaller appropriate base images where practical and multi-stage builds so build-time dependencies do not automatically remain in the final runtime image.

## Build Context

Use `.dockerignore` to exclude unnecessary local files from the build context. Avoid copying source-control metadata, temporary files and unrelated artifacts into the image.

## Layer Efficiency

Order Dockerfile instructions so stable dependency layers can be cached effectively. Clean package-manager caches when appropriate and avoid creating unnecessary duplicate layers.
