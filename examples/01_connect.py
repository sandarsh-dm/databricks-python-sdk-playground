from databricks.sdk import WorkspaceClient

# Create a client using the "playground" CLI profile
w = WorkspaceClient(profile="playground")

# Get details of the authenticated user
current_user = w.current_user.me()

print(f"Connected successfully!")
print(f"User: {current_user.user_name}")