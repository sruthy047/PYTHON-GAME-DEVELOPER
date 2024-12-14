dic={"NAME":"SAM","AGE":"18","PLACE":"Spain"}
print(dic)
while True:
    
    print("1.Insert")
    print("2.Display all keys")
    print("3.Display all values")
    print("4.Get a value")
    print("4.Update a value")
    print("5.Delete")
    choice = int(input("Enter the choice : "))
    if choice == 1:
        k=input("Enter the key ").upper()
        v=input("Enter the value ").upper()
        dic[k]=v
        print(dic)
        print("\n")
    elif choice==2:
        print("\n Keys in dictionary")
        print(list(dic.keys()))
        print("\n")
    elif choice==3:
        print("\n Values are ")
        print(list(dic.values()))
        print("\n")
    elif choice == 4:
        k=input("Enter the key: ").upper()
        print("\nValue is ",dic[k])
        print("\n")
    elif choice ==5:
        k=input("Enter the key: ").upper()
        v=input("Enter the new value: ").upper()
        print("Updated dictionary is \n",dic)
        print("\n")
    elif choice == 6:
        k=input("Enter the key: ").upper()
        del dic[k]
        print("\n",dic)
    else:
        print("\nINVALID CHOICE")
        break




dic[k]=v
print(dic)

#changing the dob
dic["PLACE"] = "UK"
print("Updated dic \n",dic)