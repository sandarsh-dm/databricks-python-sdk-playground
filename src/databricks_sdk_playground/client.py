"""
Client module for creating a Databricks Workspace client.
"""

from databricks.sdk import WorkspaceClient


def get_workspace_client(profile: str = "playground") -> WorkspaceClient:
    """
    Create and return a Databricks WorkspaceClient.

    Args:
        profile: Databricks CLI authentication profile.

    Returns:
        WorkspaceClient instance.
    """

    return WorkspaceClient(profile=profile)