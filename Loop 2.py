total = 0 # sum of scores
count = 0 # number of scores entered

# get one score & convert string to integer
score = int(input("Enter score, (Enter -9 to end): ") )
if score ==-9:
    print("Least enter a one value")
else:
    
    

# Add while loop here. Loop while score is not -9
    while score != -9:
        total=total+score # Add score to total
        count=count+1 # Keep a count of scores
        
        
# Get next score input
        score = int(input("Enter score, (Enter -9 to end): ") )

# print average of scores entered
    average = float( total ) / count
    print("Class average is", average)
