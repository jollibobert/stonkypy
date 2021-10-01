import os
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from yahoofinancials import YahooFinancials


def download_spd(asset, start_date='2021-01-01'):
    # download daily stock price data

    # download via YahooFinancials
    yfin = YahooFinancials(asset)
    info = yfin.get_stock_quote_type_data()
    asset_info = info[asset]
    date_today = datetime.today().strftime('%Y-%m-%d')
    data = yfin.get_historical_price_data(start_date=start_date, 
                                          end_date=date_today,
                                          time_interval='daily')

    # info
    addtl_info = {
        'firstTradeDate': data[asset]['firstTradeDate']['formatted_date'],
        'currency': data[asset]['currency'],
        'instrumentType': data[asset]['instrumentType']
    }
    asset_info.update(addtl_info)

    asset_info = pd.Series(asset_info)
    keep_keys = \
    ['symbol',
     'shortName',
     'market',
     'exchange',
     'exchangeTimezoneName',
     'exchangeTimezoneShortName'
     ]
    asset_info = asset_info[keep_keys + list(addtl_info.keys())]
    

    # price data
    spd = pd.DataFrame(data[asset]['prices'])
    spd = spd.drop('date', axis=1).set_index('formatted_date')
    
    return asset_info, spd


def plot_spd(asset_info, spd, normalize):
    # plot daily stock price data (adjusted closing prices)
    
    plt.figure(figsize=(12, 4))
    if normalize == False:
        plt.plot(spd['adjclose'], lw=2)
    else:
        plt.plot(spd['adjclose'] / spd['adjclose'].max() * 100, lw=2)

    plt.tick_params(axis='x',
                    which='both',
                    bottom=False,
                    top=False,
                    labelbottom=False)
    plt.title('{} | {}:{}'.format(asset_info['shortName'], 
                                  asset_info['exchange'], 
                                  asset_info['symbol']),
              weight='bold')
    if normalize == False:
        plt.ylabel(asset_info['currency'], weight='bold')
    else:
        plt.ylabel('% {}'.format(asset_info['currency']), weight='bold')
    
    plt.show()
    return


def stock_summary(asset, chart_only=False, normalize=False):
    # download daily stock price data, display information (optional)
    # and stock price chart

    asset_info, spd = download_spd(asset)

    if chart_only == False:
        print('\n\nDownloading stock price data for {}...\n'.format(asset))
        print('Asset Information:')
        display(asset_info)
        print('\nStock Price History:')
    
    plot_spd(asset_info, spd, normalize)

if __name__ == '__main__':
    print('Import this script as a module.')


