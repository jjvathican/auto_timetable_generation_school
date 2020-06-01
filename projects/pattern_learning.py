import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
#
# def data_gen(t=0):
#     cnt = 0
#     while cnt < 1000:
#         cnt += 1
#         t += 0.1
#         yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
#
#
# def init():
#     ax.set_ylim(-1.1, 1.1)
#     ax.set_xlim(0, 10)
#     del xdata[:]
#     del ydata[:]
#     line.set_data(xdata, ydata)
#     return line,
#
# fig, ax = plt.subplots()
# line, = ax.plot([], [], lw=2)
# ax.grid()
# xdata, ydata = [], []
#
#
# def run(data):
#     # update the data
#     t, y = data
#     xdata.append(t)
#     ydata.append(y)
#     xmin, xmax = ax.get_xlim()
#
#     if t >= xmax:
#         ax.set_xlim(xmin, 2*xmax)
#         ax.figure.canvas.draw()
#     line.set_data(xdata, ydata)
#
#     return line,
#
# ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=0,
#                               repeat=True, init_func=init)
# plt.show()
#




import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.dates import strpdate2num
import matplotlib.dates as mdates
import numpy as np
# from matplotlib import style
# style.use("ggplot")




def graphRawFX():
    c=str('GBPUSD1d.txt')
    date,bid,ask = np.loadtxt(c, unpack=True, delimiter=',',converters={0:mdates.bytespdate2num('%Y%m%d%H%M%S')})#,dtype={'names': ('gender', 'age', 'weight'),'formats': ('S1', 'i4', 'f4')})#converters = #{0:mdates.datestr2num('%w')}) #dtype=(float,int,int))#,converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
    print(date)
    fig=plt.figure(figsize=(10,7))

    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    plt.subplots_adjust(bottom=.23)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.grid(True)
    plt.show()
graphRawFX()


# from io import StringIO   # StringIO behaves like a file object
# c = StringIO("0 1\n2 3")
# f=np.loadtxt(c)
# print(f)
# array([[ 0.,  1.],[ 2.,  3.]])