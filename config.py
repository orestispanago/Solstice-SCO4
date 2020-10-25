import yaml
from box import Box


with open("configs/trace.yaml", "r") as ymlfile:
    trace = Box(yaml.safe_load(ymlfile))

with open("configs/geometry.yaml", "r") as ymlfile:
    geom = Box(yaml.safe_load(ymlfile))
