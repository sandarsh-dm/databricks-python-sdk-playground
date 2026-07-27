from databricks_sdk_playground.catalogs import list_catalogs


def test_list_catalogs():

    catalogs = list_catalogs()

    assert isinstance(catalogs, list)