from databricks_sdk_playground.client import get_workspace_client


def test_workspace_client():

    client = get_workspace_client()

    assert client is not None