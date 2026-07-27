import time

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

print(f"Job found : {JOB_NAME}")
print(f"Job ID    : {job_id}")

# Get the latest run
runs = list(w.jobs.list_runs(job_id=job_id, limit=1))

if not runs:
    print("No runs found.")
    exit()

run_id = runs[0].run_id

print(f"Run ID    : {run_id}")

print("\nMonitoring job...\n")

while True:

    run = w.jobs.get_run(run_id=run_id)

    life_cycle = run.state.life_cycle_state
    result = run.state.result_state

    print(f"Status : {life_cycle}")

    if life_cycle.name == "TERMINATED":

        print("\nJob completed!")

        if result:
            print(f"Result : {result}")

        break

    time.sleep(5)