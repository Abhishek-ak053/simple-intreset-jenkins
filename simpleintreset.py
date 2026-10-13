def simInt(principal, intrest  , time):
  
    return (principal * intrest * time)/100

if __name__ == "__main__":
    principal = int(input("Enter the principal amount: "))
    intrest = int(input("Enter the interest rate (in %): "))
    time = int(input("Enter the time (in years): "))

    simple_interest = simInt(principal, intrest, time)
    print(f"The simple interest is: {simple_interest}")