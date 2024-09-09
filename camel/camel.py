def snake_case(casing):
    for _ in casing:
            if _.isupper():
                print("_" + _.lower(), end ="")
            else:
                 print(_, end="")
    
    print()
    
def main():
    camel = input("Please enter your input in camelCase: ")
    snake_case(camel)


main()

'''str = "camelCase"
new_str = str[:5] + "_" + str[5:]
print(new_str)'''


