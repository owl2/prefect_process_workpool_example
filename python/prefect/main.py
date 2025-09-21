from prefect import flow, task
from prefect.logging import get_run_logger


@task
def say_hello(name: str = "World") -> str:
    """Tâche simple qui dit bonjour"""
    logger = get_run_logger()
    message = f"Hello, {name}!"
    logger.info(message)
    return message


@flow(name="hello-world-flow", log_prints=True)
def hello_world_flow(name: str = "Prefect User"):
    """
    Flow simple Hello World avec plusieurs tâches
    """
    logger = get_run_logger()
    logger.info("🚀 Démarrage du flow Hello World")
    
    greeting = say_hello(name)
    
    logger.info(f"✅ Flow terminé")
    
    return


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/owl2/prefect_process_workpool_example.git",
        entrypoint="python/prefect/main.py:hello_world_flow",
    ).deploy(
        name="hello-world-deployment",
        work_pool_name="local-pool",
    )