#Bienvenido a mi proyecto Blitz Tally. Este programa te permitira llevar el puntaje de tu juego para no tener que hacer matematicas aburridas o distraerse por intentar llevar el total de cada jugador. El programa te permite escoger la cantidad de jugadores. Los nombres de cada jugador se ingresaran al comienzo de la partida y se almacenaran para poder tener una interfaz personalizada para cada jugador. El programa es capaz de almacenar y sumar los resultados de cada partida y de cada jugador hasta que alguien supere el total de 75 puntos. Si dos o mas jugadores llegan a 75 puntos en la misma partida. EL jugador con el puntaje mas alto sera el ganador. Espero les guste y se diviertan. 
            #codebycc
def run():


    print("""\n\n\n Welcome to Blitz Tally, 
    Rules are pretty straight forward.

    After the first round. 
    Please type the total amount of cards remaining on your Blitz Pile and the total of cards from the Dutch Piles. 
    
    Remember, first player to reach 75 points is the WINNER!!!
    Start playing, you will get it with time!

 
    """)
    amount_players =  int(input("Please choose the amount of players: "))

#2 players. 

    if amount_players == 2:
        player_2_1 = input("Player 1 name: ")
        player_2_2 = input("Player 2 name: ")

#round 1
        blitz_2_1 = input( player_2_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_2_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_2_1 = int(blitz_2_1 )
        dutch_2_1 = int(dutch_2_1 )
        total_2_1 = dutch_2_1  - (blitz_2_1  * 2)
        print("Your total is: " + str(total_2_1) + "\n")
        total_p1_round1 = total_2_1
        #if total_p1_round1 >= 75:
            #print( player_2_1 + " is the winner!!!" + "(" + str(total_p1_round1) + ")")
            
        blitz_2_2 = input( player_2_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_2_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_2_2 = int(blitz_2_2 )
        dutch_2_2 = int(dutch_2_2 )
        total_2_2 = dutch_2_2  - (blitz_2_2  * 2)
        print("Your total is: " + str(total_2_2) + "\n")
        total_p2_round1 = total_2_2
        #if total_p2_round1 >= 75:
            #print( player_2_2 + " is the winner!!!" + "(" + str(total_p2_round1) + ")")
            
        
        if total_p1_round1 >= 75 and total_p1_round1 > total_p2_round1:
            print( player_2_1 + " is the winner!!!!")
            exit()
        if total_p2_round1 >= 75 and total_p2_round1 > total_p1_round1:
            print( player_2_2 + " is the winner!!!!")
            exit()


#final round 1

#round2
        blitz_2_1 = input( player_2_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_2_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_2_1 = int(blitz_2_1 )
        dutch_2_1 = int(dutch_2_1 )
        total_2_1 = dutch_2_1  - (blitz_2_1  * 2)
        print("Your total is: " + str(total_2_1))
        total_p1_round2 = total_2_1
        suma_p1_rounds12 = total_p1_round1 + total_p1_round2
        print( player_2_1 + ", your current score is: " + str(suma_p1_rounds12) + "\n")
        # if suma_p1_rounds12 >= 75:
        #     print( player_2_1 + " is the winner!!!" + "(" + str(suma_p1_rounds12) + ")")
        #     exit()

        blitz_2_2 = input( player_2_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_2_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_2_2 = int(blitz_2_2 )
        dutch_2_2 = int(dutch_2_2 )
        total_2_2 = dutch_2_2  - (blitz_2_2  * 2)
        print("Your total is: " + str(total_2_2))
        total_p2_round2 = total_2_2
        suma_p2_rounds12 = total_p2_round1 + total_p2_round2
        print( player_2_2 + ", your current score is: " + str(suma_p2_rounds12) + "\n")
        # if suma_p2_rounds12 >= 75:
        #     print( player_2_2 + " is the winner!!!" + "(" + str(suma_p2_rounds12) + ")")
        #     exit()


        if suma_p1_rounds12 >= 75 and suma_p1_rounds12 > suma_p2_rounds12:
            print( player_2_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds12 >= 75 and suma_p2_rounds12 > suma_p1_rounds12:
            print( player_2_2 + " is the winner!!!!")
            exit()  


#final round 2   

# round 3  
        blitz_2_1 = input( player_2_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_2_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_2_1 = int(blitz_2_1 )
        dutch_2_1 = int(dutch_2_1 )
        total_2_1 = dutch_2_1  - (blitz_2_1  * 2)
        print("Your total is: " + str(total_2_1))
        total_p1_round3 = total_2_1
        suma_p1_rounds123 = total_p1_round1 + total_p1_round2 + total_p1_round3
        print( player_2_1 + ", your current score is: " + str(suma_p1_rounds123) + "\n")
        # if suma_p1_rounds123 >= 75:
        #     print( player_2_1 + " is the winner!!!" + "(" + str(suma_p1_rounds123) + ")")
        #     exit()

        blitz_2_2 = input( player_2_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_2_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_2_2 = int(blitz_2_2 )
        dutch_2_2 = int(dutch_2_2 )
        total_2_2 = dutch_2_2  - (blitz_2_2  * 2)
        print("Your total is: " + str(total_2_2))
        total_p2_round3 = total_2_2
        suma_p2_rounds123 = total_p2_round1 + total_p2_round2 + total_p2_round3
        print( player_2_2 + ", your current score is: " + str(suma_p2_rounds123) + "\n")
        # if suma_p2_rounds123 >= 75:
        #     print( player_2_2 + " is the winner!!!" + "(" + str(suma_p2_rounds123) + ")")
        #     exit()     


        if suma_p1_rounds123 >= 75 and suma_p1_rounds123 > suma_p2_rounds123:
            print( player_2_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds123 >= 75 and suma_p2_rounds123 > suma_p1_rounds123:
            print( player_2_2 + " is the winner!!!!")
            exit()  


#final round 3

#round 4
        blitz_2_1 = input( player_2_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_2_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_2_1 = int(blitz_2_1 )
        dutch_2_1 = int(dutch_2_1 )
        total_2_1 = dutch_2_1  - (blitz_2_1  * 2)
        print("Your total is: " + str(total_2_1))
        total_p1_round4 = total_2_1
        suma_p1_rounds1234 = total_p1_round1 + total_p1_round2 + total_p1_round3 + total_p1_round4
        print( player_2_1 + ", your current score is: " + str(suma_p1_rounds1234) + "\n")
        # if suma_p1_rounds1234 >= 75:
        #     print( player_2_1 + " is the winner!!!" + "(" + str(suma_p1_rounds1234) + ")")
        #     exit()

        blitz_2_2 = input( player_2_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_2_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_2_2 = int(blitz_2_2 )
        dutch_2_2 = int(dutch_2_2 )
        total_2_2 = dutch_2_2  - (blitz_2_2  * 2)
        print("Your total is: " + str(total_2_2))
        total_p2_round4 = total_2_2
        suma_p2_rounds1234 = total_p2_round1 + total_p2_round2 + total_p2_round3 + total_p2_round4
        print( player_2_2 + ", your current score is: " + str(suma_p2_rounds1234) + "\n")
        # if suma_p2_rounds1234 >= 75:
        #     print( player_2_2 + " is the winner!!!" + "(" + str(suma_p2_rounds1234) + ")")
        #     exit()


        if suma_p1_rounds1234 >= 75 and suma_p1_rounds1234 > suma_p2_rounds1234:
            print( player_2_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds1234 >= 75 and suma_p2_rounds1234 > suma_p1_rounds1234:
            print( player_2_2 + " is the winner!!!!")
            exit()  


#final round 4

#3 players.


#round 1
    elif amount_players == 3:
        player_3_1 = input("Player 1 name: ")
        player_3_2 = input("Player 2 name: ")
        player_3_3 = input("Player 3 name: ")


        blitz_3_1 = input( player_3_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_1 = int(blitz_3_1 )
        dutch_3_1 = int(dutch_3_1 )
        total_3_1 = dutch_3_1  - (blitz_3_1  * 2)
        print("Your total is: " + str(total_3_1) + "\n")
        total_p1_round1 = total_3_1
        # if total_p1_round1 >= 75:
        #     print( player_3_1 + " is the winner!!!" + "(" + str(total_p1_round1) + ")")
        #     exit()

        blitz_3_2 = input( player_3_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_2 = int(blitz_3_2 )
        dutch_3_2 = int(dutch_3_2 )
        total_3_2 = dutch_3_2  - (blitz_3_2  * 2)
        print("Your total is: " + str(total_3_2) + "\n")
        total_p2_round1 = total_3_2
        # if total_p2_round1 >= 75:
        #     print( player_3_2 + " is the winner!!!" + "(" + str(total_p2_round1) + ")")
        #     exit()

        blitz_3_3 = input( player_3_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_3 = int(blitz_3_3 )
        dutch_3_3 = int(dutch_3_3 )
        total_3_3 = dutch_3_3  - (blitz_3_3  * 2)
        print("Your total is: " + str(total_3_3) + "\n")
        total_p3_round1 = total_3_3
        # if total_p3_round1 >= 75:
        #     print( player_3_3 + " is the winner!!!" + "(" + str(total_p3_round1) + ")")
        #     exit()


        if total_p1_round1 >= 75 and total_p1_round1 > total_p2_round1 and total_p1_round1 > total_p3_round1:
            print( player_3_1 + " is the winner!!!!")
            exit()
        if total_p2_round1 >= 75 and total_p2_round1 > total_p1_round1 and total_p2_round1 > total_p3_round1:
            print( player_3_2 + " is the winner!!!!")
            exit()
        if total_p3_round1 >= 75 and total_p3_round1 > total_p1_round1 and total_p3_round1 > total_p2_round1:
            print( player_3_3 + " is the winner!!!!")
            exit() 


#final round 1
#
#round 2
        blitz_3_1 = input( player_3_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_1 = int(blitz_3_1 )
        dutch_3_1 = int(dutch_3_1 )
        total_3_1 = dutch_3_1  - (blitz_3_1  * 2)
        print("Your total is: " + str(total_3_1))
        total_p1_round2 = total_3_1
        suma_p1_rounds12 = total_p1_round1 + total_p1_round2
        print( player_3_1 + ", your current score is: " + str(suma_p1_rounds12) + "\n")
        # if suma_p1_rounds12 >= 75:
        #     print( player_3_1 + " is the winner!!!" + "(" + str(suma_p1_rounds12) + ")")
        #     exit()

        blitz_3_2 = input( player_3_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_2 = int(blitz_3_2 )
        dutch_3_2 = int(dutch_3_2 )
        total_3_2 = dutch_3_2  - (blitz_3_2  * 2)
        print("Your total is: " + str(total_3_2))
        total_p2_round2 = total_3_2
        suma_p2_rounds12 = total_p2_round1 + total_p2_round2
        print( player_3_2 + ", your current score is: " + str(suma_p2_rounds12) + "\n")
        # if suma_p2_rounds12 >= 75:
        #     print( player_3_2 + " is the winner!!!" + "(" + str(suma_p2_rounds12) + ")")
        #     exit()

        blitz_3_3 = input( player_3_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_3 = int(blitz_3_3 )
        dutch_3_3 = int(dutch_3_3 )
        total_3_3 = dutch_3_3  - (blitz_3_3  * 2)
        print("Your total is: " + str(total_3_3))
        total_p3_round2 = total_3_3
        suma_p3_rounds12 = total_p3_round1 + total_p3_round2
        print( player_3_3 + ", your current score is: " + str(suma_p3_rounds12) + "\n")
        # if suma_p3_rounds12 >= 75:
        #     print( player_3_3 + " is the winner!!!" + "(" + str(suma_p3_rounds12) + ")")
        #     exit()


        if suma_p1_rounds12 >= 75 and suma_p1_rounds12 > suma_p2_rounds12 and suma_p1_rounds12 > suma_p3_rounds12:
            print( player_3_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds12 >= 75 and suma_p2_rounds12 > suma_p1_rounds12 and suma_p2_rounds12 > suma_p3_rounds12:
            print( player_3_2 + " is the winner!!!!")
            exit()
        if suma_p3_rounds12 >= 75 and suma_p3_rounds12 > suma_p1_rounds12 and suma_p3_rounds12 > suma_p2_rounds12:
            print( player_3_3 + " is the winner!!!!")
            exit()


#final round 2
#
#round 3
        blitz_3_1 = input( player_3_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_1 = int(blitz_3_1 )
        dutch_3_1 = int(dutch_3_1 )
        total_3_1 = dutch_3_1  - (blitz_3_1  * 2)
        print("Your total is: " + str(total_3_1))
        total_p1_round3 = total_3_1
        suma_p1_rounds123 = total_p1_round1 + total_p1_round2 + total_p1_round3
        print( player_3_1 + ", your current score is: " + str(suma_p1_rounds123) + "\n")
        # if suma_p1_rounds123 >= 75:
        #     print( player_3_1 + " is the winner!!!" + "(" + str(suma_p1_rounds123) + ")")
        #     exit()

        blitz_3_2 = input( player_3_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_2 = int(blitz_3_2 )
        dutch_3_2 = int(dutch_3_2 )
        total_3_2 = dutch_3_2  - (blitz_3_2  * 2)
        print("Your total is: " + str(total_3_2))
        total_p2_round3 = total_3_2
        suma_p2_rounds123 = total_p2_round1 + total_p2_round2 + total_p2_round3
        print( player_3_2 + ", your current score is: " + str(suma_p2_rounds123) + "\n")
        # if suma_p2_rounds123 >= 75:
        #     print( player_3_2 + " is the winner!!!" + "(" + str(suma_p2_rounds123) + ")")
        #     exit()

        blitz_3_3 = input( player_3_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_3 = int(blitz_3_3 )
        dutch_3_3 = int(dutch_3_3 )
        total_3_3 = dutch_3_3  - (blitz_3_3  * 2)
        print("Your total is: " + str(total_3_3))
        total_p3_round3 = total_3_3
        suma_p3_rounds123 = total_p3_round1 + total_p3_round2 + total_p3_round3
        print( player_3_3 + ", your current score is: " + str(suma_p3_rounds123) + "\n")
        # if suma_p3_rounds123 >= 75:
        #     print( player_3_3 + " is the winner!!!" + "(" + str(suma_p3_rounds123) + ")")
        #     exit()


        if suma_p1_rounds123 >= 75 and suma_p1_rounds123 > suma_p2_rounds123 and suma_p1_rounds123 > suma_p3_rounds123:
            print( player_3_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds123 >= 75 and suma_p2_rounds123 > suma_p1_rounds123 and suma_p2_rounds123 > suma_p3_rounds123:
            print( player_3_2 + " is the winner!!!!")
            exit()
        if suma_p3_rounds123 >= 75 and suma_p3_rounds123 > suma_p1_rounds123 and suma_p3_rounds123 > suma_p2_rounds123:
            print( player_3_3 + " is the winner!!!!")
            exit()


#final round 3
#
#round 4
        blitz_3_1 = input( player_3_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_1 = int(blitz_3_1 )
        dutch_3_1 = int(dutch_3_1 )
        total_3_1 = dutch_3_1  - (blitz_3_1  * 2)
        print("Your total is: " + str(total_3_1))
        total_p1_round4 = total_3_1
        suma_p1_rounds1234 = total_p1_round1 + total_p1_round2 + total_p1_round3 + total_p1_round4
        print( player_3_1 + ", your current score is: " + str(suma_p1_rounds1234) + "\n")
        # if suma_p1_rounds1234 >= 75:
        #     print( player_3_1 + " is the winner!!!" + "(" + str(suma_p1_rounds1234) + ")")
        #     exit()

        blitz_3_2 = input( player_3_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_2 = int(blitz_3_2 )
        dutch_3_2 = int(dutch_3_2 )
        total_3_2 = dutch_3_2  - (blitz_3_2  * 2)
        print("Your total is: " + str(total_3_2))
        total_p2_round4 = total_3_2
        suma_p2_rounds1234 = total_p2_round1 + total_p2_round2 + total_p2_round3 + total_p2_round4
        print( player_3_2 + ", your current score is: " + str(suma_p2_rounds1234) + "\n")
        # if suma_p2_rounds1234 >= 75:
        #     print( player_3_2 + " is the winner!!!" + "(" + str(suma_p2_rounds1234) + ")")
        #     exit()

        blitz_3_3 = input( player_3_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_3_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_3_3 = int(blitz_3_3 )
        dutch_3_3 = int(dutch_3_3 )
        total_3_3 = dutch_3_3  - (blitz_3_3  * 2)
        print("Your total is: " + str(total_3_3))
        total_p3_round4 = total_3_3
        suma_p3_rounds1234 = total_p3_round1 + total_p3_round2 + total_p3_round3 + total_p3_round4
        print( player_3_3 + ", your current score is: " + str(suma_p3_rounds1234) + "\n")
        # if suma_p3_rounds1234 >= 75:
        #     print( player_3_3 + " is the winner!!!" + "(" + str(suma_p3_rounds1234) + ")")
        #     exit()


        if suma_p1_rounds1234 >= 75 and suma_p1_rounds1234 > suma_p2_rounds1234 and suma_p1_rounds1234 > suma_p3_rounds1234:
            print( player_3_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds1234 >= 75 and suma_p2_rounds1234 > suma_p1_rounds1234 and suma_p2_rounds1234 > suma_p3_rounds1234:
            print( player_3_2 + " is the winner!!!!")
            exit()
        if suma_p3_rounds1234 >= 75 and suma_p3_rounds1234 > suma_p1_rounds1234 and suma_p3_rounds1234 > suma_p2_rounds1234:
            print( player_3_3 + " is the winner!!!!")
            exit()


#final round 4

# 4 players

#round 1
    elif amount_players == 4:
        player_4_1 = input("Player 1 name: ")
        player_4_2 = input("Player 2 name: ")
        player_4_3 = input("Player 3 name: ")
        player_4_4 = input("Player 4 name: ")


        blitz_4_1 = input( player_4_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_1 = int(blitz_4_1 )
        dutch_4_1 = int(dutch_4_1 )
        total_4_1 = dutch_4_1  - (blitz_4_1  * 2)
        print("Your total is: " + str(total_4_1) + "\n")
        total_p1_round1 = total_4_1
        # if total_p1_round1 >= 75:
        #     print( player_4_1 + " is the winner!!!" + "(" + str(total_p1_round1) + ")")
        #     exit()

        blitz_4_2 = input( player_4_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_2 = int(blitz_4_2 )
        dutch_4_2 = int(dutch_4_2 )
        total_4_2 = dutch_4_2  - (blitz_4_2  * 2)
        print("Your total is: " + str(total_4_2) + "\n")
        total_p2_round1 = total_4_2
        # if total_p2_round1 >= 75:
        #     print( player_4_2 + " is the winner!!!" + "(" + str(total_p2_round1) + ")")
        #     exit()

        blitz_4_3 = input( player_4_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_3 = int(blitz_4_3 )
        dutch_4_3 = int(dutch_4_3 )
        total_4_3 = dutch_4_3  - (blitz_4_3  * 2)
        print("Your total is: " + str(total_4_3) + "\n")
        total_p3_round1 = total_4_3
        # if total_p3_round1 >= 75:
        #     print( player_4_3 + " is the winner!!!" + "(" + str(total_p3_round1) + ")")
        #     exit()

        blitz_4_4 = input( player_4_4 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_4 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_4 = int(blitz_4_4 )
        dutch_4_4 = int(dutch_4_4 )
        total_4_4 = dutch_4_4  - (blitz_4_4  * 2)
        print("Your total is: " + str(total_4_4) + "\n")
        total_p4_round1 = total_4_4
        # if total_p4_round1 >= 75:
        #     print( player_4_4 + " is the winner!!!" + "(" + str(total_p4_round1) + ")")
        #     exit()

        
        if total_p1_round1 >= 75 and total_p1_round1 > total_p2_round1 and total_p1_round1 > total_p3_round1 and total_p1_round1 > total_p4_round1:
            print( player_4_1 + " is the winner!!!!")
            exit()
        if total_p2_round1 >= 75 and total_p2_round1 > total_p1_round1 and total_p2_round1 > total_p3_round1 and total_p2_round1 > total_p4_round1:
            print( player_4_2 + " is the winner!!!!")
            exit()
        if total_p3_round1 >= 75 and total_p3_round1 > total_p1_round1 and total_p3_round1 > total_p2_round1 and total_p3_round1 > total_p4_round1:
            print( player_4_3 + " is the winner!!!!")
            exit() 
        if total_p4_round1 >= 75 and total_p4_round1 > total_p1_round1 and total_p4_round1 > total_p2_round1 and total_p4_round1 > total_p3_round1:
            print( player_4_4 + " is the winner!!!!")
            exit()


#final round 1

#round 2
        blitz_4_1 = input( player_4_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_1 = int(blitz_4_1 )
        dutch_4_1 = int(dutch_4_1 )
        total_4_1 = dutch_4_1  - (blitz_4_1  * 2)
        print("Your total is: " + str(total_4_1) + "\n")
        total_p1_round2 = total_4_1
        suma_p1_rounds12 = total_p1_round1 + total_p1_round2
        print( player_4_1 + ", your current score is: " + str(suma_p1_rounds12) + "\n")
        # if suma_p1_rounds12 >= 75:
        #     print( player_4_1 + " is the winner!!!" + "(" + str(suma_p1_rounds12) + ")")
        #     exit()

        blitz_4_2 = input( player_4_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_2 = int(blitz_4_2 )
        dutch_4_2 = int(dutch_4_2 )
        total_4_2 = dutch_4_2  - (blitz_4_2  * 2)
        print("Your total is: " + str(total_4_2) + "\n")
        total_p2_round2 = total_4_2
        suma_p2_rounds12 = total_p2_round1 + total_p2_round2
        print( player_4_2 + ", your current score is: " + str(suma_p2_rounds12) + "\n")
        # if suma_p2_rounds12 >= 75:
        #     print( player_4_2 + " is the winner!!!" + "(" + str(suma_p2_rounds12) + ")")
        #     exit()

        blitz_4_3 = input( player_4_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_3 = int(blitz_4_3 )
        dutch_4_3 = int(dutch_4_3 )
        total_4_3 = dutch_4_3  - (blitz_4_3  * 2)
        print("Your total is: " + str(total_4_3) + "\n")
        total_p3_round2 = total_4_3
        suma_p3_rounds12 = total_p3_round1 + total_p3_round2
        print( player_4_3 + ", your current score is: " + str(suma_p3_rounds12) + "\n")
        # if suma_p3_rounds12 >= 75:
        #     print( player_4_3 + " is the winner!!!" + "(" + str(suma_p3_rounds12) + ")")
        #     exit()

        blitz_4_4 = input( player_4_4 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_4 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_4 = int(blitz_4_4 )
        dutch_4_4 = int(dutch_4_4 )
        total_4_4 = dutch_4_4  - (blitz_4_4  * 2)
        print("Your total is: " + str(total_4_4) + "\n")
        total_p4_round2 = total_4_4
        suma_p4_rounds12 = total_p4_round1 + total_p4_round2
        print( player_4_4 + ", your current score is: " + str(suma_p4_rounds12) + "\n")
        # if suma_p4_rounds12 >= 75:
        #     print( player_4_4 + " is the winner!!!" + "(" + str(suma_p4_rounds12) + ")")
        #     exit()


        if suma_p1_rounds12 >= 75 and suma_p1_rounds12 > suma_p2_rounds12 and suma_p1_rounds12 > suma_p3_rounds12 and suma_p1_rounds12 > suma_p4_rounds12:
            print( player_4_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds12 >= 75 and suma_p2_rounds12 > suma_p1_rounds12 and suma_p2_rounds12 > suma_p3_rounds12 and suma_p2_rounds12 > suma_p4_rounds12:
            print( player_4_2 + " is the winner!!!!")
            exit()
        if suma_p3_rounds12 >= 75 and suma_p3_rounds12 > suma_p1_rounds12 and suma_p3_rounds12 > suma_p2_rounds12 and suma_p3_rounds12 > suma_p4_rounds12:
            print( player_4_3 + " is the winner!!!!")
            exit()
        if suma_p4_rounds12 >= 75 and suma_p4_rounds12 > suma_p1_rounds12 and suma_p4_rounds12 > suma_p2_rounds12 and suma_p4_rounds12 > suma_p3_rounds12:
            print( player_4_4 + " is the winner!!!!")
            exit()


#final round 2

#round 3
        blitz_4_1 = input( player_4_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_1 = int(blitz_4_1 )
        dutch_4_1 = int(dutch_4_1 )
        total_4_1 = dutch_4_1  - (blitz_4_1  * 2)
        print("Your total is: " + str(total_4_1) + "\n")
        total_p1_round3 = total_4_1
        suma_p1_rounds123 = total_p1_round1 + total_p1_round2 + total_p1_round3
        print( player_4_1 + ", your current score is: " + str(suma_p1_rounds123) + "\n")
        # if suma_p1_rounds123 >= 75:
        #     print( player_4_1 + " is the winner!!!" + "(" + str(suma_p1_rounds123) + ")")
        #     exit()

        blitz_4_2 = input( player_4_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_2 = int(blitz_4_2 )
        dutch_4_2 = int(dutch_4_2 )
        total_4_2 = dutch_4_2  - (blitz_4_2  * 2)
        print("Your total is: " + str(total_4_2) + "\n")
        total_p2_round3 = total_4_2
        suma_p2_rounds123 = total_p2_round1 + total_p2_round2 + total_p2_round3
        print( player_4_2 + ", your current score is: " + str(suma_p2_rounds123) + "\n")
        # if suma_p2_rounds123 >= 75:
        #     print( player_4_2 + " is the winner!!!" + "(" + str(suma_p2_rounds123) + ")")
        #     exit()

        blitz_4_3 = input( player_4_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_3 = int(blitz_4_3 )
        dutch_4_3 = int(dutch_4_3 )
        total_4_3 = dutch_4_3  - (blitz_4_3  * 2)
        print("Your total is: " + str(total_4_3) + "\n")
        total_p3_round3 = total_4_3
        suma_p3_rounds123 = total_p3_round1 + total_p3_round2 + total_p3_round3
        print( player_4_3 + ", your current score is: " + str(suma_p3_rounds123) + "\n")
        # if suma_p3_rounds123 >= 75:
        #     print( player_4_3 + " is the winner!!!" + "(" + str(suma_p3_rounds123) + ")")
        #     exit()

        blitz_4_4 = input( player_4_4 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_4 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_4 = int(blitz_4_4 )
        dutch_4_4 = int(dutch_4_4 )
        total_4_4 = dutch_4_4  - (blitz_4_4  * 2)
        print("Your total is: " + str(total_4_4) + "\n")
        total_p4_round3 = total_4_4
        suma_p4_rounds123 = total_p4_round1 + total_p4_round2 + total_p4_round3
        print( player_4_4 + ", your current score is: " + str(suma_p4_rounds123) + "\n")
        # if suma_p4_rounds123 >= 75:
        #     print( player_4_4 + " is the winner!!!" + "(" + str(suma_p4_rounds123) + ")")
        #     exit()


        if suma_p1_rounds123 >= 75 and suma_p1_rounds123 > suma_p2_rounds123 and suma_p1_rounds123 > suma_p3_rounds123 and suma_p1_rounds123 > suma_p4_rounds123:
            print( player_4_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds123 >= 75 and suma_p2_rounds123 > suma_p1_rounds123 and suma_p2_rounds123 > suma_p3_rounds123 and suma_p2_rounds123 > suma_p4_rounds123:
            print( player_4_2 + " is the winner!!!!")
            exit()
        if suma_p3_rounds123 >= 75 and suma_p3_rounds123 > suma_p1_rounds123 and suma_p3_rounds123 > suma_p2_rounds123 and suma_p3_rounds123 > suma_p4_rounds123:
            print( player_4_3 + " is the winner!!!!")
            exit()
        if suma_p4_rounds123 >= 75 and suma_p4_rounds123 > suma_p1_rounds123 and suma_p4_rounds123 > suma_p2_rounds123 and suma_p4_rounds123 > suma_p3_rounds123:
            print( player_4_4 + " is the winner!!!!")
            exit()


#final round 3

#round 4
        blitz_4_1 = input( player_4_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_1 = int(blitz_4_1 )
        dutch_4_1 = int(dutch_4_1 )
        total_4_1 = dutch_4_1  - (blitz_4_1  * 2)
        print("Your total is: " + str(total_4_1) + "\n")
        total_p1_round4 = total_4_1
        suma_p1_rounds1234 = total_p1_round1 + total_p1_round2 + total_p1_round3 + total_p1_round4
        print( player_4_1 + ", your current score is: " + str(suma_p1_rounds1234) + "\n")
        # if suma_p1_rounds1234 >= 75:
        #     print( player_4_1 + " is the winner!!!" + "(" + str(suma_p1_rounds1234) + ")")
        #     exit()

        blitz_4_2 = input( player_4_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_2 = int(blitz_4_2 )
        dutch_4_2 = int(dutch_4_2 )
        total_4_2 = dutch_4_2  - (blitz_4_2  * 2)
        print("Your total is: " + str(total_4_2) + "\n")
        total_p2_round4 = total_4_2
        suma_p2_rounds1234 = total_p2_round1 + total_p2_round2 + total_p2_round3 + total_p2_round4
        print( player_4_2 + ", your current score is: " + str(suma_p2_rounds1234) + "\n")
        # if suma_p2_rounds1234 >= 75:
        #     print( player_4_2 + " is the winner!!!" + "(" + str(suma_p2_rounds1234) + ")")
        #     exit()

        blitz_4_3 = input( player_4_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_3 = int(blitz_4_3 )
        dutch_4_3 = int(dutch_4_3 )
        total_4_3 = dutch_4_3  - (blitz_4_3  * 2)
        print("Your total is: " + str(total_4_3) + "\n")
        total_p3_round4 = total_4_3
        suma_p3_rounds1234 = total_p3_round1 + total_p3_round2 + total_p3_round3 + total_p3_round4
        print( player_4_3 + ", your current score is: " + str(suma_p3_rounds1234) + "\n")
        # if suma_p3_rounds1234 >= 75:
        #     print( player_4_3 + " is the winner!!!" + "(" + str(suma_p3_rounds1234) + ")")
        #     exit()

        blitz_4_4 = input( player_4_4 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_4 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_4 = int(blitz_4_4 )
        dutch_4_4 = int(dutch_4_4 )
        total_4_4 = dutch_4_4  - (blitz_4_4  * 2)
        print("Your total is: " + str(total_4_4) + "\n")
        total_p4_round4 = total_4_4
        suma_p4_rounds1234 = total_p4_round1 + total_p4_round2 + total_p4_round3 + total_p4_round4
        print( player_4_4 + ", your current score is: " + str(suma_p4_rounds1234) + "\n")
        # if suma_p4_rounds1234 >= 75:
        #     print( player_4_4 + " is the winner!!!" + "(" + str(suma_p4_rounds1234) + ")")
        #     exit()



        if suma_p1_rounds1234 >= 75 and suma_p1_rounds1234 > suma_p2_rounds1234 and suma_p1_rounds1234 > suma_p3_rounds1234 and suma_p1_rounds1234 > suma_p4_rounds1234:
            print( player_4_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds1234 >= 75 and suma_p2_rounds1234 > suma_p1_rounds1234 and suma_p2_rounds1234 > suma_p3_rounds1234 and suma_p2_rounds1234 > suma_p4_rounds1234:
            print( player_4_2 + " is the winner!!!!")
            exit()
        if suma_p3_rounds1234 >= 75 and suma_p3_rounds1234 > suma_p1_rounds1234 and suma_p3_rounds1234 > suma_p2_rounds1234 and suma_p3_rounds1234 > suma_p4_rounds1234:
            print( player_4_3 + " is the winner!!!!")
            exit()
        if suma_p4_rounds1234 >= 75 and suma_p4_rounds1234 > suma_p1_rounds1234 and suma_p4_rounds1234 > suma_p2_rounds1234 and suma_p4_rounds1234 > suma_p3_rounds1234:
            print( player_4_4 + " is the winner!!!!")
            exit()


#final round 4

#round 5
        blitz_4_1 = input( player_4_1 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_1 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_1 = int(blitz_4_1 )
        dutch_4_1 = int(dutch_4_1 )
        total_4_1 = dutch_4_1  - (blitz_4_1  * 2)
        print("Your total is: " + str(total_4_1) + "\n")
        total_p1_round5 = total_4_1
        suma_p1_rounds12345 = total_p1_round1 + total_p1_round2 + total_p1_round3 + total_p1_round4 + total_p1_round5
        print( player_4_1 + ", your current score is: " + str(suma_p1_rounds12345) + "\n")
        # if suma_p1_rounds1234 >= 75:
        #     print( player_4_1 + " is the winner!!!" + "(" + str(suma_p1_rounds1234) + ")")
        #     exit()

        blitz_4_2 = input( player_4_2 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_2 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_2 = int(blitz_4_2 )
        dutch_4_2 = int(dutch_4_2 )
        total_4_2 = dutch_4_2  - (blitz_4_2  * 2)
        print("Your total is: " + str(total_4_2) + "\n")
        total_p2_round5 = total_4_2
        suma_p2_rounds12345 = total_p2_round1 + total_p2_round2 + total_p2_round3 + total_p2_round4 + total_p2_round5
        print( player_4_2 + ", your current score is: " + str(suma_p2_rounds12345) + "\n")
        # if suma_p2_rounds1234 >= 75:
        #     print( player_4_2 + " is the winner!!!" + "(" + str(suma_p2_rounds1234) + ")")
        #     exit()

        blitz_4_3 = input( player_4_3 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_3 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_3 = int(blitz_4_3 )
        dutch_4_3 = int(dutch_4_3 )
        total_4_3 = dutch_4_3  - (blitz_4_3  * 2)
        print("Your total is: " + str(total_4_3) + "\n")
        total_p3_round5 = total_4_3
        suma_p3_rounds12345 = total_p3_round1 + total_p3_round2 + total_p3_round3 + total_p3_round4 + total_p3_round5
        print( player_4_3 + ", your current score is: " + str(suma_p3_rounds12345) + "\n")
        # if suma_p3_rounds1234 >= 75:
        #     print( player_4_3 + " is the winner!!!" + "(" + str(suma_p3_rounds1234) + ")")
        #     exit()

        blitz_4_4 = input( player_4_4 + ", how many cards do you have left on your Blitz Pile?\n")
        dutch_4_4 = input("How many cards do you have from your Dutch Pile?\n")
        blitz_4_4 = int(blitz_4_4 )
        dutch_4_4 = int(dutch_4_4 )
        total_4_4 = dutch_4_4  - (blitz_4_4  * 2)
        print("Your total is: " + str(total_4_4) + "\n")
        total_p4_round5 = total_4_4
        suma_p4_rounds12345 = total_p4_round1 + total_p4_round2 + total_p4_round3 + total_p4_round4 + total_p4_round5
        print( player_4_4 + ", your current score is: " + str(suma_p4_rounds12345) + "\n")
        # if suma_p4_rounds1234 >= 75:
        #     print( player_4_4 + " is the winner!!!" + "(" + str(suma_p4_rounds1234) + ")")
        #     exit()


        if suma_p1_rounds12345 >= 75 and suma_p1_rounds12345 > suma_p2_rounds12345 and suma_p1_rounds12345 > suma_p3_rounds12345 and suma_p1_rounds12345 > suma_p4_rounds12345:
            print( player_4_1 + " is the winner!!!!")
            exit()
        if suma_p2_rounds12345 >= 75 and suma_p2_rounds12345 > suma_p1_rounds12345 and suma_p2_rounds12345 > suma_p3_rounds12345 and suma_p2_rounds12345 > suma_p4_rounds12345:
            print( player_4_2 + " is the winner!!!!")
            exit()
        if suma_p3_rounds12345 >= 75 and suma_p3_rounds12345 > suma_p1_rounds12345 and suma_p3_rounds12345 > suma_p2_rounds12345 and suma_p3_rounds12345 > suma_p4_rounds12345:
            print( player_4_3 + " is the winner!!!!")
            exit()
        if suma_p4_rounds12345 >= 75 and suma_p4_rounds12345 > suma_p1_rounds12345 and suma_p4_rounds12345 > suma_p2_rounds12345 and suma_p4_rounds12345 > suma_p3_rounds12345:
            print( player_4_4 + " is the winner!!!!")
            exit()


#final round 5


    else:
        print("Please enter a number from 2 to 4.")


if __name__ == "__main__":
    run()