import math as mt

#treinamento de lambda

#to_alternating_case = lambda string: string.swapcase()

#merge_arrays=lambda a,b:sorted({*(a+b)})

#lista = merge_arrays([1,2,3], [0,2,4])


#test = lambda x: [ int(x[i] **(1/2)) for i in range(len(x))]

square_or_square_root=lambda arr: [e**(1/2) if e**(1/2)%1==0 else e**2 for e in arr ]

# [2, 9, 3, 49, 4, 1]
lista = [4, 3, 9, 7, 2, 1]

print(square_or_square_root(lista))

#print(int(4**(1/2)))