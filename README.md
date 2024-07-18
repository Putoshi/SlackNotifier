# Slack Notifier

## 概要
`slack_notifier.py` は、特定の状態に基づいてSlackに通知を送るPythonスクリプトです。このスクリプトは、Webhookを通じてSlackのチャンネルにメッセージをポストします。

## 機能
- **カスタマイズ可能なメッセージ**: スクリプトは、タイトル、メッセージ本文、状態（good, warning, danger, normal）、およびタイムスタンプの有無をカスタマイズして送信できます。
- **状態に応じた色分け**: メッセージは、状態に応じて色分けされます（例: goodは緑、warningは黄色、dangerは赤）。
- **タイムスタンプの追加**: オプションで現在の日時をメッセージに追加できます。

## 使用方法
1. **Webhook URLの設定**: Slackから取得したWebhook URLをスクリプトに設定します。
2. **関数の呼び出し**: `emmit` 関数を呼び出し、適切なパラメータを渡してメッセージを送信します。

### 関数のシグネチャ
```python
emmit(state, title, message, timestamp)
```

### パラメータ
- `webhook_url`: SlackのWebhook URL。
- `state`: メッセージの状態（'good', 'warning', 'danger', 'normal'）。
- `title`: Slackに表示されるメッセージのタイトル。
- `message`: Slackに表示されるメッセージ本文。
- `timestamp`: メッセージに現在時刻を追加するかどうかのブール値。

## 例
```python
import slack_notifier

slack_notifier.emmit("good", "System Alert", "Everything is running smoothly.", True)
```

この例では、状態が 'good' で、タイトルが "System Alert"、メッセージが "Everything is running smoothly." の通知をSlackに送信し、現在の日時も追加されます。
