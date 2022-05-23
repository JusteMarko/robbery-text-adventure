answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("""
you ar out with an expensive bag

you are wearing an expensive bag, so you are being robbed. Do you fight back . (Yes / No)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\nso you want to be tought? (Yes / No)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nthats a huge risk, it could be your last, and of coure you could maybe walk off with your bag.")

    elif ans2 in answer_no:
        print("\nyour not gonna play a hero? (yes/no)")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

elif ans1 in answer_no:
    print("\nyou are going to give the bag just like that, you are not going to fight? (Yes / No)\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\nSorry! your dead, he stabbed you, Game Over.")

    elif ans3 in answer_no:
        print("\nCongrats! you may now contiune your day safely")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

else:
    print("\nYou typed the wrong input. GOODBYE!")
