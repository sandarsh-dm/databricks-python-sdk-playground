# Listing Tables using Databricks Python SDK

## Objective

Learn how to retrieve tables and views from a schema using the Databricks Python SDK.

## Hierarchy

Catalog → Schema → Table

## Example

See `examples/04_list_tables.py`.

## Key Learnings

- `w.tables` provides access to the Tables API.
- Listing tables requires both catalog and schema names.
- Table objects expose metadata such as name and table type.
- Views can also appear in the results.