import os


def save_subscription(configs, encoded):
    os.makedirs("output", exist_ok=True)

    txt_path = os.path.join("output", "sub.txt")
    b64_path = os.path.join("output", "sub_base64.txt")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(configs))

    with open(b64_path, "w", encoding="utf-8") as f:
        f.write(encoded)

    return txt_path, b64_path