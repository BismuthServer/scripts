import mcrcon
from nbt import nbt
import json

with open("config.json") as f:
    cfg = json.load(f)

ip = cfg["server"]["ip"]
rcon_pass = cfg["server"]["rconpass"]
rcon_port = cfg["server"]["rconport"]

smprcon = mcrcon.MCRcon(ip, rcon_pass, rcon_port)
smprcon.connect()
scoreboards = nbt.NBTFile("/home/mc/bismuth/survival/server/bismuth_smp/data/scoreboard.dat")["data"]

new_player = input("Enter new IGN: ")
old_player = input("Enter old IGN: ")

for i in scoreboards["Objectives"]:
    smprcon.command("/scoreboard players operation " + new_player + " " + i["Name"].value + " += " + old_player + " " + i["Name"].value)

print("Check if the scores have transferred. If they have, then run '/scoreboard players reset " + old_player + "'")
