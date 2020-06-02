n=int(input("Enter N\n"))
###########################################3
turn=1
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	print(" "*(n-i),end='')
	print("*"*(2*i-1),end='')
	print()
for i in range(1,n+1):
	print(" "*(n-2),end='')
	print("*"*3,end='')
	print()
#############################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,i+1):
		if i==j or j==1 or i==n:
			print(j,end='')
		else:
			print(" ",end='')
	print()
##############################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,2*n):
		if i+j==n+1:
			print("1",end='')
		elif j-i==n-1:
			print(i,end='')
		elif i==n and j%2==1:
			print(((i+j)//2)%10,end='')
		else:
			print(" ",end='')
	print()

#################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,2*n):
	for j in range(1,(i)+1,1):
		if j==1:
			print('*',end='  ')
		else:
			print(j-1,end='  ')
	for j in range(i-1,0,-1):
		if j==1:
			print('*',end='  ')
		else:
			print(j-1,end='  ')
			
	print()
for i in range(2*n-2,1,-1):
	for j in range(1,(i)+1,1):
		if j==1:
			print('*',end='  ')
		else:
			print(j-1,end='  ')
	for j in range(i-1,0,-1):
		if j==1:
			print('*',end='  ')
		else:
			print(j-1,end='  ')
			
	print()
##################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
        print("  "*(n-i)*2+"* "*(i))
for i in range(1,n):
        print("  "*(i)*2+"* "*(n-i))
        
##################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,2*n+1):
		if i+j==n+1 or i==j:
			print("*",end='')
		else:
			print(" ",end='')
	print()
###################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,2*n+1):
		if (i==1 and j<n)or(j==n) or (i==n and j>n):
			print("*",end=' ')
		else:
			print(" ",end=' ')
	print()

####################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,n+1):
		if i+j==n+1 or i==1 or i==n:
			print("*",end=' ')
		else:
			print(" ",end=' ')
	print()
#####################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,n+1):
		if i==1:
			print(j,end=' ')
		elif i==n:
			print(n-j,end=' ')
		elif j==1:
			print(i,end=' ')
		elif j==n:
			print(n-i,end=' ')
		else:
			print(" ",end=' ')
	print()

#####################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	print(" "*(n-i),end='')
	print("10"*i)
#####################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n*2):
	for j in range(1,n+1):
		if j==1 or i+j==n+1 or i-j==n-1:
			print('*',end=' ')
		else:
			print(" ",end=' ')
	print()
######################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,n+1):
		if (i==n//2+1) or(i<n//2+1 and j==1) or(i>n//2+1 and j==n)or(j==n//2+1)or(i==n and j<n//2+1) or(i==1 and j>n//2+1):
			print('*',end=' ')
		else:
			print(" ",end=' ')
	print()
####################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(i,0,-1):
		print(2**(j-1),end=' ')
	print()
####################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for  i in range(0,n):
	for  j in range(0,i):
		print(2**j,end='  ')
	for j in range(i-2,-1,-1):
		print(2**j,end='  ')
	print()
###################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
k=0
for i in range(1,n+1):
        for j in range(0,2*i-1):
                k+=1
                print(k,end='')
        print()
##################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
k=0
for i in range(1,n+1):
        s=''
        for j in range(i-1,-1,-1):
                k+=1
                l=str(k)
                s+=' '+l[::-1]
        print(s[::-1])
######################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=' ')
	for k in range(i-1,0,-1):
		print(k,end=' ')
	print()
########################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
        for j in range(n,i-1,-1):
                print(j,end='')
        print(' '*(2*(i-1)),end='')
        for j in range(i,n+1):
                print(j,end='')
        print()
########################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	for j in range(1,i+1):
		print(i,end='')
	for k in range(i+1,n+1):
		print(k,end='')
	print()
########################################################



                
########################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
	print('*'*(n-i+1)+'-'*(2*i)+'*'*(n-i+1))
########################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
k=ord('A')-1
for i in range(1,n+1):
        for j in range(1,i):
                k+=1
                print(chr(k),end='')
        print()
	
########################################################
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
x='Python'
for i in range(1,len(x)+1):
	print(x[0:i])
########################################################
x=[0,1,0]
print(f"\n\nPattern number : {turn}",end="\n\n\n\n")
turn+=1
for i in range(1,n+1):
        for j in range(1,len(x)-1):
                print(x[j],end=' ')
        print()
        i=0
        k=[0]
        while i!=len(x)-1:       
                 k.append(x[i]+x[i+1])
                 i+=1
        k.append(0)
        x=k
     #   print(k)
########################################################
