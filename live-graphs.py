"""Live Graphs"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')


def main():
  fig = plt.figure()
  ax1 = fig.add_subplot(1,1,1)
  def animate(i):
    x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
    ax1.clear()
    ax1.plot(x, y)
  ani = animation.FuncAnimation(fig, animate, interval=1000)
  plt.show()

if __name__ == '__main__':
  main()
