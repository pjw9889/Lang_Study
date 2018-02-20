area_dict = {}

with open("seoul.txt") as f:
    strs = f.read().split("\n")[:-1]

    for line in strs:
        items = line.split(",")
        data = [items[0], items[2]]

        if not (data[0] in area_dict):
            area_dict[data[0]] = []

        area_dict[data[0]].append(float(items[2]))
# check value // print(list(area_dict.keys()))
seoul = area_dict['108']

# histogram

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

labels = list(range(len(seoul)))

plt.plot(labels, seoul)

plt.savefig("./result_pic/seoul.png")
plt.close()
