# Unity Catalog - Listing Catalogs using Databricks SDK

## Objective

Learn how to use the Databricks Python SDK to retrieve the list of catalogs available in a Databricks workspace.

## What is Unity Catalog?

Unity Catalog is Databricks' centralized governance solution for managing data and AI assets. It organizes data using a three-level hierarchy:

Catalog → Schema → Table/View

A catalog is the highest level in this hierarchy and contains one or more schemas.

## Hands-on Example

Example file:

`examples/02_list_catalogs.py`

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="playground")

catalogs = w.catalogs.list()

for catalog in catalogs:
    print(catalog.name)
```

## Sample Output

```text
dev_catalog
samples
workspace
sparkcatalog
...
```

## Key Learnings

- `WorkspaceClient` is the entry point to the Databricks SDK.
- `w.catalogs` provides access to the Catalogs API.
- `list()` returns catalog objects that the authenticated user can access.
- `catalog.name` retrieves the name of each catalog.

## References

- Databricks SDK for Python
- Unity Catalog Documentation