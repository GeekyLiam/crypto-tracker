import json
import requests
import time

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
            coin_loop = False
        elif coin == "ETH":
            print("Ethereum selected.")
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
            cur_loop = False
        elif currency == "GBP":
            print("GBP selected.")
            cur_loop = False
        else:
            print("Currency not recognized. Please retry.")

    coin_cur = (coin, currency)
    return coin_cur

def coin_price():
    pass

def menu():
    print("Welcome to CryptoTracker!")
    print("Please choose an option from the menu:")

    menu_loop = True

    while menu_loop:
        print("1. View Coin Price")
        print("2. Exit")

        choice = input("Enter your choice: \n")

        if choice == "1":
            coin_cur = coin_cur_selection()
            coin_price(coin_cur)

        elif choice == "2":
            print("Exiting CryptoTracker...")
            time.sleep(1)
            quit()

def main():
    menu()

if __name__ == '__main__':
    main()