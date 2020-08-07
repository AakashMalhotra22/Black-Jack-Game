from colorama import*
from cards_deck import cards


ob1 = cards()
p = ob1.decks()

card_values = {Fore.RED + ' A ': 11, Fore.RED + ' 1 ': 1, Fore.RED + ' 2 ': 2, Fore.RED + ' 3 ': 3,
                   Fore.RED + ' 4 ': 4, Fore.RED + ' 5 ': 5, Fore.RED + ' 6 ': 6, Fore.RED + ' 7 ': 7,
                   Fore.RED + ' 8 ': 8, Fore.RED + ' 9 ': 9,
                   Fore.RED + '10 ': 10, Fore.RED + ' J ': 10, Fore.RED + ' Q ': 10, Fore.RED + ' K ': 10,
                   Fore.BLACK + ' A ': 11, Fore.BLACK + ' 1 ': 1, Fore.BLACK + ' 2 ': 2, Fore.BLACK + ' 3 ': 3,
                   Fore.BLACK + ' 4 ': 4,
                   Fore.BLACK + ' 5 ': 5, Fore.BLACK + ' 6 ': 6, Fore.BLACK + ' 7 ': 7, Fore.BLACK + ' 8 ': 8,
                   Fore.BLACK + ' 9 ': 9, Fore.BLACK + '10 ': 10, Fore.BLACK + ' J ': 10, Fore.BLACK + ' Q ': 10,
                   Fore.BLACK + ' K ': 10}

y4 = (Fore.BLACK + "Hidden")
c1 = (Fore.LIGHTCYAN_EX + "")

def func():
            print(Fore.LIGHTCYAN_EX, "")
            com1 = ' ____________'
            com2 = '|            |'
            com3 = '|            |'
            com4 = f'|     {p[0][0]}{c1}    |'
            com5 = f'|   {p[0][1]}{c1}  |'
            com6 = '|            |'
            com7 = '|____________|'
            i = 0


            coadd1 = '    ____________'
            coadd2 = '  |            |'
            coadd3 = '  |            |'
            coadd4 = '  |     {}{}    |'
            coadd5 = '  |   {}{}  |'
            coadd6 = '  |            |'
            coadd7 = '  |____________|'



            y = 1
            while y == 1:
                i+=1
                com1 += coadd1
                com2 += coadd2
                com3 += coadd3
                com4 += coadd4.format(p[i][0],c1)
                com5 += coadd5.format(p[i][1],c1)
                com6 += coadd6
                com7 += coadd7
                print(com1)
                print(com2)
                print(com3)
                print(com4)
                print(com5)
                print(com6)
                print(com7)



                y = int(input("daal: "))

func()
'''
print(com1)
print(com2)
print(com3) 
print(com4)
print(com5)
print(com6)
print(com7)
'''