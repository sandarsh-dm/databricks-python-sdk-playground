"""
Utility functions for Databricks Workspace operations.
"""

from databricks_sdk_playground.client import get_workspace_client


def create_workspace_folder(
    workspace_path: str,
    profile: str = "playground",
):
    """
    Create a workspace folder if it does not already exist.
    """
    w = get_workspace_client(profile)
    w.workspace.mkdirs(workspace_path)