#collect user input for string
name = input("What is your name?")

#collect user input for integer
age = int(input("How old are you? "))

#collect user input for boolean
trueOrFalse = bool(input("Is the input true? "))

#print results
print("My name is " + name)
print("I will be " + str(age + 1) + " next year.")
print("The input was converted to " + str(trueOrFalse))