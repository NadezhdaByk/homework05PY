# Реализуйте RLE алгоритм: реализуйте модуль восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file1.txt', 'r', encoding='utf-8') as file:
    arr = [str(i) for i in file.read()]
print(arr)
for i in range(0, len(arr), 2):
    arr[i]=int(arr[i])
print(arr)
new=[]

for i in range(0, len(arr)-1,2):
    new.append(arr[i+1]*arr[i])
print(new)
arr_new="".join(new)

data=open('file2.txt', 'w', encoding='utf-8')
data.write(arr_new)
data.close()