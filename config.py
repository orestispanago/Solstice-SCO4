import yaml
from box import Box
import os

solstice_path = os.path.join(os.getcwd(), "solstice")
os.environ["LD_LIBRARY_PATH"] = os.path.join(solstice_path, "lib:")
os.environ["MANPATH"] = os.path.join(solstice_path, 'share', 'man:')
os.environ["PATH"] += f':{solstice_path}/bin:'

with open("configs/trace.yaml", "r") as ymlfile:
    trace = Box(yaml.safe_load(ymlfile))

with open("configs/geometry.yaml", "r") as ymlfile:
    geom = Box(yaml.safe_load(ymlfile))
