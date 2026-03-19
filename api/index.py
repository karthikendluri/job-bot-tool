from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Temporary in-memory database (Vercel resets this often)
# In production, you'd connect this to a Supabase or MongoDB URL
job_tracker = []

class JobApplication(BaseModel):
    title: str
    company: str
    url: str

@app.get("/api/jobs")
def get_jobs():
    return job_tracker

@app.post("/api/apply")
async def apply_to_job(job: JobApplication):
    # Logic to "Apply" would go here. 
    # NOTE: On Vercel, you would use a Webhook or a Remote Browser.
    
    new_entry = {
        "id": len(job_tracker) + 1,
        "title": job.title,
        "company": job.company,
        "url": job.url,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "✅ Applied"
    }
    job_tracker.append(new_entry)
    return {"message": "Job tracked successfully!", "job": new_entry}
