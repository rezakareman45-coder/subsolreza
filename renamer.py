def rename_configs(configs):
    renamed = []

    for index, config in enumerate(configs, start=1):
        if "#" in config:
            config = config.split("#")[0]

        config += f"#reza{index}"

        renamed.append(config)

    return renamed