number = int(input("enter your number"))
even_number = 0
odd_number = 0
while number > 0:
    dig = number % 10
    number= number // 10 
    if dig % 2 == 0:
        even_number+= 1
    else:
            odd_number += 1

if even_number > odd_number:
    print("even digits are more than odd digits")
elif even_number == odd_number:
    print("even digits are equal odd digits")
else:
    print("odd digits are more than even digits")
