import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [2,3,4,5]

plt.plot(x,y)
plt.savefig("./result_pic/figname.png")
plt.close()

plt.scatter(x,y)
plt.savefig("./result_pic/scatter.png")
plt.close()

plt.hist(x)
plt.savefig("./result_pic/hist.png")
plt.close()

plt.boxplot(x)
plt.savefig("./result_pic/boxplot.png")
plt.close()

plt.bar(x,y)
plt.savefig("./result_pic/bar.png")
plt.close()
