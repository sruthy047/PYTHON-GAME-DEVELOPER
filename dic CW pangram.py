sent = input("Enter a string").lower()
alphacount={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
for c in sent:
    if c.isalpha():
        if c in alphacount:
            alphacount[c] += 1
        
print(alphacount)
pangram ="True"
for val in alphacount.values():
    if val==0:
        pangram="False"
if pangram=="True":
    print("Entered text is pangram")
else:
    print("Entered text is not pangram")

