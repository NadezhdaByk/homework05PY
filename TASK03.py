# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
#  
# RLE
# stroka = 'aaaaaaaaaabbbbbbbbbbbccccccccc'
# stroka = '10a12b9c'


with open('file.txt', 'r+', encoding='utf-8') as file:
    arr = [str(i) for i in file.read()]

count=[]
counter=0
new_arr=[]
i=0
while arr!=0:
   f=arr[0]
   new_arr.append(f)
   for j in range(len(arr)):
        if arr[j]==f:
            counter+=1
            
   count.append(counter)
   counter=0
   i+=1
   while f in arr:
       arr.remove(f)
 
print(count)
print(new_arr)
itog=[]
for i in range(len(count)):
    itog.append(str(count[i])+new_arr[i])
    

print("".join(itog))