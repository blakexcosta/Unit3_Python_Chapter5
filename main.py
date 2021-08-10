
def main():
    # booleans
    number1 = 1
    number5 = 5
    # boolean values are written as True and False
    if (number1 > number5):
        print("this statement is true")
    else:
        print("this statement is false")

    # list of comparison operators
    # https://education.launchcode.org/lchs/chapters/booleans-and-conditionals/boolean-expressions.html

    #len() example
    text = "Don't panic"
    if(len(text) >= 10):
        print("{} has more than 10 character".format(text))

    # logic operators (and, or, etc.)
    name = "Bob"
    if (len(name)>5 and len(name)<10):
        print("{} is between 5 and 10 characters".format(name))
    else:
        print("{} is either less than 5 characters or greater than 10".format(name))

    # table of operations for operators
    # https://education.launchcode.org/lchs/chapters/booleans-and-conditionals/truth-tables.html

    # chained conditionals, (elif)
    num = 10
    other_num = 20
    if num > other_num:
        print(num, "is greater than", other_num)
    elif num < other_num:
        print(num, "is less than", other_num)
    else:
        print(num, "is equal to", other_num)
        
if __name__ == "__main__":
    main()

