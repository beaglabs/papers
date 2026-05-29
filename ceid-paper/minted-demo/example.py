def assign_task(task_id: str, robot_id: str) -> dict:
    return {
        "op": "assign_task",
        "taskId": task_id,
        "robotId": robot_id,
    }
