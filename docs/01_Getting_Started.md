# Getting Started with Databricks Python SDK

## Objective
Connect to a Databricks workspace using the Python SDK.

## Prerequisites
- Python 3.12
- Virtual Environment (.venv)
- databricks-sdk
- Databricks CLI profile

## Example
See `examples/01_connect.py`.

## Key Learnings
- `WorkspaceClient` is the entry point to the Databricks SDK.
- The SDK can use an authenticated Databricks CLI profile.
- `current_user.me()` verifies connectivity.