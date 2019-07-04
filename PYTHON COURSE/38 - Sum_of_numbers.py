# sum of numbers 1 to 10 using while loop



total = 0
i = input("Enter a value : ")
i = int(i)

if i > 10:
    print("Value is out of range")

while i <= 10:
    total += i        # or we can write total = total + i
    i += 1            # or we can write i = i + 1
    print(total)       # total = 0+1+2+3+4+5+6+7+8+9+10
