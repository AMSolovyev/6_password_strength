import getpass
from string import punctuation


def is_password_in_blacklist(file_path='blacklist.txt'):
    try:
        with open(file_path, 'r') as file_handler:
            return file_handler.read().split('\n')
    except FileNotFoundError:
        return None


def get_passwords_rating(password, password_rating, min_password_len):
    if any(char in punctuation for char in password):
        password_rating += 1
    if len(password) >= min_password_len:
        password_rating += 2
    if len(password) == max_password_len:
        password_rating += 2
    if any(char.isupper() for char in password):
        password_rating += 2
    if any(char.islower() for char in password):
        password_rating += 2
    if any(char.isdigit() for char in password):
        password_rating += 2
    if password in blacklist:
        password_rating /= 2
    return password_rating


def print_password_strength(password_strength, password_rating):
    print(password_strength, password_rating)


def get_password():
    password = getpass.getpass('Input your password: ')
    return password


if __name__ == "__main__":
    password_rating = 0
    min_password_len = 6
    max_password_len = 10
    password = get_password()
    blacklist = is_password_in_blacklist()
    password_rating = get_passwords_rating(
        password, password_rating, min_password_len)
print_password_strength(
    'The bad password is 1, the good password is 10.'
    ' Your password strength is  : ', password_rating)
