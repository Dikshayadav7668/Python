def add(a,b):
    print(f"Adding {a}+{b}")
    return a+b

def subtract(a,b):
    print(f"Subtracting {a}-{b}")
    return a-b

def multiply(a,b):
    print(f"Multiplying {a}*{b}")
    return a*b

def divison(a,b):    
    print(f"Divison {a}/{b}")
    return a/b


print("Lets fun with the maths")    
age=add(30,14)
height=subtract(758,563)
weight=multiply(15,2)
iq=divison(100,2)


print(f"Age is{age} height {height} weight{weight} and iq is {iq}")


print ("Here is a puzzle:")

what=add(age,subtract(height,multiply(weight,divison(iq,2))))
print("That becomes:", what," can you do it become hand")