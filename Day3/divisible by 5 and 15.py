start = int(10)
end = int(150)
counter = start
while counter <= end:
    if counter % 15 == 0 and counter % 5 == 0:
        print(counter, " is divisible by 15 and 5")
    counter += 1