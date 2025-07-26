#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:
    print("\n-----CALCULATOR-----")
    print("Enter an Operation (+, - , * , /) or press 'q' for exit.")

    process = input("Operation : ")

    if process.lower() == "q":
        print("Exiting...")
        break
    if process not in ["+", "-","*" , "/",]:
        print("Invalid operation. ")
        continue 

    numbers = []

    print("Enter number one by one. Type 'done' to finish ")

    while True:
        data = input("Number : ")
        if data.lower() == "done":
            break
        try: 
            number = float(data)
            numbers.append(number)
        except ValueError:
            print("Invalid Number.. ")

    if len(numbers) == 0:
        print("No Numbers Entered! ")
        continue 

    # Perform the operation:

    if process == "+":
        Result = (sum(numbers))

    if process == "*":
        Result = 1
        for n in numbers:
            Result *= n

    if process == "-":
        Result = numbers[0]
        for c in numbers[1::]:
            Result -= c

    if process == "/":
        try:    
            Result = numbers[0]
            for b in numbers[1::]:
                Result /= b
        except ZeroDivisionError:
            print("Zero Division Error!. ")
            continue 

    print(f"Result = {Result}")


# In[ ]:




