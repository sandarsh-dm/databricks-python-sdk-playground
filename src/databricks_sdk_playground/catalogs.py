"""
Utility functions for working with Unity Catalog catalogs.
"""

from databricks_sdk_playground.client import get_workspace_client


def list_catalogs(profile: str = "playground"):
    """
    Return all available Unity Catalog catalogs.
    """
    w = get_workspace_client(profile)
    return list(w.catalogs.list())