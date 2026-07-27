from databricks_sdk_playground.tables import list_tables


def test_list_tables():

    tables = list_tables(
        catalog_name="dev_poc",
        schema_name="default"
    )

    assert isinstance(tables, list)