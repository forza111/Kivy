import json
class AdressBook():
    filename = 'adressbook.json'
    spisok = {}

    @classmethod
    def first_start(cls,name,info):
        AdressBook.spisok[name] = info
        AdressBook.DumpFile()

    @classmethod
    def append(cls,name,info):
        '''Добавление контакта в словарь или изменение существующего контакта'''
        AdressBook.LoadFile()
        if AdressBook.spisok.get(name):
            print('Данные контакта {} изменены и занесены в адресную книгу.'.format(name))
        else:
            print('Контакт {} занесен в адресную книгу.'.format(name))
        AdressBook.spisok[name] = info
        AdressBook.DumpFile()


    @classmethod
    def change(cls,name):
        '''Изменение существующего контакта'''
        AdressBook.LoadFile()
        if AdressBook.spisok.get(name):
            info = input('Введите новую информацию о контакте {}'.format(name))
            AdressBook.append(name,info)
        else:
            AdressBook.view_information(name)

    @classmethod
    def view_information(cls,name):
        '''Возвращает ключ - значение из словаря'''
        AdressBook.LoadFile()
        if AdressBook.spisok.get(name):
            print('{} : {}'.format(name,AdressBook.spisok[name]))
        else:
            answer = input('Такого контакта не существует, желаете добавить данный контакт в адресную книгу?\nY \ N')
            if answer.upper() == 'Y':
                info = input('Введите информацию о контакте {}'.format(name))
                AdressBook.append(name,info)

            elif answer.upper() == 'N':
                print('Всего доброго')
            else:
                print('Вы ввели некорректный ответ')
                AdressBook.view_information(name)

    @classmethod
    def DelKey(cls, name):
        '''Удаляет пару ключ - значение из словаря'''
        AdressBook.LoadFile()
        if AdressBook.spisok.get(name):
            print('Контакт {} : {} успешно удален из адресной книги'.format(name, AdressBook.spisok.pop(name)))
        else:
            print('Такого контакта не существует, попробуйте еще раз')
            AdressBook.DelKey(input('Введи имя контакта, от которого вы хотите изюавиться'))
        AdressBook.DumpFile()


    @classmethod
    def DumpFile(cls):
        '''Функция сохраняет в фаил Json словарь'''
        with open(AdressBook.filename,'w') as f:
            json.dump(AdressBook.spisok,f)
    @classmethod
    def LoadFile(cls):
        '''Функция загружает из json фаила в словарь'''
        with open(AdressBook.filename, 'r') as f:
            AdressBook.spisok = json.load(f)



#AdressBook.DelKey('kak')
#AdressBook.view_information('FORZA11fffk1')
#AdressBook.append('nlolojdn9999fgfgj',8787889)
#AdressBook.first_start('kak',8899988)
#AdressBook.change('forzaedefvdfvde')
