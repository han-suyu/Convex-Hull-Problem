import numpy as np
import random
import scipy.spatial as spt
import matplotlib.pyplot as plt
plt.rc('font', family='simhei', size=10)    # 设置中文显示，字体大小


points = np.random.randint(0, 50, (50, 2))
plt.scatter(x=points[:, 0], y=points[:, 1], marker='*', color='blue')

# 调用ConvexHull函数解决凸包问题
hull = spt.ConvexHull(points=points)


for sim in hull.simplices:
    plt.plot(points[sim, 0], points[sim, 1], 'red')   
    # 数组下标用逗号隔开表示行和列分开处理。（逗号的两边还可以各加冒号限定行或列的范围）
    # 比如points[sim, 0]就表示所有点中横坐标下标为sim（两行），纵坐标下标为0（1列）的值，这些值恰好是相邻两点的x坐标，两个值，再加上points[sim, 1]也是两个值，共4个值，满足plot的参数要求。
    # plot基本参数要求：plt.plot(点1横坐标, 点2横坐标,点1纵坐标，点2纵坐标， color='')  

    plt.title("最大凸多边形面积：{}".format(hull.area)) # 图形标题
 
plt.show()