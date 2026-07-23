from databricks.sdk import WorkspaceClient

# Create a client using the CLI profile
w = WorkspaceClient(profile="playground")

catalog_name = "dev_poc"

print(f"Schemas in catalog: {catalog_name}")
print("-" * 40)

# List all schemas in the catalog
schemas = w.schemas.list(catalog_name=catalog_name)

for schema in schemas:
    print(schema.name)