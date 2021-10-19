# a = "The sky is purple"
# print(a)

# for letter in a:
#     print(letter)
    
    
def cause_problems_on_purpose(n):
    if n <= 0:
        raise ValueError("negative number. you sent {} smh".format(n))
        
    try:
        from my_calculator import sqrt
    except:
    #except ModeulNotFoundError:
        from math import sqrt
        
    x = sqrt(n)
    return x


def more_problems(b, c):
    
    try:
        return b + c
    except:
        return "you can't add that"
    
def add_positive_integers(a,b):
    if a < 0 or b <0:
        raise ValueError("negative")
        
    if type(a) is not int or type(b) is not int:
        raise TypeError("Cannot add non-integers")
        
    return a + b
    
    
def main():
    print(cause_problems_on_purpose(-4))
    print(more_problems("b", 25))
    try:
         x = add_positive_integers(2,3)
         print(x)
    #except ValueError as err:   puts it into var for you
    except ValueError:
        print("Got value error it does")
    except TypeError:
        print("Got Type Error")
    except:
        print("all other errors")


if __name__ == "__main__":
    main()
    
