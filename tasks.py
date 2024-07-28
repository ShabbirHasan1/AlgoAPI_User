from fastapi import APIRouter

from taskscheduler import *

tasksrouter = APIRouter()

@tasksrouter.get("/")
async def get_tasks():
    return {"message": "Tasks!"}

@tasksrouter.get("/list")
async def list_tasks():
    jobs = []
    for job in TaskScheduler.get_jobs():
        jobs.append({
            "id": job.id,
            "name": job.name,
            "trigger": str(job.trigger)
            # "next_run_time": str(job)
        })
    return {"tasks": jobs}


@tasksrouter.post("/start/{task_id}")
async def start_task(task_id: str):
    job = TaskScheduler.get_job(task_id)
    if not job:
        raise HTTPException(status_code=404, detail="Task not found")
    job.start()
    return {"status": "started"}

@tasksrouter.post("/pause/{task_id}")
async def pause_task(task_id: str):
    job = TaskScheduler.get_job(task_id)
    if not job:
        raise HTTPException(status_code=404, detail="Task not found")
    job.pause()
    return {"status": "paused"}

@tasksrouter.post("/resume/{task_id}")
async def resume_task(task_id: str):
    job = TaskScheduler.get_job(task_id)
    if not job:
        raise HTTPException(status_code=404, detail="Task not found")
    job.resume()
    return {"status": "resumed"}

@tasksrouter.delete("/remove/{task_id}")
async def remove_task(task_id: str):
    job = TaskScheduler.get_job(task_id)
    if not job:
        raise HTTPException(status_code=404, detail="Task not found")
    TaskScheduler.remove_job(task_id)
    return {"status": "removed"}











