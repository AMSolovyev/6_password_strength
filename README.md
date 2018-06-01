# Password Strength Calculator 
The script ```password_strength``` evaluates the user's password and gives an estimate from 1 to 10. 1 - very weak password, 10 - very strong password. Is taken into account: 


   - the use of both upper-case and lower-case letters (case sensitivity);
   - inclusion of one or more numerical digits;
   - inclusion of special characters, such as @, #, $;
   - prohibition of words found in a password blacklist;
   - prohibition of words found in the user's personal information;
   - prohibition of passwords that match the format of calendar dates.


# Quickstart 

The example of script launch on Linux, Python 3.5:
```
python3 password_strength.py 
```
On Windows you use similarly.

You can print data like this: 
```
Введите пароль123456@
Введите имя файла чёрного списка:black.txt
Введите имя файла с персональной информацией:g
Файл не существует g
Введите данные через пробел
====================================================================================================
Введите имя файла с полным и кратким названием компании:
Файл не существует 
Введите данные через пробел
====================================================================================================
Оценка сложности пароля:   5
```

# Project Goals

The code is written for educational purposes. Training course for web-developers -
[DEVMAN.org](https://devman.org)