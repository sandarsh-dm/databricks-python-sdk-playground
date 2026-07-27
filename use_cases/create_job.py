from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import Task, NotebookTask

# Create a client using the CLI profile
w = WorkspaceClient(profile="playground")

# Notebook deployed in the previous step
NOTEBOOK_PATH = "/Users/msandarsh25@gmail.com/sdk_playground/sample_notebook"

print("Creating Databricks Job...\n")

job = w.jobs.create(
    name="SDK Playground - Sample Notebook",
    tasks=[
        Task(
            task_key="run_sample_notebook",
            notebook_task=NotebookTask(
                notebook_path=NOTEBOOK_PATH
            )
        )
    ]
)

print("Job created successfully!")
print(f"Job ID   : {job.job_id}")
print(f"Job Name : SDK Playground - Sample Notebook")