#LIST OF STUDENT'S NAME
names=["ANKIT","UTKARSH","HIMANSHU","ADITYA"]

#LIST OF MARKS 
marks=[80,79,85,74]

print("marks before updation:",marks)
rank_before=dict(zip(names,marks))
a=dict(sorted(rank_before.items(),reverse=True, key=lambda item:item[1]))
before_updates=list(a)

#PRINTING THE LIST OF STUDENTS IN DESCENDING ORDER OF MARKS BEFORE UPDATION
print("list of students in order of marks before updates:",a)


#LIST OF UPDATES IN MARKS
updates=[1,6,-2,14]

updated_marks=[]
for i in range(0,len(marks)):
    updated_marks.append(marks[i]+updates[i])
print("updated marks are:",updated_marks)
rank_after=dict(zip(names,updated_marks))
x=dict(sorted(rank_after.items(),reverse=True, key=lambda item:item[1]))
updated_rank=list(x)

#PRINTING LIST OF STUDENTS IN DESCENDING ORDER OF MARKS AFTER UPDATION
print("list of sudents in order of marks after updates:",x)
max_marks=max(rank_after,key=rank_after.get)
B=before_updates.index(max_marks)
C=updated_rank.index(max_marks)
print("student with max marks:",max_marks,",","JUMP:",B-C)

