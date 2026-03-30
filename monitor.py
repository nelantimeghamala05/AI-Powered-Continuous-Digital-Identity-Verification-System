from apscheduler.schedulers.background import BackgroundScheduler
from services.verify_service import verify_user

scheduler = BackgroundScheduler()
job = None

def start_monitoring(user_id):
    global job

    if not scheduler.running:
        scheduler.start()

    if job is None:
        job = scheduler.add_job(
            lambda: verify_user(user_id),
            trigger="interval",
            seconds=5
        )
        print("Monitoring started...")

def stop_monitoring():
    global job

    if job:
        job.remove()
        job = None
        print("Monitoring stopped.")