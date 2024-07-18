import os
import requests
import json
import datetime
from dotenv import load_dotenv
from loguru import logger
from rich.logging import RichHandler
logger.configure(handlers=[{"sink":RichHandler(), "format":"{message}"}])

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

def emmit(state, title, message, timestamp):
    if not SLACK_WEBHOOK_URL:
        logger.error("[SLACK NOTIFIER] SLACK_WEBHOOK_URL is not set")
        return

    # State Color
    state_color = "#999999"
    if state == "good":
        state_color = "#00FF00"  # Assuming 'good' is green
    elif state == "warning":
        state_color = "#FFFF00"  # Assuming 'warning' is yellow
    elif state == "danger":
        state_color = "#FF0000"  # Assuming 'danger' is red
    elif state == "normal":
        state_color = "#FFFFFF"  # Assuming 'normal' is white

    post_data = {
        "color": state_color,
        "fields": [
            {
                "title": title,
                "value": message,
                "short": False
            }
        ],
    }

    # Add Timestamp
    if timestamp:
        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        now = datetime.datetime.now(JST)
        value = post_data["fields"][0]["title"]
        now_str = now.strftime('%Y/%m/%d %H:%M:%S')
        post_data["fields"][0]["title"] = f"{value} - {now_str}"

    if state == "warning":
      logger.warning(f"[SLACK NOTIFIER] Webhookurl {SLACK_WEBHOOK_URL}")
      logger.warning(f"[SLACK NOTIFIER] State : {state}")
      logger.warning(f"[SLACK NOTIFIER] Title : {title}")
      logger.warning(f"[SLACK NOTIFIER] Message : {message}")
      logger.warning(post_data)
    elif state == "danger":
      logger.error(f"[SLACK NOTIFIER] Webhookurl {SLACK_WEBHOOK_URL}")
      logger.error(f"[SLACK NOTIFIER] State : {state}")
      logger.error(f"[SLACK NOTIFIER] Title : {title}")
      logger.error(f"[SLACK NOTIFIER] Message : {message}")
      logger.error(post_data)
    else:
        logger.info(f"[SLACK NOTIFIER] Webhookurl {SLACK_WEBHOOK_URL}")
        logger.info(f"[SLACK NOTIFIER] State : {state}")
        logger.info(f"[SLACK NOTIFIER] Title : {title}")
        logger.info(f"[SLACK NOTIFIER] Message : {message}")
        logger.info(post_data)
        
    requests.post(SLACK_WEBHOOK_URL, data=json.dumps(post_data))

# Example usage
# emmit("good", "System Alert", "Everything is running smoothly.", True)