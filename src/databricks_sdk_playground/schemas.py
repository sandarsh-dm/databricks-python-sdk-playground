"""
Utility functions for working with Unity Catalog schemas.
"""

from databricks_sdk_playground.client import get_workspace_client


def list_schemas(catalog_name: str, profile: str = "playground"):
    """
    Return all schemas for a given catalog.
    """
    w = get_workspace_client(profile)
    return list(w.schemas.list(catalog_name=catalog_name))