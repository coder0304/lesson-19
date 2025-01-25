def squaredValues(beg,end):
    lst=[]

    for i in range(beg,end):
        lst.append(i**2)
    lst_even=[]
    lst_odd=[]

    for i in lst:
         if i% 2==0:
          lst_even.append(i)    
    else:
     lst_odd.append(i) 
    print("Heres a list of even squares within specified range",lst_even)
    print("Heres a list of odd squares within specified range",lst_odd)

beg=int(input("Enter starting range: "))
end=int(input("Enter end range: "))

squaredValues(beg,end)