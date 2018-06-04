# Password Strength Calculator 
The script ```password_strength``` evaluates the user's password and gives an estimate from 1 to 10. 1 - very weak password, 10 - very strong password. Is taken into account: 


   - the use of both upper-case and lower-case letters (case sensitivity);
   - inclusion of one or more numerical digits;
   - inclusion of special characters, such as @, #, $;
   - prohibition of words found in a password blacklist;
   - prohibition of words found in the user's personal information;
   - prohibition of passwords that match the format of calendar dates.

There are bad passwords in the ```blacklist.txt```


# Quickstart 

The example of script launch on Linux, Python 3.5:
```
python3 password_strength.py 
```
On Windows you use similarly.

You can print data like this: 
```
Input your password: 
The bad password is 1, the good password is 10. Your password strength is  :  6

```

# Project Goals

The code is written for educational purposes. Training course for web-developers -
[DEVMAN.org](https://devman.org)