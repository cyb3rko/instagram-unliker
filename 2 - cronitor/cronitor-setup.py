import cronitor

cronitor.api_key = "YOUR_API_KEY"
cronitor.Monitor.put(
    key="YOUR_JOB_NAME",
    type="job",
    schedule="0 */2 * * *"  # Or whatever interval you want (default: every 2 hours)
)
