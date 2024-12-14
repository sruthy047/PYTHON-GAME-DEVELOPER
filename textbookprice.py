textbook={"ENGLISH":200,"MATHEMATICS":350,"PHYSICS":250,"CHEMISTRY":200,"CS":200}
print(textbook)
print("\n Updating price of Physics book")
textbook["PHYSICS"]=280
print("\n Updated values")
print(textbook)
textbook["French"]=180
textbook["BIOLOGY"]=300
print("\n",textbook)
print("\n Book names \n",textbook.keys())
print("\n Price of books \n",textbook.values())
print("\n ",textbook)