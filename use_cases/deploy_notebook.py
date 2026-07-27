import base64

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ImportFormat, Language

# Create a client using the CLI profile
w = WorkspaceClient(profile="playground")

# Local notebook path
local_file = "notebooks/sample_notebook.py"

# Destination folder in Databricks Workspace
workspace_folder = "/Users/msandarsh25@gmail.com/sdk_playground"

# Destination notebook path
workspace_notebook = f"{workspace_folder}/sample_notebook"

print("Connected successfully!")
print(f"Local File       : {local_file}")
print(f"Workspace Folder : {workspace_folder}")
print(f"Workspace Path   : {workspace_notebook}")

print("\nCreating workspace folder...")

# Create the folder if it doesn't already exist
w.workspace.mkdirs(workspace_folder)

print("Workspace folder is ready.")

# Read the local notebook file
with open(local_file, "rb") as file:
    notebook_content = file.read()

print(f"Notebook loaded successfully ({len(notebook_content)} bytes)")

# Convert notebook content to Base64
encoded_content = base64.b64encode(notebook_content).decode("utf-8")

print("Notebook encoded successfully.")

print("\nImporting notebook into Databricks Workspace...")

# Import the notebook into the Databricks Workspace
w.workspace.import_(
    path=workspace_notebook,
    content=encoded_content,
    format=ImportFormat.SOURCE,
    language=Language.PYTHON,
    overwrite=True,
)

print("Notebook imported successfully!")