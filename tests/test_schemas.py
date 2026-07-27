from databricks_sdk_playground.schemas import list_schemas


def test_list_schemas():

    schemas = list_schemas("dev_poc")

    assert isinstance(schemas, list)