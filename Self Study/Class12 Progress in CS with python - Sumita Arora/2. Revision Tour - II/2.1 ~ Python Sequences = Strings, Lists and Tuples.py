#Using Visual Studio Code
#Main User using Git Service with GitHub
#Made on apr 16 16:04:52 2022


#%%
#Q2 :
str1="nectarine"
o1,o2,o3,o4=str1[0],str1[2:4],str1[-4],str1[-2]
print(o1+o2+o3+o4)
str2="blueberry"
p1,p2,p3=str2[0:2],str2[4],str2[6:9]
print(p1+p2+p3)

#%%
#Q3 :
istr,vl5,ostr1 = input("Enter String "),['a','e','i','o','u'],''
for s in istr:
    if s in vl5:
        ostr1 +='({})'.format(s)
    else:
        ostr1 +=s
print(ostr1)

#%%
#Q7 :
istr1 = input("Enter list elements space separated : ")
ilt = list(map(int ,istr1.split()))
del ilt[0]
print(ilt)
#%%
#Q9 :
tpi1 = (1, 2, 3)
tpi2 = (4, 5, 6)
tpi3 = tpi1 +  tpi2
print(tpi3)
#%%
#Q10 :
yu1 = [3, 4, 1, 5, 8, 2]
yu1.sort()
print("Output using inbuilt function : {}".format(yu1))
#%%
#Q11 :
#method_1
tyj = (3, 4, 1, 5, 8, 2)
loku = list(tyj)
ui = len(loku)
for h1 in range(ui):
    for h2 in range(ui):   
        if(loku[h1]<loku[h2]):
            temp = loku[h1]
            loku[h1] = loku[h2]
            loku[h2] = temp
tyj = tuple(loku)
print("Output of tuple to list approach : {}".format(tyj))
#%%
#Q12 :
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
row = len(a)
col = len(a[0])
n = row*col//2
count = 0
for r in range(row):
    for c in range(col):
        if count<=n:
            temp = a[r][c]
            a[r][c] = a[row-1-r][col-1-c]
            a[row-1-r][col-1-c] = temp
            count+=1 
for i in  range(row) :  
    for j in range(col) : 
        print(a[i][j],end= ' '); 
    print(); 




#Project Completed at apr 16 17:48:46 2022
#Project Completed with Visual Studio Code
#Support Visual Studio Code