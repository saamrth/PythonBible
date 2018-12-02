
# for comments

name =input("What is your name?: ")

age = input("How old are you? :")

city = input("Where do you live?: ")

hobby = input("What do you love doing?: ")

string = "Your name is {},You are {} years old. You live in {} and you love {}."

output = string.format(name,age,city,hobby)

print(output)
