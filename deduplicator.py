def remove_duplicates(configs):
    unique = []
    seen = set()

    for config in configs:
        if config not in seen:
            seen.add(config)
            unique.append(config)

    return unique