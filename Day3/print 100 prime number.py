num=2
count=0
print("100 Numbers of prime mumber are")
while count <=100:
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
            count +=1
    num +=1
    
            
                