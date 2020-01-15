def string_to_ascii(text):
    code = ''.join(str(ord(c)) for c in text)
    print(code)
    k=0
    for i in range(2,int(code)//2+1):
    	if(int(code)%i==0):
    		k=k+1
    if(k<=0):
    	print("Ο αριθμός είναι πρώτος")
    else:
    	print("Ο αριθμός δεν είναι πρώτος")


text = input("Γράψτε ένα string: ")
string_to_ascii(text)
