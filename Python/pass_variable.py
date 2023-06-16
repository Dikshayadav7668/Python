#from sys import argv


#script, first, second, orange =argv

#print("The script is called:",script)
#print("Your first variable is :",first)
#print("Your second variable is :",second )
#print("Your thired variable is :",orange)
#from sys import argv

#script,user_name=argv
#prompt='>'

#print(f"Hi {user_name}. I'm {script} script")
#print(f"I'd like to you ask you some question")
#print(f"Do you like me{user_name}")
#likes=input(prompt)

#print(f"Where do you live{user_name}")
#lives=input(prompt)

#print(f"Where do you live{user_name}")
#computer=input(prompt)

#print(f"""
#Alright,so you said{likes} about liking me
#You live in{lives} where you not sure it
#and you have a {computer} computer .Nice
#""")
from sys import argv

script,filename=argv

txt=open(filename)
print(f"Here is you file name{filename}")

print(txt.read())

print("Open your file again")
file_again=input(">")

txt_again=open(file_again)
print(txt_again.read())
