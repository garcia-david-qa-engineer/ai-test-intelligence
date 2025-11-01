import json

def clean_markdown(md: str) -> str:
    return md.strip()

def to_json_risk(raw: str) -> dict:
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"risks": []}
