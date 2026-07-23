from databricks.sdk import WorkspaceClient

# Create a client using the CLI profile
w = WorkspaceClient(profile="playground")

print("Available Catalogs")
print("-" * 30)

# Retrieve all accessible catalogs
catalogs = w.catalogs.list()

# Display catalog names
for catalog in catalogs:
    print(catalog.name)