from colorama import*
from random import*
from cards_deck import cards
from blackjackopening import BlackJack_opening
from time import*
class distribution():
    def __init__(self):
        self.i=4

        ob1= cards()
        self.p = ob1.decks()
        p = self.p

        self.card_values= {Fore.RED+' A ':11,Fore.RED+' 1 ':1,Fore.RED+' 2 ':2,Fore.RED+' 3 ':3,Fore.RED+' 4 ':4,Fore.RED+' 5 ':5,Fore.RED+' 6 ':6,Fore.RED+' 7 ':7,Fore.RED+' 8 ':8,Fore.RED+' 9 ':9,
             Fore.RED+'10 ':10,Fore.RED+' J ':10,Fore.RED+' Q ':10,Fore.RED+' K ':10,Fore.BLACK+' A ':11,Fore.BLACK+' 1 ':1,Fore.BLACK+' 2 ':2,Fore.BLACK+' 3 ':3,Fore.BLACK+' 4 ':4,
             Fore.BLACK+' 5 ':5,Fore.BLACK+' 6 ':6,Fore.BLACK+' 7 ':7,Fore.BLACK+' 8 ':8,Fore.BLACK+' 9 ':9,Fore.BLACK+'10 ':10,Fore.BLACK+' J ':10,Fore.BLACK+' Q ':10,Fore.BLACK+' K ':10}
        card_values = self.card_values

        self.y4 = (Fore.BLACK+"Hidden")
        y4 = self.y4
        self.c1 = (Fore.LIGHTCYAN_EX+"")
        c1 =self.c1



        print(Fore.LIGHTCYAN_EX, "")
        self.com1 = 40*" "+' ____________'+            '    ____________'
        self.com2 = 40*" "+'|            |'+           '  |            |'
        self.com3 = 40*" "+'|            |'+           '  |            |'
        self.com4 = 40*" "+f'|     {p[0][0]}{c1}    |'+'  |   '+y4+c1+'   |'
        self.com5 = 40*" "+f'|   {p[0][1]}{c1}  |'+    '  |            |'
        self.com6 = 40*" "+'|            |'+           '  |            |'
        self.com7 = 40*" "+'|____________|'+           '  |____________|'
        self.com8 = 40*" "+Fore.YELLOW+ '    Card 1'+ "          Card 2"
        self.com9 = 40*" "+Fore.MAGENTA+ f"           Total = {card_values[p[0][0]]}"
        self.com10 = 40 * " " + Fore.LIGHTBLUE_EX + "             DEALER"


        self.pla1 = 40*" "+' ____________'+             '    ____________'
        self.pla2 = 40*" "+'|            |'+            '  |            |'
        self.pla3 = 40*" "+'|            |'+            '  |            |'
        self.pla4 = 40*" "+f'|     {p[2][0]}{c1}    |'+f'  |     {p[3][0]}{c1}    |'
        self.pla5 = 40*" "+f'|   {p[2][1]}{c1}  |'+    f'  |   {p[3][1]}{c1}  |'
        self.pla6 = 40*" "+'|            |'+            '  |            |'
        self.pla7 = 40*" "+'|____________|'+            '  |____________|'
        self.pla8 = 40*" "+Fore.YELLOW+ '    Card 1'+ "          Card 2"
        self.pla9 = 40*" "+Fore.MAGENTA+ f"           Total = {card_values[p[2][0]]+card_values[p[3][0]]}"
        self.pla10 = 40 * " " + Fore.LIGHTBLUE_EX + "             Player"

        print(self.com1)
        print(self.com2)
        print(self.com3)
        print(self.com4)
        print(self.com5)
        print(self.com6)
        print(self.com7)
        print(self.com8)
        print(self.com9)
        print(self.com10)
        print("\n")
        print(Fore.LIGHTCYAN_EX, "")
        print(self.pla1)
        print(self.pla2)
        print(self.pla3)
        print(self.pla4)
        print(self.pla5)
        print(self.pla6)
        print(self.pla7)
        print(self.pla8)
        print(self.pla9)
        print(self.pla10)

        # Moving further
        self.computer_total = card_values[p[0][0]]
        self.player_total = card_values[p[2][0]] + card_values[p[3][0]]
        player_total = self.player_total
        print()
        if player_total == 21:
            print(Fore.RED + "\tBlack JACK!!!         Black JACK!!!         Black JACK!!!         Black JACK!!!         Black JACK!!!         Black JACK!!!         Black JACK!!!")
            print(Fore.YELLOW + "                            Congratulations!!!!!!!!!!!!!!!!" + Fore.BLUE + "   Player has WON    " + Fore.YELLOW +
                " Congratulations!!!!!!!!!!!!!!!!")

        else:

            self.n20 = input(
                Fore.YELLOW + "\t\t\t\t\t\t\t\t\t\tDo you want to " + Fore.RED + " HIT, " + Fore.BLUE + " STAND " + Fore.YELLOW + " or " + Fore.MAGENTA + " SURRENDER"
                + Fore.YELLOW + "\n\t\t\t\t\t\t\t\t\t Press (" + Fore.RED + "h for HIT" + Fore.YELLOW + ',' + Fore.BLUE + ' s for STAND ' + Fore.YELLOW + 'and ' + Fore.MAGENTA + 'i for SURRENDER' +
                Fore.YELLOW + '):')
            while self.n20 not in "sSiIhH":
                print("Enter valid input...")
                self.n20 = input(
                    Fore.YELLOW + "\t\t\t\t\t\t\t\t\t\tDo you want to " + Fore.RED + " HIT, " + Fore.BLUE + " STAND " + Fore.YELLOW + " or " + Fore.MAGENTA + " SURRENDER"
                    + Fore.YELLOW + "\n\t\t\t\t\t\t\t\t\t Press (" + Fore.RED + "h for HIT" + Fore.YELLOW + ',' + Fore.BLUE + ' s for STAND ' + Fore.YELLOW + 'and ' + Fore.MAGENTA + 'i for SURRENDER' +
                    Fore.YELLOW + '):')
            if self.n20 in ['s','S']:
                self.stand()


            elif self.n20 in ["h","H"]:
                self.hit()
            elif self.n20 in ["i","I"]:
                self.surrender()
            else:
                pass



    def hit(self):

        plaadd1 = '    ____________'
        plaadd2 = '  |            |'
        plaadd3 = '  |            |'
        plaadd4 = '  |     {}{}    |'
        pladd5 = '  |   {}{}  |'
        plaadd6 = '  |            |'
        plaadd7 = '  |____________|'

        self.n20 ='h'
        while self.n20 in"hH":

            if self.p[self.i][0] in [Fore.RED+" A ", Fore.BLACK+" A "]:
                if self.player_total+11>21:
                    self.card_values[self.p[self.i][0]]=1

            self.player_total += self.card_values[self.p[self.i][0]]
            self.plaadd9 = 40 * " " + Fore.MAGENTA + "           {}Total = {}".format((self.i - 3) * 10 * ' ', self.player_total)
            print(50*"\n")
            self.pla1 += plaadd1
            self.pla2 += plaadd2
            self.pla3 += plaadd3
            self.pla4 += plaadd4.format(self.p[self.i][0], self.c1)
            self.pla5 += pladd5.format(self.p[self.i][1], self.c1)
            self.pla6 += plaadd6
            self.pla7 += plaadd7
            self.pla8+="          Card {}".format(self.i-1)
            self.pla9 =self.plaadd9
            self.pla10="          "+self.pla10

            print(Fore.LIGHTCYAN_EX, "")
            print(self.com1)
            print(self.com2)
            print(self.com3)
            print(self.com4)
            print(self.com5)
            print(self.com6)
            print(self.com7)
            print(self.com8)
            print(self.com9)
            print(self.com10)
            print("\n")
            print(Fore.LIGHTCYAN_EX, "")
            print(self.pla1)
            print(self.pla2)
            print(self.pla3)
            print(self.pla4)
            print(self.pla5)
            print(self.pla6)
            print(self.pla7)
            print(self.pla8)
            print(self.pla9)
            print(self.pla10)
            self.i += 1
            if self.player_total >21:
                print()
                print(Fore.RED+ "\t\t\t\t\tBURST!!!         BURST!!!         BURST!!!         BURST!!!         BURST!!!         BURST!!!         BURST!!!")
                print(Fore.BLUE+"\t\t\t\t\t                                              !!!PLAYER LOST!!!                                           ")
                break
            elif self.player_total ==21:
                sleep(5)

                self.stand()
                break


            self.n20 = input(
                Fore.YELLOW + f"\t\t\t\t\t\t\t\t\t\t{8*' '}Do you want to " + Fore.RED + " HIT "+ Fore.YELLOW + " or " + Fore.BLUE + " STAND "
                + Fore.YELLOW + f"\n\t\t\t\t\t\t\t\t\t{8*' '}   Press (" + Fore.RED + "h for HIT" + Fore.YELLOW +  Fore.YELLOW + ' and ' +  Fore.BLUE + ' s for STAND '
                + Fore.YELLOW + '):')
            while self.n20 not in "shSH":
                print("Invalid input...")
                self.n20 = input(
                    Fore.YELLOW + f"\t\t\t\t\t\t\t\t\t\t{8 * ' '}Do you want to " + Fore.RED + " HIT " + Fore.YELLOW + " or " + Fore.BLUE + " STAND "
                    + Fore.YELLOW + f"\n\t\t\t\t\t\t\t\t\t{8 * ' '}   Press (" + Fore.RED + "h for HIT" + Fore.YELLOW + Fore.YELLOW + ' and ' + Fore.BLUE + ' s for STAND '
                    + Fore.YELLOW + '):')
            if self.n20 in"sS":
                self.stand()


    def split(self):
                pass

    def stand(self):
        self.card_values= {Fore.RED+' A ':11,Fore.RED+' 1 ':1,Fore.RED+' 2 ':2,Fore.RED+' 3 ':3,Fore.RED+' 4 ':4,Fore.RED+' 5 ':5,Fore.RED+' 6 ':6,Fore.RED+' 7 ':7,Fore.RED+' 8 ':8,Fore.RED+' 9 ':9,
             Fore.RED+'10 ':10,Fore.RED+' J ':10,Fore.RED+' Q ':10,Fore.RED+' K ':10,Fore.BLACK+' A ':11,Fore.BLACK+' 1 ':1,Fore.BLACK+' 2 ':2,Fore.BLACK+' 3 ':3,Fore.BLACK+' 4 ':4,
             Fore.BLACK+' 5 ':5,Fore.BLACK+' 6 ':6,Fore.BLACK+' 7 ':7,Fore.BLACK+' 8 ':8,Fore.BLACK+' 9 ':9,Fore.BLACK+'10 ':10,Fore.BLACK+' J ':10,Fore.BLACK+' Q ':10,Fore.BLACK+' K ':10}

        num = 3
        print(50*"\n")
        self.com4 = 40 * " " + f'|     {self.p[0][0]}{self.c1}    |' + f'  |     {self.p[1][0]}{self.c1}    |'
        self.com5 = 40 * " " + f'|   {self.p[0][1]}{self.c1}  |' + f'  |   {self.p[0][1]}{self.c1}  |'
        self.com9 = 40*" "+Fore.MAGENTA+ f"           Total = {self.card_values[self.p[0][0]]+self.card_values[self.p[1][0]]}"
        self.computer_total = self.card_values[self.p[0][0]]+self.card_values[self.p[1][0]]
        print(Fore.BLUE+"The second hidden card of the dealer is...")
        print(Fore.LIGHTCYAN_EX, "")
        print(self.com1)
        print(self.com2)
        print(self.com3)
        print(self.com4)
        print(self.com5)
        print(self.com6)
        print(self.com7)
        print(self.com8)
        print(self.com9)
        print(self.com10)
        if self.computer_total > 16 and self.computer_total < self.player_total and self.computer_total <= 21:
            print()
            print(Fore.RED + "\t\t\t\t\tDEALER LOST!!!         DEALER LOST!!!         DEALER LOST!!!         DEALER LOST!!!        DEALER LOST!!!")
            print(
                Fore.BLUE + "\t\t\t\t\t                                              !!!PLAYER WON!!!                                           ")

        elif self.computer_total == self.player_total and self.computer_total <= 21:
            print()
            print(Fore.RED + "\t\t\t\t\tPUSH!!!         PUSH!!!         PUSH!!!         PUSH!!!        PUSH!!!        PUSH!!!        PUSH!!!        PUSH!!!")
            print(
                Fore.BLUE + "\t\t\t\t\t                                              !!!MATCH DRAW!!!                                           ")

        elif self.computer_total > self.player_total and self.computer_total <= 21:
            print()
            print(Fore.RED + "\t\t\t\t\tDEALER WON!!!         DEALER WON!!!         DEALER WON!!!         DEALER WON!!!        DEALER WON!!!")
            print(Fore.BLUE + "\t\t\t\t\t                                              !!!PLAYER LOST!!!                                           ")


        print("\n")
        print(Fore.LIGHTCYAN_EX, "")
        print(self.pla1)
        print(self.pla2)
        print(self.pla3)
        print(self.pla4)
        print(self.pla5)
        print(self.pla6)
        print(self.pla7)
        print(self.pla8)
        print(self.pla9)
        print(self.pla10)

        coadd1 = '    ____________'
        coadd2 = '  |            |'
        coadd3 = '  |            |'
        coadd4 = '  |     {}{}    |'
        coadd5 = '  |   {}{}  |'
        coadd6 = '  |            |'
        coadd7 = '  |____________|'

        if self.computer_total<self.player_total and self.computer_total<16:
            sleep(4)
            print(50 * "\n")

            y=1
            while y==1:
                if self.p[self.i][0] in [Fore.RED + " A ", Fore.BLACK + " A "]:
                    if self.computer_total + 11 > 21:
                        self.card_values[self.p[self.i][0]] = 1

                self.computer_total += self.card_values[self.p[self.i][0]]
                coadd9 =40 * " " + Fore.MAGENTA + "           {}Total = {}".format((num-2) * 10 * ' ', self.computer_total)


                print(Fore.LIGHTCYAN_EX, "")
                self.com1 += coadd1
                self.com2 += coadd2
                self.com3 += coadd3
                self.com4 += coadd4.format(self.p[self.i][0], self.c1)
                self.com5 += coadd5.format(self.p[self.i][1], self.c1)
                self.com6 += coadd6
                self.com7 += coadd7
                self.com8 += "          Card {}".format(num)
                self.com9 = coadd9
                self.com10 = "          " + self.com10
                print(self.com1)
                print(self.com2)
                print(self.com3)
                print(self.com4)
                print(self.com5)
                print(self.com6)
                print(self.com7)
                print(self.com8)
                print(self.com9)
                print(self.com10)
                if self.computer_total>21:
                    print()
                    print(Fore.RED + "\t\t\t\t\tDEALER BURST!!!         DEALER BURST!!!         DEALER BURST!!!         DEALER BURST!!!        DEALER BURST!!!")
                    print(Fore.BLUE + "\t\t\t\t\t                                              !!!PLAYER WON!!!                                           ")
                    y=2
                elif self.computer_total>16 and self.computer_total<self.player_total and self.computer_total<=21:
                    print()
                    print(Fore.RED + "\t\t\t\t\tDEALER LOST!!!         DEALER LOST!!!         DEALER LOST!!!         DEALER LOST!!!        DEALER LOST!!!")
                    print(Fore.BLUE + "\t\t\t\t\t                                              !!!PLAYER WON!!!                                           ")
                    y = 2
                elif self.computer_total == self.player_total and self.computer_total<=21:
                    print()
                    print(Fore.RED + "\t\t\t\t\tPUSH!!!         PUSH!!!         PUSH!!!         PUSH!!!        PUSH!!!        PUSH!!!        PUSH!!!        PUSH!!!")
                    print(Fore.BLUE + "\t\t\t\t\t                                              !!!MATCH DRAW!!!                                           ")
                    y = 2
                elif self.computer_total>self.player_total and self.computer_total<=21:
                    print()
                    print(Fore.RED + "\t\t\t\t\tDEALER WON!!!         DEALER WON!!!         DEALER WON!!!         DEALER WON!!!        DEALER WON!!!")
                    print(Fore.BLUE + "\t\t\t\t\t                                              !!!PLAYER LOST!!!                                           ")
                    y=2

                print("\n")
                print(Fore.LIGHTCYAN_EX, "")
                print(self.pla1)
                print(self.pla2)
                print(self.pla3)
                print(self.pla4)
                print(self.pla5)
                print(self.pla6)
                print(self.pla7)
                print(self.pla8)
                print(self.pla9)
                print(self.pla10)
                self.i += 1
                num+=1


    def surrender(self):
                    print()
                    print(Fore.LIGHTRED_EX+"     SURRENDERED!!!         SURRENDERED!!!         SURRENDERED!!!         SURRENDERED!!!         SURRENDERED!!!         SURRENDERED!!!")
                    print(Fore.BLUE+"                                     ...You have got 50 percent of the bid amount back in your account...")




















y = distribution()

'''
        print(com1)
        print(com2)
        print(com3)
        print(com4)
        print(com5)
        print(com6)
        print(com7)
        print(com8)
        print(com9)
        print(com10)



'''