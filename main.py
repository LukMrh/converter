print "Welcome to my simple converter!"
convert = 0.62137

while True:
    try:
        km = int(raw_input("Please enter the number of kilometers:"))
    except:
        print "Kilometers entered must be a number!"
        break

    print km * convert

    answer = raw_input("Would you try once more (y/n)?").lower()

    if answer != "y":
        break
