import export_1
import export_2
import import1
import inter_data
import view
import data


data.init()



def menu():
    print('Введите цифру с необходимым действием')
    print('[0] Ввести данные в базу вручную: ')
    print('[1] Ввести данные в базу (экспорт_1): ')
    print('[2] Ввести данные в базу (экспорт_2): ')
    print('[3] Показать данные: ')
    print('[4] Импортировать данные: ')
    print('[5] Выход: ')

result=111

while result != 5:
    menu()
    result = int(input())
    if result == 0:
       inter_data.interdata()
    elif result == 1:
        export_1.export_1_data()
    elif result == 2:
        export_2.export_2_data()
    elif result == 3:
        view.view_data()
    elif result == 4:
        import1.import_data()

print('ВЫХОДИМ')
