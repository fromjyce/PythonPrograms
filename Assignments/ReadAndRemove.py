'''
Write a python program to read contents from a file and store the result in a list 
after removing the newline character.
'''

def read_file_contents(file_name):
  with open(file_name, "r") as file:
    contents = file.readlines()
  return [line.strip() for line in contents]

             

file_name = "Sample.txt"
contents = read_file_contents(file_name)
with open("SampleRR.txt","w") as file:
   for line in contents:
     file.write(line)

with open("SampleRR.txt","r") as file1:
  for line in file1:
    print(line)


