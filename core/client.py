import requests

class WorkdayClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        })

    def post(self, path: str, json: dict):
        url = f"{self.base_url}{path}"
        resp = self.session.post(url, json=json, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def get(self, path: str, params: dict | None = None):
        url = f"{self.base_url}{path}"
        resp = self.session.get(url, params=params or {}, timeout=30)
        resp.raise_for_status()
        return resp.json()
