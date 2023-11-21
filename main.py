import json
import requests
import time
import os

def coin_cur_selection():
    """
    Function for coin/currency selection. 
    Returns tuple containing selected coin and currency.
    """
    
    # Currently supported coins: BTC, ETH
    coin_loop = True
    while coin_loop:
        coin = input("Enter the coin ticker: \n").upper()
        if coin == "BTC":
            print("Bitcoin selected.")
            time.sleep(0.2)
            coin_loop = False
        elif coin == "ETH":
            print("Ethereum selected.")
            time.sleep(0.2)
            coin_loop = False
        else:
            print("Coin not recognized. Please retry.")

    # Currently supported currencies: USD, GBP
    cur_loop = True
    while cur_loop:
        currency = input("Enter the currency: \n").upper()
        if currency == "USD":
            currency = "USDT"
            print("USD selected.")
            time.sleep(0.2)
            cur_loop = False
        elif currency == "GBP":
            print("GBP selected.")
            time.sleep(0.2)
            cur_loop = False
        else:
            print("Currency not recognized. Please retry.")

    coin_cur = (coin, currency)
    return coin_cur

def coin_price(coin, currency):
    """
    Function for fetching cryptocurrency price using the Binance API.
    """

    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}{currency}"
    data = requests.get(url)
    data = data.json()

    return data

def menu():
    print("Welcome to CryptoTracker!")
    print("Please choose an option from the menu:")

    menu_loop = True

    while menu_loop:
        print("\n1: View Coin Price.")
        print("c: Clear Terminal.")
        print("q: Exit")

        choice = input("Enter your choice: \n")

        if choice == "1":
            coin_cur = coin_cur_selection()
            coin_data = coin_price(coin_cur[0], coin_cur[1])
            if coin_data["symbol"] == "BTCUSDT":
                print(f"BTC/USD price is ${float(coin_data['price']):.2f}.")
            elif coin_data["symbol"] == "BTCGBP":
                print(f"BTC/GBP price is £{float(coin_data['price']):.2f}.")
            elif coin_data["symbol"] == "ETHUSDT":
                print(f"ETH/USD price is ${float(coin_data['price']):.2f}.")
            elif coin_data["symbol"] == "ETHGBP":
                print(f"ETH/GBP price is £{float(coin_data['price']):.2f}.")
                
        elif choice == "c" or choice =="C":
            print("Clearing terminal...")
            time.sleep(1)
            os.system('cls')
            print("Welcome to CryptoTracker!")
            print("Please choose an option from the menu:")

        elif choice == "q" or choice == "Q":
            print("Exiting CryptoTracker...")
            time.sleep(1)
            quit()

def main():
    menu()

if __name__ == '__main__':
    main()