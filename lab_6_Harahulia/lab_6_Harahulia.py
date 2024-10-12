# [[[ Завдання 1 ]]]
def is_year_leap(year):
    #
    # Write your code here.
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    #
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
  yr = test_data[i]
  print(yr,"->",end="")
  result = is_year_leap(yr)
  if result == test_results[i]:
      print("OK")
  else:
      print("Failed")

# [[[ Завдання 2 ]]]
# def is_year_leap(year):
# #
# # Your code from LAB 4.3.6.
# #

def days_in_month(year, month):
    #
    # Write your new code here.
    global cheatsheet_common, cheatsheet_leap
    cheatsheet_common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cheatsheet_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 0 < month < 13:
        if not is_year_leap(year):
            return cheatsheet_common[month -1]
        else: return cheatsheet_leap[month -1]
    else: return
    #

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
  yr = test_years[i]
  mo = test_months[i]
  print(yr, mo, "->", end="")
  result = days_in_month(yr, mo)
  if result == test_results[i]:
      print("OK")
  else:
      print("Failed")

# [[[ Завдання 3 ]]]
# def is_year_leap(year):
# #
# # Your code from LAB 4.3.1.6.
# #

# def days_in_month(year, month):
# #
# # Your code from LAB 4.3.1.7.
# #

def day_of_year(year, month, day):
    #
    # Write your new code here.
    day_o_year = 0
    if not 0 < month < 13:
        return
    elif day in range(1, days_in_month(year, month) +1, 1):
        for d in cheatsheet_common[:month-1]:
            day_o_year += d
        return day_o_year + day
    else: return
    #

print(day_of_year(2000, 12, 31))
print(day_of_year(2024, 10, 11))
print(day_of_year(2000, 12, 33))
print(day_of_year(2000, 13, 31))


# [[[ Завдання 4 ]]]
def is_prime(num):
    #
    # Write your code here.
    beacon_for_prime = [2, 3, 5, 7] #працює до 120 включно, далі потребує розширення простими числами
    for j in beacon_for_prime:
        if num == j:
            continue
        elif num % j == 0:
            return False
        elif num % j != 0:
            continue
    return True
    #

for i in range(1, 20):
  if is_prime(i + 1):
          print(i + 1, end=" ")
print()


# [[[ Завдання 5 ]]]
def liters_100km_to_miles_gallon(liters):
    #
    # Write your code here.
    return 3.785411784 * 100 * 1000 / (liters * 1609.344)
    #

def miles_gallon_to_liters_100km(miles):
    #
    # Write your code here.
    return 3.785411784 * 100 * 1000 / (miles * 1609.344)
    #

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


# [[[ Завдання 6 ]]]
def is_a_triangle(a, b, c):
    if a + b < c:
        return False
    elif a + c < b:
        return False
    elif b + c < a:
        return False
    else: return True

print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 2, 5))
print(is_a_triangle(5, 1, 2))
print(is_a_triangle(2, 5, 1))
print(is_a_triangle(15, 10, 15))


# [[[ Завдання 7 ]]]
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return "Не трикутник"
    if a**2 + b**2 == c**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    else: return False

print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(1, 2, 5))
print(is_a_right_triangle(15, 10, 15))