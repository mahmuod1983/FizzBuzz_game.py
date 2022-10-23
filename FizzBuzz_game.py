#for-in loop that traverses numbers from 1 to 100


for namber in range(1,201):
  #checking that number is divisible by both 3 and 5
  if(namber%3==0 and namber%5==0):
    print("FizzBuzz")
  #checking that number is divisible by 3
  elif(namber%3 == 0):
    print("Fizz")
  #checking that number is divisible by 5
  elif(namber%5 == 0):
    print("Buzz")
  #And if not divisible by either of them print num as it is
  else:
    print(namber)
