import math

mu = float(input("Введіть Mu (середнє): "))
sigma = float(input("Введіть Sigma (дисперсія): "))
x = float(input("Введіть x: "))
f_x = 1 / (sigma * (2 * math.pi)**(1 /2)) * math.exp(-((x - mu)**2) / (2 * sigma ** 2))
print(f_x)

john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=", ")
totalApple = john + mary + adam
print(totalApple)
print("Загальна кількість яблук в наших героїв дорівнює " + str(totalApple))

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)


# this program computes the number of seconds in a given number of hours

hours = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", hours) #printing the number of hours
print("Seconds in Hours: ", hours * seconds) # printing the number of seconds in a given number of hours

#to do: add "Goodbye" message; increase hours to 3


a = float(input("Введіть a: "))# input a float value for variable a here
b = float(input("Введіть b: "))# input a float value for variable b here

print(a + b)# output the result of addition here
print(a - b)# output the result of subtraction here
print(a * b)# output the result of multiplication here
print(a / b)# output the result of division here

print("\nThat's all, folks!")

x = float(input("Enter value for x: "))

# put your code here
y = x + 1/x
y = x + 1/y
y = x + 1/y
y = x + 1/y
y = 1 / y
print("y =", y)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
mins += hour * 60
mins += dura
hour = mins // 60
hour = hour % 24
mins = mins % 60

print("Час завершення події: ", str(hours) + ':', mins, sep="")