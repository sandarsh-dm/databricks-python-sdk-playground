from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="playground")

catalog_name = "dev_poc"
schema_name = "incremental_demo"

print(f"Tables in {catalog_name}.{schema_name}")
print("-" * 40)

tables = w.tables.list(
    catalog_name=catalog_name,
    schema_name=schema_name
)

for table in tables:
    print(table.name)