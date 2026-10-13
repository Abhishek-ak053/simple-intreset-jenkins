import sys
def simInt(principal, intrest  , time):
  
    return (principal * intrest * time)/100

if __name__ == "__main__":
    principal = int(sys.argv[1])
    intrest = int(sys.argv[2])
    time = int(sys.argv[3])
    simple_interest = simInt(principal, intrest, time)
    print(f"The simple interest is: {simple_interest}")