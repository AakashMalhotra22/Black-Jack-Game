from random import*
from colorama import*
from threading import*
from time import*
from datetime import*

class black_jack:
    def __init__(self):
        self.available_amount = None
        self.bidding_amount = None
        self.remaining_amount = None
        self.deck = []

    def opening(self):
            print(50 * "\n")
            print(Fore.RED, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to black jack game.")
            print(10 * "\n")

            print(Fore.GREEN, "")
            self.available_amount = 10000
            print(Fore.YELLOW, "You have 10,000 Rs available balance.")

            print(Fore.BLUE, "")
            self.inp1 = input("Press any key to continue: ")
            print(50 * "\n")

            print(Fore.YELLOW, "")
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

            inp2 = 1
            self.bidding_amount = None
            while inp2 == 1:
                try:
                    print(Fore.YELLOW + f"Available balance = {self.available_amount} Rs")
                    print(Fore.RED, "")
                    self.bidding_amount = int(input("How much do you want to bid: "))

                    inp2 = 0
                except:
                    print(Fore.BLUE, "Make sure you enter a number only.")
                    inp2 = 1

            if self.bidding_amount > self.available_amount:
                inp3 = None
                while inp3 == None or self.bidding_amount > self.available_amount:
                    print(Fore.MAGENTA, "The amount you entered is more than the balance amount: ")
                    try:

                        print(Fore.YELLOW + f"Available balance = {self.available_amount} Rs")
                        print(Fore.RED, "")
                        self.bidding_amount = int(input("How much do you want to bid: "))

                        inp3 = 2
                    except:

                        print(Fore.BLUE, "Make sure you enter a number only ")
                        inp2 = 1

    def show1(self):
        self.remaining_balance = self.available_amount - self.bidding_amount
        print(Fore.MAGENTA, "")
        print("                                        Total Balance         = 10,000 Rs")
        print("                                        Bid amount            = {:,} Rs".format(self.bidding_amount))
        print("                                        Remaining Balance     = {:,} Rs".format(self.remaining_balance))

        inp4 = input(Fore.YELLOW + "Press any key to continue: ")
        sleep(1)
        print(50 * "\n")

    def decks(self):

        cardfaces= [' A ',' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ','10 ',' J ',' Q ',' K ']
        suits = [' Heart ','Diamond', " Spade "," Club  "]
        x =0
        for i in suits:
            x+=1
            for j in cardfaces:
                if x <= 2:
                    self.deck.append([Fore.RED+j,Fore.RED+i])
                else:
                    self.deck.append([Fore.BLACK+j,Fore.BLACK+i])
        shuffle(self.deck)
        return self.deck

    def distribution(self):
        p =y1.decks()

        card_values= {Fore.RED+' A ':11,Fore.RED+' 1 ':1,Fore.RED+' 2 ':2,Fore.RED+' 3 ':3,Fore.RED+' 4 ':4,Fore.RED+' 5 ':5,Fore.RED+' 6 ':6,Fore.RED+' 7 ':7,Fore.RED+' 8 ':8,Fore.RED+' 9 ':9,
             Fore.RED+'10 ':10,Fore.RED+' J ':10,Fore.RED+' Q ':10,Fore.RED+' K ':10,Fore.BLACK+' A ':11,Fore.BLACK+' 1 ':1,Fore.BLACK+' 2 ':2,Fore.BLACK+' 3 ':3,Fore.BLACK+' 4 ':4,
             Fore.BLACK+' 5 ':5,Fore.BLACK+' 6 ':6,Fore.BLACK+' 7 ':7,Fore.BLACK+' 8 ':8,Fore.BLACK+' 9 ':9,Fore.BLACK+'10 ':10,Fore.BLACK+' J ':10,Fore.BLACK+' Q ':10,Fore.BLACK+' K ':10}

        y4 = (Fore.BLACK+"Hidden")
        c1 = (Fore.LIGHTCYAN_EX+"")


        for i in range(1):

            print(Fore.LIGHTCYAN_EX,"")
            print(' ____________','    ____________','                                          ____________','     ____________')
            print('|            |','  |            |','                                        |            |','   |            |')
            print('|            |','  |            |','                                        |            |','   |            |')
            print(f'|     {p[0][0]}{c1}    |','  |   '+y4+c1+'   |',f'                                        |    {p[1][0]}{c1}     |',f'   |    {p[2][0]}{c1}     |')
            print(f'|   {p[0][1]}{c1}  |','  |            |',f'                                        |  {p[1][1]}{c1}   |',f'   |  {p[2][1]}{c1}   |')
            print('|            |','  |            |','                                        |            |','   |            |')
            print('|____________|','  |____________|','                                        |____________|','   |____________|')
            print(Fore.YELLOW,'   Card 1',"          Card 2                                                  Card 1           Card 2  ")

            computer_total = card_values[p[0][0]]
            player_total = card_values[p[1][0]]+card_values[p[2][0]]
            if card_values[p[1][0]]==card_values[p[2][0]]:
                ask1 = input(Fore.YELLOW+"Do you want to split, (yes or no): ")
                while ask1 not in ['yes', "YES", "NO", 'no', "No", "Yes"]:
                    print(Fore.RED+"Please write yes or no")
                    ask1 = input(Fore.YELLOW+"Do you want to split, (yes or no): ")
                if ask1 in ['yes', "YES", "Yes"]:
                    self.split()
            print(Fore.MAGENTA,f"         Total = {card_values[p[0][0]]}                                                                Total = {card_values[p[1][0]]+card_values[p[2][0]]}                            ")
            print("")
            print(Fore.LIGHTGREEN_EX,"              Computer", end = "")

            print(Fore.LIGHTMAGENTA_EX,"                                                               Player            ")
            print()
            sleep(7)
            if player_total ==21:
                print(Fore.RED+"Black JACK!!!         Black JACK!!!         Black JACK!!!         Black JACK!!!         Black JACK!!!         Black JACK!!!         Black JACK!!!")
                print(Fore.YELLOW+"                            Congratulations!!!!!!!!!!!!!!!!"+Fore.BLUE+"   Player has WON    "+Fore.YELLOW+
                      " Congratulations!!!!!!!!!!!!!!!!")
                print(Fore.MAGENTA+"                                               You have won {:,} Rs.".format(1.5*self.bidding_amount))
                self.available_amount = self.remaining_balance+1.5*self.bidding_amount
                print("                                               Total Balance = {:,} Rs".format(self.available_amount))


            else:

                n20 = input(Fore.YELLOW+"\t\t\t\t\t\t\tDo you want to "+Fore.RED+" HIT, "+Fore.BLUE+" STAND "+Fore.YELLOW+" or "+Fore.MAGENTA+" SURRENDER"
                            + Fore.YELLOW+"\n\t\t\t\t\t\t Press ("+Fore.RED+"h for HIT"+Fore.YELLOW+','+Fore.BLUE+' s for STAND '+Fore.YELLOW+'and '+Fore.MAGENTA+'i for SURRENDER'+
                Fore.YELLOW+'): ')
    def split(self):
        pass
    def stand(self):
        pass
    def hit(self):
        pass
    def surrender(self):
        pass





y1 = black_jack()
y1.opening()
y1.show1()
y1.distribution()
