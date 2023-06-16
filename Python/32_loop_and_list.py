the_count=[1,2,3,4,5,6]
fruits=['Apple','Orange','Pears','Apricot']
changes=[1,'Penis',2,'dimes',3,'quarters']

for number in the_count:
    print(f"This is count:{number}")

for fruits in fruits:
    print(f"The fruits type is:{fruits}")    


for i in changes:
    print(f"I got it :{i}")

elements=[]

for i in range(0,6):
    print(f"Adding {i} to the list:")
    elements.append(i)


for i in elements:
    print(f"Element was :{i}")
