def shatrangi():
    m = int(input("Row: \n"))
    n = int(input("Col: \n"))
    for i in range (m):
        if i % 2 == 0:
            for j in range (n):
                if j %2 ==0:
                    print ("🟩",end = " ")
                else:
                    print ("🟨",end = " ")
            print ("\n")
            
        else:
            for j in range (n):
                if j %2 ==0:
                    print ("🟨",end = " ")
                else:
                    print ("🟩",end = " ")
            print ("\n")
        
shatrangi ()