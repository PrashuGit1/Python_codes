try:
    n=int(input('Enter the number : '))
    result=10/n
except ZeroDivisionError:
    print("can't devided by Zero !")
except ValueError:
    print("Please enter the valid number !")
else:
    print('Devision is : ', result)
finally:
    print("This always runs.")