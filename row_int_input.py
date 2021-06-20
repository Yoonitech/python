wi=input()   #row input :/1 2 3 55 106
list_wi=[]
l=len(wi)
k=-1
for i in range(0,l):
    if i > k and wi[i] != ' ' :
        sum = int(wi[i])
        t=1
        if  i+t != l :
            while wi[i+t] != ' ' :
                
                if  i+t != l :
                    sum = (sum*10) + int(wi[i+t])
                k=t+i
             
                if i+t+1 != l :
                    t=t+1
                else:
                    break    
                        
                
        list_wi.append(sum)
print(list_wi)   #list output :/['1','2','3','55','106']     
