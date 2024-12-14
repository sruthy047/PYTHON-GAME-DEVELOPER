dic={"NAME":"SAM","AGE":"18","PLACE":"Spain"}
print(dic)

k=input("Enter the key ").upper()
v=input("Enter the value ").upper()

dic[k]=v
print(dic)

#changing the dob
dic["PLACE"] = "UK"
print("Updated dic \n",dic)