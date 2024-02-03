import json
from pathlib import Path

import mcrcon
from nbt import nbt
from tqdm import tqdm

from utils import backup_scoreboard

with open("config.json") as f:
    cfg = json.load(f)

ip = cfg["server"]["ip"]
rcon_pass = cfg["server"]["rconpass"]
rcon_port = cfg["server"]["rconport"]
world_path = Path(cfg['server']['world'])

scoreboard_path = world_path / 'data' / 'scoreboard.dat'

smprcon = mcrcon.MCRcon(ip, rcon_pass, rcon_port)


def remove_zero_scores():
    scoreboards = nbt.NBTFile(scoreboard_path)['data']

    for score in tqdm(filter(lambda x: x['Score'].value == 0, scoreboards['PlayerScores'])):
        smprcon.command(f"/scoreboard players reset {score['Name'].value} {score['Objective'].value}")


if __name__ == "__main__":
    smprcon.connect()

    backup_scoreboard(smprcon, world_path, scoreboard_path)
    remove_zero_scores()

    smprcon.disconnect()
