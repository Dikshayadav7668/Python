from sys import exit

def gold_room():
    print("This room is full of gold.How much do you take.")

    choice=input(">")
    if '0' in choice or '1' in choice:
        how_much=int (choice)


    else:
        print("man learn to type a number")    



    if how_much<50:
        print("You are not greedy! good exit")
        exit(0)    


    else:
        print("You greedy bastered!")


def bear_room():
    print("There is a bear hear")
    print("The bear has a bunch of honey")
    print("the fat bear is in front of another door")
    print("How are you going to move the bear")
    bear_moved=False


    while True:
        choice=input(">")

        if choice=="take honey":
            dead ("The bear looks at you and slap of you")


        elif choice=="taunt bear" and not bear_moved:
            print("The bear has moved from the door:")   
            print("You can go throw it now.")
            bear_moved=True

        elif choice=="taunt bear" and bear_moved:
            dead("The bear get pissed off and  chews your leg off")   


        elif choice=="open door" and bear_moved:
            gold_room()     


        else:
            print("I got not idea what that means.")    


def cthulhu_room():
    print("Here you see the great evil cthulhu")           
    print("He, it whatever stares at you and you go insane")
    print("Do you flee for your life  and eat your head")
       


    choice=input(">")   

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("Well that was tasty!")    


    else:
        cthulhu_room()    


def dead(why):
        print(why,"Good job!")  


def start():
        print("You are in dark room")      
        print("There is a door to your left and right")
        print("Which one do you take")



        choice=input(">")    

        if choice=="left":
           bear_room()


        elif choice=="right":
          cthulhu_room()    

        else:
            dead("You stumble around the room until you starve")



start ()



