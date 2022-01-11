import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


# 在（start,end)区间内，随机生成具有 n 个点的点集（return: list [(x1,y1)...(xn,yn)]）
def sample(n, start=0, end=101):
    return list(zip([random.randint(start, end) for _ in range(n)], [random.randint(start, end) for _ in range(n)]))
  




'''
# 计算两个向量之间的叉积。返回三点之间的关系：

<0，说明第三个点是向左转，则保留第二个点（栈顶元素）,再加入第三个点
>0，说明第三个点是向右转，则删除第二个点（栈顶元素）,再加入第三个点
=0，说明三点共线

'''       
def ccw(a, b, c):
    return ((b[1] - a[1]) * (c[0] - b[0]))   -    ((c[1] - b[1]) * (b[0] - a[0]) )






# 分别求出后面n-1个点与出发点的斜率，借助sorted完成从小到大排序
def compute(next):
    
    start = points[0]  # 第一个点

    # 按极角序排列的方法，但现在输入的坐标点是笛卡尔坐标点。不适合用这个
    # angle = math.atan2( start[2] - next[2], start[1] - next[1] )
    # return angle


    # 按斜率排列的方法
    if start[0] == next[0]:  # 如果x坐标相同，那么求斜率时会出现分母为0的情况,直接返回斜率无穷大
        return 99999
    slope = (start[1] - next[1]) / (start[0] - next[0])
   
    return slope










def Graham_Scan(points):

    # # 找到最左边且最下面的点作为出发点，和第一位互换
    Min=9999
    
    for i in range(len(points)):
        # 寻找最左边的点
        if points[i][0]<Min:
            Min = points[i][0]
            index = i
        # 如果同在最左边，可取y值更小的
        elif points[i][0]==Min:
            if points[i][1]<=points[index][1]:
                Min = points[i][0]
                index = i
    # 和第一位互换位置
    temp = points[0]
    points[0] = points[index]
    points[index] = temp


   

    # 排序：从第二个元素开始，按与第一个元素的斜率排序
    points = points[:1] + sorted(points[1:], key=compute)   # 前半部分是出发点  ；  后半部分是经过按斜率排序之后的n-1个坐标点     注意： “+”是拼接的含义，不是数值相加



    # 用列表模拟一个栈。（最先加入的是前两个点，前两次while必定不成立，从而将点加进去）
    convex_hull = []
    
    for p in points:
        
        '''
        # 如果能顺时针方向（右转）连接第三个顶点，就删除栈顶元素再加入这个顶点 ； 否则（向左转才达到第三个顶点），直接加入这个顶点  
        convex_hull[-2]：栈顶元素下面的元素
        convex_hull[-1]：栈顶元素
        p：要分析的第三个顶点

        '''
        while len(convex_hull) > 1 and ccw(convex_hull[-2], convex_hull[-1], p) >= 0:
            convex_hull.pop()
        convex_hull.append(p)

    return convex_hull



def show_result(points, results):
    """
    画图
    :param points: 所有点集
    :param results: 所有边集
    :return: picture
    """
    all_x = []
    all_y = []
    for item in points:
        a, b = item
        all_x.append(a)
        all_y.append(b)

    for i in range(len(results)-1):
        item_1=results[i]
        item_2 = results[i+1]
        #  横坐标,纵坐标
        one_, oneI = item_1
        two_, twoI = item_2
        plt.plot([one_, two_], [oneI, twoI])

    plt.scatter(all_x, all_y)
    plt.show()






if __name__ == '__main__':

    # points = [(101, 47), (32, 40), (21, 90), (65, 100), (98, 64), (81, 43), (51, 20), (75, 82), (90, 34), (38, 101)]
    points = sample(100)


    hull = Graham_Scan(points)  
    print(hull)



    # 可视化，有利于检查结果的正确性
    hull.append(hull[0])  # 把最后一个点和源点连起来，绘制成闭合连线（仅在画图时这样处理）
    show_result(points, hull)

    
