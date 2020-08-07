from random import*
from colorama import*
from threading import*
from time import*
from datetime import*

class BlackJack_opening():
    def __init__(self):



            print(50*"\n")
            print(Fore.RED, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to black jack game.")
            print(10*"\n")

            print(Fore.GREEN,"")
            self.available_amount = 10000
            print(Fore.YELLOW,"You have 10,000 Rs available balance.")

            print(Fore.BLUE,"")
            self.inp1 = input("Press any key to continue: ")
            print(50*"\n")

            print(Fore.YELLOW,"")
            print("Let's begin")
            print(3)
            sleep(0.5)
            print(2)
            sleep(0.5)
            print(1)
            sleep(0.5)
            print("Go")
            sleep(0.5)
            print("")

            inp2 =1
            self.bidding_amount = None
            while inp2 ==1:
                try:
                  print(Fore.YELLOW+f"Available balance = {self.available_amount} Rs")
                  print(Fore.RED, "")
                  self.bidding_amount = int(input("How much do you want to bid: "))

                  inp2 =0
                except:
                    print(Fore.BLUE,"Make sure you enter a number only.")
                    inp2 = 1

            if self.bidding_amount>self.available_amount:
                inp3 = None
                while inp3 ==None or self.bidding_amount > self.available_amount:
                        print(Fore.MAGENTA,"The amount you entered is more than the balance amount: ")
                        try:

                            print(Fore.YELLOW+f"Available balance = {self.available_amount} Rs")
                            print(Fore.RED, "")
                            self.bidding_amount = int(input("How much do you want to bid: "))

                            inp3 =2
                        except:

                            print(Fore.BLUE,"Make sure you enter a number only ")
                            inp2 = 1


    def show(self):
            self.remaining_balance = self.available_amount - self.bidding_amount
            print(Fore.MAGENTA,"")
            print("                                        Total Balance         = 10,000 Rs")
            print("                                        Bid amount            = {:,} Rs".format(self.bidding_amount))
            print("                                        Remaining Balance     = {:,} Rs".format(self.remaining_balance))


            n1 = input(Fore.YELLOW+"Press any key to continue: ")
            sleep(1)
            print(50*"\n")

if __name__ =="__main__":
    bjo = BlackJack_opening()
    bjo.show()