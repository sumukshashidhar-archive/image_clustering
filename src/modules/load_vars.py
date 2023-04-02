def load_env_file(filepath):
    """
    Load variables from an env file into a dictionary.
    """
    env_vars = {}
    with open(filepath) as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env_vars[key] = value.strip('"')
    return env_vars

