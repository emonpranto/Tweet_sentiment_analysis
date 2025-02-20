student = ["Alice", "Bob", "Charlie","David", "Eve"]

for i in range(len(student)):
    name = student[i].split()
    if name[0][0] == 'A' :
        print(name[0])
    if name[0][0] == 'D':
        print(name[0])

## Another python fuction we can use is startswith 

for name in student:
    if name.startswith(("A","D")):
        print(name)