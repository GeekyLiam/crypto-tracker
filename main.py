import json
import requests
import time

def coin_price():
    
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

    cur_loop = True
    while cur_loop:
        currency = input.capitalize("Enter the currency: \n")
        if currency == USD:
            currency = "USDT"
            print("USD Selected.")

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