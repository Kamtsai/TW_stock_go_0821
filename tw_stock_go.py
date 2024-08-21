import twstock
import pandas as pd
import os
from datetime import datetime

def ensure_data_dir():
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Created 'data' directory.")

def scrape_stock(stock_code):
    ensure_data_dir()
    stock = twstock.Stock(stock_code)
    target_price = stock.fetch_from(2020, 5)

    name_attribute = [
        'Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change',
        'Transaction'
    ]

    df = pd.DataFrame(columns=name_attribute, data=target_price)
    
    filename = f'data/{stock_code}.csv'
    df.to_csv(filename, index=False)
    print(f"Data for stock {stock_code} has been saved to {filename}")

def update_last_updated():
    ensure_data_dir()
    with open('data/last_updated.txt', 'w') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Updated last_updated.txt")

if __name__ == "__main__":
    stocks = ['0050', '2330', '2317']  # 您可以添加更多股票代碼
    for stock in stocks:
        scrape_stock(stock)
    update_last_updated()
    
    print("Script execution completed. Check the 'data' directory for output files.")
