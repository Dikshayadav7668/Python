from sys import argv

script,filename=argv

txt=open(filename)
print("This is your filename{filename}")
print(txt.read())

print("I trying to again open this file")
file_again=input('>')
txt_again=open(file_again)
print(txt_again.read())