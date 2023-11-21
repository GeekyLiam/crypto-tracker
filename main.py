import json
import requests
import time

def coin_price():
    
    # Currently supported coins: BTC, ETH
    coin_loop = True
    while coin_loop:
        coin = input.capitalize("Enter the coin ticker: \n")
        if coin == "BTC":
            print("Bitcoin selected.")
            coin_loop = False
        elif coin == "ETH":
            print("Ethereum selected.")
            coin_loop = False
        else:
            print("Coin not recognized. Please retry: \n")

    # Currently supported currencies: USD, GBP
    cur_loop = True
    while cur_loop:
        currency = input.capitalize("Enter the currency: \n")
        if currency == "USD":
            currency = "USDT"
            print("USD selected.")
            cur_loop = False
        elif currency == "GBP":
            print("GBP selected.")
            cur_loop = False
        else:
            print("Currency not recognized. Please retry: \n")

def menu():
    print("Welcome to CryptoTracker!")
    print("Please choose an option from the menu:")

    menu_loop = True

    while menu_loop:
        print("1. View Coin Price")
        print("2. Exit")

        choice = input("Enter your choice: \n")

        if choice == "1":
            coin_price()

        elif choice == "2":
            print("Exiting CryptoTracker...")
            time.sleep(1)
            quit()

def main():
    menu()

if __name__ == '__main__':
    main()