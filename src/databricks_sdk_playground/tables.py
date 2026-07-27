"""
Utility functions for working with Unity Catalog tables.
"""

from databricks_sdk_playground.client import get_workspace_client


def list_tables(
    catalog_name: str,
    schema_name: str,
    profile: str = "playground",
):
    """
    Return all tables and views from a schema.
    """
    w = get_workspace_client(profile)

    return list(
        w.tables.list(
            catalog_name=catalog_name,
            schema_name=schema_name,
        )
    )