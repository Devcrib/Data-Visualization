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

def load_data(stock_file):
    file = os.path.join(stock_file)
    date, openp, highp, lowp, closep, volume, adj_close = np.loadtxt(file,
                                                                     skiprows=1,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: converter('%Y-%m-%d')})
    return [date, openp, highp, lowp, closep, volume, adj_close]

def main():
    stock_data = 'YAHOO-FB'
    stock_file = os.path.join('stock', '{}.csv'.format(stock_data))
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    date, openp, highp, lowp, closep, volume, adj_close = load_data(stock_file)
    midprice_index = int(len(closep)/2)
    ax1.plot_date(date, closep, '-', linewidth=.5, label='Close price')
    ax1.fill_between(date, closep, closep[midprice_index], where=(closep > closep[midprice_index]), color='g', label='Profit', alpha=0.3)
    ax1.fill_between(date, closep, closep[midprice_index], where=(closep < closep[midprice_index]), color='r', label='Loss', alpha=0.3)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.title(stock_data)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc=4)
    plt.subplots_adjust(left=0.12, bottom=0.20, right=0.90, top=0.88, wspace=0.20, hspace=0.20)
    plt.show()
    

if __name__ == '__main__':
    main()
