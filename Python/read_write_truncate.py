from sys import argv

script,filename=argv
print(f"We are going to erase{filename}")
print(f"If you don't want that, hit CTRL-C(^C)")
print(f"If you do not want hit Return")

input('?')
print("Opening the file name")
target=open(filename,'w')

print("Truncatin the file,Good Bye!")
target.truncate()

print("Now I'm ask you for in three lines")
line1=input("Line 1 is:")
line2=input("Line 2 is:")
line3=input("Line 3 is:")

print("I'm going to write these to the file")
target.write(line1)
target.write("/n")
target.write(line2)
target.write("/n")
target.write(line3)
target.write("\n")

print("Now I'm Close this file")
target.close()
