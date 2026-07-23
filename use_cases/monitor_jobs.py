from databricks.sdk import WorkspaceClient
from datetime import datetime

# Create a client using the CLI profile
w = WorkspaceClient(profile="playground")

print("=" * 60)
print("Databricks Job Monitoring Report")
print(f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}")
print("=" * 60)

jobs = list(w.jobs.list())

print(f"\nTotal Jobs Found: {len(jobs)}")
print("-" * 60)

for job in jobs:
    print(f"Job Name : {job.settings.name}")
    print(f"Job ID   : {job.job_id}")
    print("-" * 60)