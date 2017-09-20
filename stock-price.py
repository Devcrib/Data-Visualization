"""Stock Price"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def converter(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytes_converter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytes_converter

def load_data(stock_name):
    file = os.path.join('stock', stock_name)
    date, openp, highp, lowp, closep, volume, adj_close = np.loadtxt(file,
                                                                     skiprows=1,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: converter('%Y-%m-%d')})
    return [date, openp, highp, lowp, closep, volume, adj_close]

def main():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    date, openp, highp, lowp, closep, volume, adj_close = load_data('YAHOO-FB.csv')
    ax1.plot_date(date, closep, '-', linewidth=.5, label='Close price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    

if __name__ == '__main__':
    main()
