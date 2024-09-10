def convert_tweet(statement):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in statement:
        if char in vowels:
            new_char = char.replace(char, "")
            print(new_char, end="")
        else:
            final_output = print(f"{char}", end = "")
            
    


def main():
    tweet = input("Input: ")
    convert_tweet(tweet)
    print()


main()