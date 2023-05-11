import sys
args = sys.argv
if len(args) < 2:
    print("Please provide a task to perform.")
    exit()
task = args[1]
if task == "greet":
    if len(args) < 3:
        print("Please provide a name to greet.")
        exit()
    name = args[2]
    print("Hello, " + name + "!")
elif task == "count":
    if len(args) < 3:
        print("Please provide a number to count to.")
        exit()
    n = int(args[2])
    for i in range(1, n+1):
        print(i)
else:
    print("Unknown task: " + task)
