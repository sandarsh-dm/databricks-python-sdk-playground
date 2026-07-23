from databricks.sdk import WorkspaceClient

# Create a client using the CLI profile
w = WorkspaceClient(profile="playground")

print("Available Jobs")
print("-" * 40)

# Retrieve all jobs
jobs = w.jobs.list()

# Display job details
for job in jobs:
    print(f"Job ID   : {job.job_id}")
    print(f"Job Name : {job.settings.name if job.settings else 'N/A'}")
    print("-" * 40)