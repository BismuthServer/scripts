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

new_player = input("Enter new IGN: ")
old_player = input("Enter old IGN: ")

for score in filter(lambda x: x['Name'].value == old_player, scoreboards['PlayerScores']):
    smprcon.command(f"/scoreboard players set {new_player} {score['Objective'].value} {score['Score'].value}")

print("Check if the scores have transferred. If they have, then run '/scoreboard players reset " + old_player + "'")
