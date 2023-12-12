from itertools import permutations

list_a = [1,3,5]
list_b = [2,4,6]

list_c = permutations(list_a)
list_d = permutations(list_b)
avg = 0
ind =0

for iter in list_c:
    list_d = permutations(list_b)
    for iter2 in list_d:
        print(ind)
        hasil = iter[0]+iter2[0] + iter[1]+iter2[1] + iter[2]+iter2[2]
        print(f"==>> hasil: {hasil}")
        avg += hasil
        ind+=1
# for iter in list_c:
#     hasil = list_a[0]* list_b[0] + list_a[1]* list_b[1] + list_a[2]* list_b[2]
#     avg += hasil


print(avg/36)




