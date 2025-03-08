import re

url_pattern = re.compile(r'https?://\S+')

def has_url_in_message(message: str) -> bool:
    match = url_pattern.search(message)
    return match.group(0) if match else None
