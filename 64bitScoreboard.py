from nbt import nbt

# Load the scoreboard file
nbt_file = nbt.NBTFile("old_scoreboard.dat", "rb")

# For each player
for player in nbt_file["data"]["PlayerScores"]:
    player["Score"] = nbt.TAG_Long(player["Score"].value & 0xffffffff)

nbt_file.write_file("scoreboard.dat")
