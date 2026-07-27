from databricks_sdk_playground.workspace import create_workspace_folder


def test_create_workspace_folder():

    create_workspace_folder(
        "/Users/msandarsh25@gmail.com/sdk_playground_test"
    )

    assert True