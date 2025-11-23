try:
 num = int(input("Enter your number : "))
 print(num)
except ValueError as ex:
  print("Exception: ",ex)
except:
  print("Error Occured")
finally:
  print("I will execute no matter what happens")



for i in range(1,11):
    if i==3:
      continue
    print(i)
