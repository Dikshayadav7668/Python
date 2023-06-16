people=30
cars=40
trucks=15


if cars>people:
    print("We should take the car")


elif people>cars:
    print("We should not take the car")

else :
    print("We can't decide")


if trucks>cars:
    print("there are to many trucks")   

elif trucks<cars:
    print("May be could take the car")

else:
    print("We still can't decide")   

if people>trucks:
    print("Alright, let's just take the car")   


else:
    print("Fine .Lets stay home then.")