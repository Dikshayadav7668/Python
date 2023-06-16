print("Lets practise everything:")
print('you\'d need to know\' bout escape with\\ that do')
print("\n for newline \t for tab")

poem="""
\t The lovely world 
with logic so firmly planted
cannot discern \n the need oof love
not comprened passion from intution
and require an expalanation
\n\t\where there is npone
"""

print('-------------')
print(poem)
print('--------------')

five=10-2+3-6
print(f"There should be five:{five}")

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates

start_point=10000
beans,jars,crates=secret_formula(start_point)
print("With a a starting point of:{}".format(start_point))

print(f"We have beans{beans} jars {jars} and crates{crates}")

start_point=start_point/10

print("We can aslo do this that way:")
formula=secret_formula(start_point)

print("We have beans {} , jars {} and crates {} .". format(*formula))