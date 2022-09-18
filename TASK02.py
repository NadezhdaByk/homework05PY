# Создайте программу для игры в ""Крестики-нолики"".


dask = ['1', '2', '3', '4', '5', '6','7', '8', '9']
def print_dask(dask):
   for i in range(3):
      print(dask[0+i*3], dask[1+i*3], dask[2+i*3])
print_dask(dask)

def check_win(dask):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if dask[each[0]] == dask[each[1]] == dask[each[2]]:
          return dask[each[0]]
   return False

s = ''
count=1
for i in range(9):
    if i % 2 == 0:
        print('Ходит игрок 1')
        s = '0'
        j=int(input('введите номер ячейки куда поставить 0: '))
        dask[j-1]=s
        print_dask(dask)
        
        tmp = check_win(dask)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if count == 9:
            print("Ничья!")
            break
        count+=1
    else:
        print('Ходит игрок 2')
        s = 'X'
        j=int(input('введите номер ячейки куда поставить X: '))
        dask[j-1]=s
        print_dask(dask)
        tmp = check_win(dask)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if count == 9:
            print("Ничья!")
            break
        count+=1

