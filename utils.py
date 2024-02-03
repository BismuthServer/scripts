import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from mcrcon import MCRcon


def backup_scoreboard(smprcon: MCRcon, world_path: Path, scoreboard_path: Path):
    smprcon.command("save-off")
    smprcon.command("save-all flush")

    wait_command = "inotifywait -m -r " + str(world_path) + " | grep -v ACCESS"
    subprocess.call(["waitsilence", "-timeout", "5s", "-command", wait_command])

    now = datetime.now()
    date_time = now.strftime("%m.%d.%Y.%H.%M")
    shutil.copy(scoreboard_path, scoreboard_path.parent / f"scoreboard.dat.{date_time}.bak")

    smprcon.command("save-on")
