"""
Utility functions for working with Databricks Jobs.
"""

from databricks_sdk_playground.client import get_workspace_client


def list_jobs(profile: str = "playground"):
    """
    Return all Databricks jobs.
    """
    w = get_workspace_client(profile)
    return list(w.jobs.list())