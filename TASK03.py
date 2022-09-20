# Реализуйте RLE алгоритм: реализуйте модуль сжатия данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
#  
# RLE
# stroka = 'aaaaaaaaaabbbbbbbbbbbccccccccc'
# stroka = '10a12b9c'


with open('file.txt', 'r', encoding='utf-8') as file:
    arr = [str(i) for i in file.read()]

count=[]
counter=1
new_arr=[]
i=0
while len(arr)!=0:
   f=arr[0]
   new_arr.append(f)
   for j in range(1,len(arr)):
        if arr[j]==f:
            counter+=1
            
   count.append(counter)
   counter=1
   i+=1
   while f in arr:
       arr.remove(f)
 
print(count)
print(new_arr)
itog=[]
for i in range(len(count)):
    itog.append(str(count[i])+new_arr[i])
    
new_itog="".join(itog)
print(new_itog)

data=open('file3.txt', 'w', encoding='utf-8')
data.write(new_itog)
data.close()