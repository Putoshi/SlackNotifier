import os
import requests
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from loguru import logger
from rich.logging import RichHandler
from enum import Enum

# 環境変数の読み込み
load_dotenv()

# ロガーの設定
logger.configure(handlers=[{"sink": RichHandler(), "format": "{message}"}])

# Slack Webhook URLの取得
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

class MessageState(Enum):
    GOOD = ("#00FF00", logger.info)
    WARNING = ("#FFFF00", logger.warning)
    DANGER = ("#FF0000", logger.error)
    NORMAL = ("#FFFFFF", logger.info)

def emit(state: MessageState, title: str, message: str, include_timestamp: bool = True):
    if not SLACK_WEBHOOK_URL:
        logger.error("[SLACK NOTIFIER] SLACK_WEBHOOK_URL is not set")
        return

    # メッセージに @channel を追加する条件を設定
    if state == MessageState.DANGER:
        message = "<!channel> " + message

    post_data = {
        "color": state.value[0],
        "fields": [
            {
                "title": title,
                "value": message,
                "short": False
            }
        ],
    }

    if include_timestamp:
        JST = timezone(timedelta(hours=9), 'JST')
        now = datetime.now(JST).strftime('%Y/%m/%d %H:%M:%S')
        post_data["fields"][0]["title"] = f"{title} - {now}"

    log_func = state.value[1]
    log_func(f"[SLACK NOTIFIER] State: {state.name}, Title: {title}, Message: {message}")

    response = requests.post(SLACK_WEBHOOK_URL, json=post_data)
    if response.status_code != 200:
        logger.error(f"Failed to send Slack notification. Status code: {response.status_code}")

# 使用例
# emit(MessageState.GOOD, "System Alert", "Everything is running smoothly.")