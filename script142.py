low_rate = 0
medium_rate = 0
high_rate = 0
total = 0
while True :
    rating = int(input("Enter a rating (-1 to stop)"))
    if rating == -1:
        break

    if rating < 1 or rating > 5 :
        continue

    if rating == 1 or rating ==2 :
        low_rate += 1

    elif rating ==4 or rating == 5:
        high_rate +=1

    total +=1

print("Total valid ratings :", total)
print("Low ratings(1-2)", low_rate)
print("Medium ratings (3):", medium_rate)
print("High ratings (4-5):", high_rate)
