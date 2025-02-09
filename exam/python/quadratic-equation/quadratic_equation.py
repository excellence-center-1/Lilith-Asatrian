import equation
def main():
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        print("The roots of this equation are: ", equation.equation(a,b,c))
    except ValueError:
        print("Not valid arguments are given.")
    finally:
        print("End of program.")

main()