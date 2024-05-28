from typing import Any, Dict
import requests


def call_api(input_json: Dict[str, Any]) -> Dict[str, Any]:
    path = input_json.pop("path")
    response = requests.get(f"https://algorithma.ruvnet.repl.co/random/{path}", params=input_json)

    if response.status_code == 200:
        return response.text
    else:
        return {"status_code": response.status_code, "text": response.text}
