from .methods import do_something
from huey.contrib.djhuey import task

@task()
def task_do_something():
    """
    This function is a task that runs the do_something method.
    It can be called from anywhere in the codebase.
    """
    do_something()