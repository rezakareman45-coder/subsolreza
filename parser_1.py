import base64


def parse_subscription(text):
    try:
        decoded = base64.b64decode(text).decode("utf-8")
    except Exception:
        decoded = text

    configs = []

    for line in decoded.splitlines():
        line = line.strip()

        if line:
            configs.append(line)

    return configs