# Q1
liste = [1, 2, 3, 4, 5]
liste = [i*2 for i in liste]

print(liste)

#Q2
liste2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste2 = [i*2 for i in liste2 if i>0]

print(liste2)

#Q3
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste = [i*2 if i>0 else i*3 for i in liste]

print(liste)

#Q4
liste = [(i,j) for i in range(10) for j in range(2)]
print(liste)