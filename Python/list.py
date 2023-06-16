ten_things="Apple.orange,Crows,Telephoe.light,Sugar"

print("Wait there is not a ten things!,Let's fix it")

stuff=ten_things.split(' ')
more_stuff=["day","Night","Song","Frisbee","corn","banana","Girl","boy"]
  

while len(stuff)!=10:
    next_one = more_stuff.pop( )
    print("Adding",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} item now.")


print("there are go:stuff")    
print("Let's  do some thing with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.join(stuff))
print('#'.join(stuff[3:5]))