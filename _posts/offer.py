import numpy as np 
import matplotlib.pyplot as plt 

def drawcount():
    plt.rcParams['font.sans-serif']=['WenQuanYi'] #用来正常显示中文标签 
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    
    # company = ['bytedance', 'meituan', 'baidu', 'NetEase', 'honor', 'alibaba', 'huawei', 'tencent music', 'lazada', 'bilibili', 'duxiaoman']
    month = ['July', 'August', 'September', 'October', 'November']
    company = month
    # data = [11, 4, 3, 3, 2, 1, 3, 2, 1, 1, 2]
    # data = [4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    data = [1, 3, 9, 19, 1]
    data = np.array(data)

    plt.barh(np.arange(data.size), data) #, label='interview nums')
    # plt.xticks(np.arange(0, 12, 1), fontsize=10)
    plt.xticks(np.arange(0, 20, 2), fontsize=10)
    plt.yticks(np.arange(len(data)), company, fontsize=10)
    plt.xlabel('number of interviews', fontsize=20)
    # plt.xlabel('number of process', fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend()
    plt.show()


def drawcountpie():
    # month = ['July', 'August', 'September', 'October', 'November']
    # labels = month
    company = ['bytedance', 'meituan', 'baidu', 'NetEase', 'honor', 'alibaba', 'huawei', 'tencent music', 'lazada', 'bilibili', 'duxiaoman']
    labels = company
    # data = [1, 3, 9, 19, 1]
    data = [11, 4, 3, 3, 2, 1, 3, 2, 1, 1, 2]
    x = data
    #0.1表示将B那一块凸显出来
    # explode = (0,0, 0, 0.1,0) 
    explode = (0.1,0, 0,0,0,0,0,0,0, 0,0) 
    # 绘制饼图,autopct='%.0f%%' 显示百分比
    # textprops = {'fontsize':30, 'color':'k'} 大小为30，颜色为黑色
    # explode=explode 将B那一块凸显出来
    # shadow=True 显示阴影
    #startangle，起始角度，0，表示从0开始逆时针转，为第一块。选择从60度开始
    #pctdistance，百分比的文本离圆心的距离为0.5
    plt.pie(x,labels=labels,autopct='%.0f%%', textprops = {'fontsize':15, 'color':'k'},
            explode=explode,shadow=True,startangle=60,pctdistance = 0.5)
    
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    # drawcount() 
    drawcountpie() 
