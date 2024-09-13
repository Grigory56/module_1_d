

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_=sorted(set(students))
student_s=[]
for i in range(len(grades)):
  student_s.append(sum(grades[i])/len(grades[i]))
sred_=dict(zip(list_,student_s))
print(sred_)