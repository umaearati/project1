import yaml

def load_config(config_path:str = "/Users/nanimahi/project1/config/config.yaml") -> dict:
    """
    Load configuration from a YAML file.
    
    :param file_path: Path to the YAML configuration file.
    :return: Dictionary containing the configuration.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    print(config)
    return config

load_config("/Users/nanimahi/project1/config/config.yaml")