from databricks.sdk import WorkspaceClient

# Create a client using the CLI profile
w = WorkspaceClient(profile="playground")

JOB_NAME = "SDK Playground - Sample Notebook"

print("Searching for the job...\n")

job_id = None

# Find the job by name
for job in w.jobs.list():
    if job.settings and job.settings.name == JOB_NAME:
        job_id = job.job_id
        break

if job_id is None:
    print("Job not found!")
    exit()

print(f"Job found: {JOB_NAME}")
print(f"Job ID: {job_id}")

print("\nTriggering the job...")

# Trigger the job
run = w.jobs.run_now(job_id=job_id)

print("Job triggered successfully!")
print(f"Run ID: {run.run_id}")