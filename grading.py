bangla=int(input("enter marks:"))
eng=int(input("enter marks:"))
math=int(input("enter marks:"))
religion=int(input("enter marks:"))
science=int(input("enter marks:"))
ict=int(input("enter marks:"))

total_marks=600

got_marks=bangla+eng+math+religion+science+ict
print(got_marks)
avg_mark=got_marks/6
if bangla and eng and math and religion and science and ict <=32:
    print("You are Failed")
else:

    if avg_mark>=80 and avg_mark<=100:
        print("you got A+")
    elif avg_mark>=70and avg_mark<=79:    
        print("You got A")
    elif avg_mark>=60and avg_mark<=69:    
        print("You got A-")
    elif avg_mark>=50and avg_mark<=59:    
        print("You got B")
    elif avg_mark>=40and avg_mark<=49:    
        print("You got C")
    elif avg_mark>=33and avg_mark<=39:    
        print("You got D")
    else:
        print("Invalid  input")    

    


