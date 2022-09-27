### Case 1
#Write a program to ask the user to enter two integers and display the division.
#The program must catch the ValueError exception and the ZeroDivisionError exception and display an error message.


try:
  # ask user to enter 2 integers
  user_input = input("Enter the 1st integer: ")
  number1 = int(user_input)

  user_input = input("Enter the 2nd integer: ")
  number2 = int(user_input)

  # calculate the quotient
  quotient = number1/number2

  # display the division equation
  print("{0} / {1} = {2}".format(number1, number2, quotient)) 

except ValueError as e:
  print("You have entered an invalid input")

except ZeroDivisionError as e:
  print("The second number must be non-zero")


### Case 2
# Write a program to ask the user to enter a positive integer.
# The program should keep asking until the user enters a valid input.
# keep asking until we got a valid number
while True:
  try:
    # ask user to enter a positive integer
    user_input = input("Enter a positive integer: ")

    # attempt to translate input into integer
    try:
      number = int(user_input)
    except:
      raise ValueError("Input is not an integer")

    # if number is not positive then raise exception
    if(number <= 0):
      raise ValueError("Input is not a positive integer")

    # if we get to here- then we should have a valid number
    print("You have entered {0}".format(number))
    break

  except ValueError as e:
    print(e)

