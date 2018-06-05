import getpass
from string import punctuation


def load_blacklist(file_path='blacklist.txt'):
    try:
        with open(file_path, 'r') as file_handler:
            return file_handler.read().split('\n')
    except FileNotFoundError:
        return None


def get_rating(password, blacklist):
    max_password_len = 6
    password_rating = 0
    if len(password) >= max_password_len:
        password_rating += 2
    if any(char in punctuation for char in password):
        password_rating += 2
    if any(char.isupper() and char.islower() for char in password):
        password_rating += 3
    if any(char.isdigit() for char in password):
        password_rating += 3
    if password in blacklist:
        password_rating /= 2
    return password_rating


def print_password_strength(password_strength, password_rating):
    print(password_strength, password_rating)


def get_password():
    password = getpass.getpass('Input your password: ')
    return password


if __name__ == '__main__':
    password = get_password()
    blacklist = load_blacklist()
    password_rating = get_rating(password, blacklist)
    print_password_strength(
        'The bad password is 1,\n'
        'the good password is 10.\n'
        'Your password strength is: ',
        password_rating)
