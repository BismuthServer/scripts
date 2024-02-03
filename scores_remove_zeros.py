import mcrcon
from nbt import nbt
import json
import os

with open("config.json") as f:
    cfg = json.load(f)

ip = cfg["server"]["ip"]
rcon_pass = cfg["server"]["rconpass"]
rcon_port = cfg["server"]["rconport"]

smprcon = mcrcon.MCRcon(ip, rcon_pass, rcon_port)
smprcon.connect()

world_path = cfg['server']['world']
scoreboards = nbt.NBTFile(os.path.join(world_path, 'data', 'scoreboard.dat'))['data']

for score in filter(lambda x: x['Score'].value == 0, scoreboards['PlayerScores']):
    smprcon.command(f"/scoreboard players reset {score['Name'].value} {score['Objective'].value}")
