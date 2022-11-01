from prefect import flow, get_run_logger
from prefect.filesystems import GitHub

github_block = GitHub.load("dev")

@flow
def my_docker_flow():
    logger = get_run_logger()
    logger.info("Hello from Docker!")
