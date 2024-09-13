def check_fruit(s):
    fruit_list = {"apple":"130", "avocado":"50", "kiwifruit":"90", "pear":"100", "sweet cherries":"100"}
    if s in fruit_list:
        print(f"Calories: {fruit_list[s]}")
    else:
        pass


def main():
    user_fruit = input("Item: ").lower()
    check_fruit(user_fruit)


main()