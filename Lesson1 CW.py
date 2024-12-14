dic={}
while True:
    print("1.Insert")
    print("2.Display all country name")
    print("3.Display all capital")
    print("4.Get capital")
    print("5.Delete")
    choice = int(input("Enter the choice : "))
    if choice == 1:
        country=input("Enter the country").upper()
        capital=input("Enter the capital").upper()
        dic[country]=capital
        print(dic)
    elif choice==2:
        print("\n Keys in dictionary")
        print(list(dic.keys()))
    elif choice==3:
        print("\n Values are ")
        print(list(dic.values()))
    elif choice == 4:
        country=input("Enter the country name: ").upper()
        print("\nCapital is ",dic[country])
    elif choice == 5:
        country=input("Enter the country name: ").upper()
        del dic[country]
        print("\n",dic[country])
    else:
        print("\nINVALID CHOICE")
        break

