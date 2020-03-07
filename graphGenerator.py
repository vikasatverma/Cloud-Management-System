import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import thread
import main
import time


# This function is called periodically from FuncAnimation
def animate(i, xs, ys,ax):
    temp_c = next(main.statGenarator())

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%M:%S'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.axhline(50,color='r')
    plt.ylim(0,100)
    for i, j in zip(xs, ys):
        ax.annotate(str(j), xy=(i, j))
    plt.subplots_adjust(bottom=0.30)
    plt.title('vCPU Usage')
    plt.ylabel('Percentage Used')

def genGraph():
    # Set up plot to call animate() function periodically
    fig = plt.figure("vCPU Usage")
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys,ax), interval=1)
    plt.show()

genGraph()
