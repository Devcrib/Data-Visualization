"""Loaded from file"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
