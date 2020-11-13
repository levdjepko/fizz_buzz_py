
# fizz buzz - 
# print fizz when divisible by 3
# print buzz when divisible by 5
# print fizzbuzz when divisible by 15

for num in range(1, 101):
  if (num % 15 == 0):
    print ("FizzBuzz")
  elif (num % 5 == 0):
    print ("Buzz")  
  elif (num % 3 == 0):
    print ("Fizz") 
  else:
    print (num)
