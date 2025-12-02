from datetime import datetime

def generate_schedule(tasks):
    task_list = []

    for t in tasks:
        deadline = datetime.strptime(t["deadline"], "%Y-%m-%d")
        days_left = (deadline - datetime.now()).days + 1

        urgency = max(1, 10 - days_left)
        priority_score = int(t["difficulty"]) * urgency

        task_list.append({
            "id": t["id"],
            "task": t["task"],
            "deadline": t["deadline"],
            "priority": priority_score,
            "completed": t["completed"]
        })

    task_list.sort(key=lambda x: x["priority"], reverse=True)
    return task_list
