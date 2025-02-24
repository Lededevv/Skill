list_mov = {'00': '-','01': '-','02': '-',
            '10': '-','11': '-','12': '-',
            '20': '-','21': '-','22': '-'}
#Флаг "победителя"
winer = None
#Флаг хода
flag = 'x'

def simole_control(funct):

    """ Функция - декоратор принимает на вход функцию game_pole c двумя параметрами.

        Функция проверяет корректность данных передаваемых в параметрах и в случае
        отклонений выдает сообщение об ошибке. Если параметры соответствуют требованиям
        выполняется функция game_pole."""


    funct("00","-")
    def wrapper(xy_pole,signs):
        if list_mov.get(xy_pole) != "-" and list_mov.get(xy_pole)  is not None:
            print("Введите координаты свободного игрового поля")
            return list_mov
        if list_mov.get(xy_pole) != "-" and list_mov.get(xy_pole) is  None:
            print("Введите координаты в рамках игрового поля\n"
                  "Состоящие только из двух цифр")
            return list_mov
        else:
             return funct(xy_pole,signs)
    return wrapper

@simole_control
def game_pole(xy: str,sign: str):

    """Функция выводит игровое поле и фиксирует изменения словаре после выполнения успешного хода

     Функция принимает два параметра: ключа словаря и значение флага которое запишет
      по этому ключу в словарь"""

    global flag
    list_mov[xy] = sign
    # флаг хода на противоположный
    flag = "x" if sign == "o" else "o"
    #Выводим игровое поле
    line1 = "   0   1   2"
    line2 = f"0 {list_mov['00']}   {list_mov['01']}   {list_mov['02']}"
    line3 = f"1 {list_mov['10']}   {list_mov['11']}   {list_mov['12']}"
    line4 = f"2 {list_mov['20']}   {list_mov['21']}   {list_mov['22']}"
    print(line1+"\n",
          line2+'\n',
          line3+"\n",
          line4+'\n')
    return list_mov

def game_status(list_game: dict) -> str:

    """Функция проверят наличие выигрышные комбинации на игровом поле.

    При наступлении выигрышной комбинации возвращает флаг победившего хода."""

    if (list_game['00'] == list_game['01']
            and list_game['01'] == list_game['02']
            and list_game['00'] != "-"):
        return list_game['00']

    elif (list_game['10'] == list_game['11']
            and list_game['11'] == list_game['12']
            and list_game['10'] != "-"):
        return list_game['10']

    elif (list_game['20'] == list_game['21']
            and list_game['21'] == list_game['22']
            and list_game['20'] != "-"):
        return list_game['20']

    elif (list_game['00'] == list_game['10']
            and list_game['10'] == list_game['20']
            and list_game['00'] != "-"):
        return list_game['00']

    elif (list_game['01'] == list_game['11']
            and list_game['11'] == list_game['21']
            and list_game['01'] != "-"):
        return list_game['01']

    elif (list_game['02'] == list_game['12']
            and list_game['12'] == list_game['22']
            and list_game['02'] != "-"):
        return list_game['02']

    elif (list_game['00'] == list_game['11']
            and list_game['11'] == list_game['22']
            and list_game['00'] != "-"):
        return list_game['00']

    elif (list_game['20'] == list_game['11']
            and list_game['11'] == list_game['02']
            and list_game['02'] != "-"):
        return list_game['02']

# Цыкл действует пока game_status не вернет флаг победившего хода
while winer is None :
    if flag == "x":
        print("Ходят крестики : ")
    else:
        print("Ходят нолики : ")
    winer = game_status(game_pole(input(), flag))
    if winer == "o":
        print("Победа ноликов")
    elif winer == "x":
        print("Победа крестиков")
    # Если флага нет и нет места на поле выводим "ничья"
    elif  "-" not in list(list_mov.values()):
        print("Ничья")
        break

