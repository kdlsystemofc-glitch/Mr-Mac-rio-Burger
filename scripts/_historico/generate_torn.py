import random

random.seed(42)

# Top torn paper: fill top (0,0) down to rip line
points_top = []
for x in range(0, 1441, 12):
    y = 16.0 + 5.0 * (x / 1440.0) + random.uniform(-4.0, 4.0)
    points_top.append(f"{x},{y:.1f}")

start_y = points_top[0].split(",")[1]
path_top = f"M0,0 L0,{start_y} " + " ".join(f"L{p}" for p in points_top) + " L1440,0 Z"

# Bottom torn paper: fill bottom (1440,40) up to rip line
points_bot = []
for x in range(0, 1441, 12):
    y = 20.0 + 4.0 * ((1440 - x) / 1440.0) + random.uniform(-4.0, 4.0)
    points_bot.append(f"{x},{y:.1f}")

bot_start_y = points_bot[0].split(",")[1]
path_bot = f"M0,40 L0,{bot_start_y} " + " ".join(f"L{p}" for p in points_bot) + " L1440,40 Z"

with open("scripts/torn_top.txt", "w") as f:
    f.write(path_top)

with open("scripts/torn_bot.txt", "w") as f:
    f.write(path_bot)

print("Generated torn paths!")
