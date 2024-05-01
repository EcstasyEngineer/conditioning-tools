from pyyaml import load, FullLoader

def load_config():
    with open("config/settings.yaml", "r") as file:
        return load(file, Loader=FullLoader)

settings = load_config()