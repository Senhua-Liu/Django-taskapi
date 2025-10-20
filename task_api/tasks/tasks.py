import time
from .models import Task

def process_task(task_id):
    task = Task.objects.get(id=task_id)
    try:
        print(f"Processing task: {task.title}")
        time.sleep(5)  # Simulation d’un long traitement
        task.status = 'COMPLETED'
    except Exception:
        task.status = 'FAILED'
    task.save()
