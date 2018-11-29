mylist = [1,2,3,4,5,6,7,8,9,0]
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd:', num)
sum = 0        
for num in mylist:
    sum = num + sum
    print(sum)