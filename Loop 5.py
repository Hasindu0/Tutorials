for number in range(3) :
    print("-------------------------------------------")
    print("Outer loop iteration " + str(number))
 # Inner loop
    for another_number in range(4):
        print("****************************")
        print("In inner loop iteration " + str(another_number))
print()
print("#####################################################")
print()
r=1
for x in range(1,4): # print 3 rows
    r+=1
    for y in range(1,r): # 3 asterisks a row
        print('*', end='')
    print() 
