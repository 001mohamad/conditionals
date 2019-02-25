marks=[]
passed=[]
fail=[]

s1=int(input("what did you score?"))
marks.append(s1)

s2=int(input("what did you score?"))
marks.append(s2)

s3=int(input("what did you score?"))
marks.append(s3)

s4=int(input("what did you score?"))
marks.append(s4)

s5=int(input("what did you score?"))
marks.append(s5)

s6=int(input("what did you score?"))
marks.append(s6)

s7=int(input("what did you score?"))
marks.append(s7)

s8=int(input("what did you score?"))
marks.append(s8)

s9=int(input("what did you score?"))
marks.append(s9)

s10=int(input("what did you score?"))
marks.append(s10)

#print(marks)

for mark in marks:
    if mark>50:
        passed.append(mark)
    else:
        fail.append(mark)
"""        
print(passed)
print(fail)
"""

list_which_failed=int(len(fail))
list_which_passed=int(len(passed))
"""
print()
print(list_which_passed)"""

print("The list of students who failed is " + list_which_failed)
print("The list of students who passed is " + list_which_passed)