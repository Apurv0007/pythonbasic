sub1 = int(input("Enter 1st sub marks\n"))
sub2 = int(input("Enter 2st sub marks\n"))
sub3 = int(input("Enter 3st sub marks\n"))
if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
elif(sub1+sub2+sub3)/3<40:
    print("fail due to total percentage is less than 40")
    
else:
    print("You are pass")
    
    
    
    
    
    