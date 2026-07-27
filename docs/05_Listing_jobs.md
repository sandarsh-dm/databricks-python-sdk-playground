# Listing Jobs using Databricks Python SDK

## Objective

Learn how to retrieve all jobs available in a Databricks workspace using the Databricks Python SDK.

## Why list jobs?

Databricks Jobs automate notebooks, Python scripts, SQL queries, and workflows. Listing jobs helps understand the available workloads in a workspace and serves as the foundation for automation and monitoring.

## Example

See `examples/05_list_jobs.py`.

## Key Learnings

* `w.jobs` provides access to the Jobs API.
* `list()` retrieves all jobs available in the workspace.
* Each job object exposes metadata such as the job ID and job name.
* The Jobs API can be extended to create, trigger, and monitor job executions.

This keeps the style, length, and structure consistent with your `02_Listing_Catalogs.md`, `03_Listing_Schemas.md`, and `04_Listing_Tables.md`.
