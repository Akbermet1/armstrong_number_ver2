import math

def armstrongNumber():

    for number in range(1000):
        if number >= 0 and number < 10:
            print(number)
        elif number >= 10 and number < 100:
            tens = math.floor(number/10)
            digits = number % 10

            calculation = tens**2+digits**2

            if number == calculation:
                print(number)
        else:
            hundreds = math.floor(number/100)
            tens = math.floor((number % 100)/10)
            digits = number % 10

            calculation = hundreds**3+tens**3+digits**3

            if calculation == number:
                print(number)


armstrongNumber()