grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
srednya1 = sum(grades[0])/len(grades[0])
srednya2 = sum(grades[1])/len(grades[1])
srednya3 = sum(grades[2])/len(grades[2])
srednya4 = sum(grades[3])/len(grades[3])
srednya5 = sum(grades[4])/len(grades[4])
students_alpabeth = sorted(students)
spisok = {students_alpabeth[0]:srednya1,
          students_alpabeth[1]:srednya2,
          students_alpabeth[2]:srednya3,
          students_alpabeth[3]:srednya4,
          students_alpabeth[4]:srednya5}
print (spisok)