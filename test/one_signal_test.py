import requests

url = "https://onesignal.com/api/v1/notifications"

payload = {
    # "included_segments": ["Subscribed Users"],
    # "included_segments": [
    #     ""
    # ],
    "include_external_user_ids": [
        '8'
    ],
    "app_id": "c028e613-8406-43a8-ba01-fbff5754aa95",
    "headings": {
        "ko": "새로운 메세지 제목",
        "en": "새로운 메세지 제목",
    },
    "contents": {
        "ko": "새로운 메세지 본문",
        "en": "새로운 메세지 본문",
    },
    "name": "INTERNAL_CAMPAIGN_NAME"
}
headers = {
    "accept": "application/json",
    "Authorization": 'Basic MzM5OTk3MjAtOTNkYi00ODRlLWE2YjctNDE0MDYzN2FmYzk5',
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

