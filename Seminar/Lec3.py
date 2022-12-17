#1.
# path='/Users/maksimkutlaev/Desktop/GeekBrains/Python/Seminar/Lec4.txt'
# f=open(path, 'r')
# data=f.read()+' '
# f.close()
# numbers=[]

# while data !='':
#     space_pos=data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data=data[space_pos+1:]

# out=[]

# for i in numbers:
#         if not i%2:
#             out.append((i,i**2))
# print(out)

#2.
# def select(f,col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data ='1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x,x**2), res)
# print(res)


#3.
# li=[x for x in range(1,20)]

# li=list(map(lambda x: x+10, li))

# print(li)

#4.
data ='1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x,x**2), res))
print(res)

#5
# data=[x for x in range(10)]
# res=list(filter(lambda x: not x%2, data))
# print(res)