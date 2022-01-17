def calculatePay():
    # Implement your solution in between the two comment blocks
    print("Calculating pay")
    # This first line is provided for you
    hasHrs = False
    hasRate = False

    while hasHrs != True:
        try:
            hrs = input("Enter Hours: ")
            hrs = float(hrs)
            hasHrs = True
        except:
            print ("That is not a valid number. Try again.")

    while hasRate != True:
        try:
            rate = input("Enter Rate: ")
            rate = float(rate)
            hasRate = True
        except:
            print("That is not a valid number. Try again.")

    grossPay = hrs * rate
    print(grossPay)
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()