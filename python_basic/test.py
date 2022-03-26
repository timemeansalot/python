import numpy as np

def perm(a,left, right):
    if left==right:
        print(a)
    for i in range(left,right+1):
        a[left],a[i]=a[i],a[left]
        perm(a,left+1,right)
        a[left],a[i]=a[i],a[left]

# a=np.random.randint(1,100,4)
a=[106,24,29,787]
print(a,len(a))
perm(a,0,len(a)-1)
