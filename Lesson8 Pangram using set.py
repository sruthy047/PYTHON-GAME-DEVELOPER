alpha=set("abcdefghijklmnopqrstuvwxyz")

user_str=input("Enter a string ").lower()
if alpha.issubset(user_str):
    print(user_str+" is pangram")
else:
    print(user_str+" is not pangram")
