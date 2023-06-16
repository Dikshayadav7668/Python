from sys import argv
from os.path import exists

script,from_file,to_file=argv

print(f"Copying from{from_file} to{to_file}")
in_file=open(from_file)
indata=in_file.read()

print(f"The input file is{len(indata)} byte long")
print(f"Does the output of file exists{exists(to_file)}")

print("Ready hit return to continue,CTRL-C to abort")

out_file=open(to_file,'w')
out_file.write(indata)

print("All right , all done")
out_file.close()
in_file.close()

