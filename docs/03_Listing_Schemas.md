# Listing Schemas using Databricks Python SDK

## Objective

Learn how to retrieve all schemas within a specific catalog using the Databricks Python SDK.

## Why list schemas?

Schemas organize tables, views, and other database objects within a catalog. Before querying or managing tables, it is often useful to discover the available schemas.

Hierarchy:

Catalog → Schema → Table

## Hands-on Example

Example file:

`examples/03_list_schemas.py`

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="playground")

catalog_name = "dev_poc"

schemas = w.schemas.list(catalog_name=catalog_name)

for schema in schemas:
    print(schema.name)
```

## Sample Output

```text
default
incremental_demo
information_schema
```

## Key Learnings

- `w.schemas` provides access to the Schemas API.
- `list()` requires a `catalog_name` because schemas belong to a catalog.
- The SDK returns schema objects, and `schema.name` displays the schema name.