import random

from encoder import encode_subscription
from deduplicator import remove_duplicates
from config import SUBSCRIPTIONS, LIMIT_PER_SUB
from renamer import rename_configs
from downloader import download_subscription
from parser_1 import parse_subscription
from writer import save_subscription

all_configs = []

print("شروع پروژه")

for index, url in enumerate(SUBSCRIPTIONS[:2], start=1):
    print(f"\nساب {index}")

    data = download_subscription(url)

    if data is None:
        print("دانلود نشد.")
        continue

    configs = parse_subscription(data)

    print(f"تعداد کل کانفیگ‌ها: {len(configs)}")

    selected = random.sample(
        configs,
        min(LIMIT_PER_SUB, len(configs))
    )

    print(f"انتخاب شد: {len(selected)} کانفیگ")

    all_configs.extend(selected)

before = len(all_configs)

all_configs = remove_duplicates(all_configs)

after = len(all_configs)

print(f"\nکانفیگ تکراری حذف شد: {before - after}")

all_configs = rename_configs(all_configs)
encoded = encode_subscription(all_configs)

txt_path, b64_path = save_subscription(
    all_configs,
    encoded
)

print(f"\nفایل متنی: {txt_path}")
print(f"فایل Base64: {b64_path}")

