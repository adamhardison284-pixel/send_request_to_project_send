import requests
import time
import os

URL = os.getenv("URL")

INTERVAL = 2
RUN_DURATION = 3600

WORKER_PREFIX = os.getenv("WORKER_ID", "worker")


def trigger_process_emails(worker_id):
    print('url', URL)
    try:
        response = requests.post(
            URL,
            json={
                "source": "github_cron",
                "cron_id": worker_id
            },
            timeout=30
        )
        print(worker_id, response.status_code)
        print(response.text)
        print("=====================================================================================")
    except Exception as e:
        print("Error:", e)


def main():
    inc = 0
    total_runs = RUN_DURATION // INTERVAL

    for _ in range(total_runs):
        inc += 1
        worker_id = f"{WORKER_PREFIX}_{inc}"
        trigger_process_emails(worker_id)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
