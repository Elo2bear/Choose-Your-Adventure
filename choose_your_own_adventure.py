name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to and end and you can choose to go either left or right, which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across")
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose')


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you wan to cross it or head back (cross/back)?")
    
    if answer == "back":
        print("You go back to the main road and lose.")
    elif answer == "cross":
         answer = input("You cross the bridge and meet a wizard. Do you talk to them (yes/no)?")
        
         if answer == "yes":
            print("You talk to the wizzard and recieve magic, You win!")
         elif answer == "no":
            print("You ignore wizard and You lose")
         else:
            print('Not a valid option. You lose.')
        
    else:
            print('Not a valid option. You lose.')
            
    print("Thank you for playing!")
 
