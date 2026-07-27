from databricks_sdk_playground.jobs import list_jobs


def test_list_jobs():

    jobs = list_jobs()

    assert isinstance(jobs, list)