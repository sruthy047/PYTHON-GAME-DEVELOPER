comp_record=[]
for i in range(5):
    print("Enter the details for Group{} ".format(i+1))
    group_name=input("Enter the group name: ")
    size=int(input("Size of group "))
    date=input("Enter the date of competition")
    venue=input("Venue- ")
    medal=input("Medal type")
    group_record=(group_name,size,date,venue,medal)
    comp_record.append(group_record)

for i in comp_record:
    print("Group name : {}, Size: {} ,Date: {},medal= {}".format(i[0],i[1],i[2],i[3],i[4]))