import requests
from config import OPENAI_API_KEY


class ChatService:
    def __init__(self):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }

    def get_alert_message(self, alert_text):
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": alert_text}
            ],
            "temperature": 0.7,
        }
        try:
            response = requests.post(
                self.url, headers=self.headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error calling ChatGPT API: {e}"
