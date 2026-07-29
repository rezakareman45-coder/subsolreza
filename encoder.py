import base64


def encode_subscription(configs):
    text = "\n".join(configs)

    encoded = base64.b64encode(
        text.encode("utf-8")
    ).decode("utf-8")

    return encoded