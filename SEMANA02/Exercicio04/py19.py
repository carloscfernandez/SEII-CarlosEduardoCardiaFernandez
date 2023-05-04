#li = [9,1,8,2,7,3,6,4,5]

#s_li=sorted(li, reverse=True)
#print('Sorted Veriable:\t', s_li)

#li.sort()
#print('Original Veriable:\t', li)

tup=(9,1,8,2,7,3,6,4,5)
s_tup=sorted(tup)
print('Tuple\t', s_tup)

li = [-6,-5,-4,1,2,3]
s_li=sorted(li, key=abs)
print(s_li)
