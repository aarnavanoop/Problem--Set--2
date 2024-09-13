def is_valid(s):
    #check if it is between 2 and 6 characters and starts with two letters and has no punctuation
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        if s.isalpha():
            return True
        else:
            i = 0
            while i < len(s):
                    #check if the character is a digit
                    if s[i].isdigit():
                            #if the first character is a digit, break out since we start from s[0]
                        if s[i] == "0":
                            return False
                            #if after the first digit the rest of the digits are numbers return true
                        elif s[i:].isdigit():
                            return True
                        elif s[i].isalpha():
                            pass
                        else:
                            return False
                    
                    i+= 1
    else:
        return False

def first_check(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        return True
    else:
        return False



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()