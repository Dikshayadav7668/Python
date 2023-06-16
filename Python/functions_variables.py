def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} booxes of crackers")
    print("Man that is enought for party")
    print("Get a blanket.\n")

    print("We can just give the function name directly")
    cheese_and_crackers(20,60)

    print("Or We can use variable from our script")
    amount_of_cheese=10
    amount_of_crackers=50

    cheese_and_crackers(amount_of_cheese,amount_of_crackers)

    print("We can even do math inside too.")
    cheese_and_crackers(12+3,4+5)

    print("And We combine the two variable and maths")
    cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)