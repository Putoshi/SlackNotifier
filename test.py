# test.py
import slack_notifier
from slack_notifier import MessageState  # State Enumをインポート

slack_notifier.emit(MessageState.DANGER, "System Alert", "This is a test message", True)