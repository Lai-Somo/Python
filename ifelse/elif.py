gender = input("Please enter your gender: ")
if gender != "male" and gender != "female":
    print("Invalid gender")
    print("Sorry, please try again")
elif gender == "male":
    print("Join the blue team")
else:
    print("Join the pink team")