import re
import os
import getpass


def load_data(file_path):
    with open(file_path, 'r') as file:
        return file.read().split('\n')


def get_added_data_from_file(text):
    work_file = input(text)
    if not os.path.exists(work_file):
        print('Файл не существует {}'.format(work_file))
        input_user_datum = input('Введите данные через пробел').split()
        print('=' * 100)
    else:
        input_user_datum = load_data(work_file)

    return input_user_datum


def is_password_long(password):
    return len(password) >= 6


def has_both_upper_and_lower_cases(password):
    return not password.islower() and not password.isupper()


def has_numbers(password):
    return password.isdigit()


def has_special_characters(password):
    return bool(re.search(r'[ !#$%&():*+,-./[\\\]^_`{|}~]', password))


def has_forbidden_words(password, forbidden_words):
    pattern_dd_mm_yyyy = \
        '(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d'
    pattern_mm_dd_yyyy = \
        '(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d'
    has_forbidden_words = bool(re.search(pattern_dd_mm_yyyy, password))
    has_forbidden_words = bool(re.search(pattern_mm_dd_yyyy, password))

    if password in forbidden_words:
        has_forbidden_words = True

    return has_forbidden_words


def check_password_strength(password, forbidden_words):
    strength = 0
    if is_password_long(password):
        strength += 3
    if has_both_upper_and_lower_cases(password):
        strength += 2
    if has_numbers(password):
        strength += 3
    if has_special_characters(password):
        strength += 2
    if has_forbidden_words(password, forbidden_words):
        strength /= 2

    return strength

if __name__ == '__main__':
    password = getpass.getpass('Введите пароль')

    blacklist = get_added_data_from_file('Введите имя файла чёрного списка:')
    personal_info = get_added_data_from_file(
        'Введите имя файла с персональной информацией:')
    company_name = get_added_data_from_file(
        'Введите имя файла с полным и кратким названием компании:')
    forbidden_words = blacklist + personal_info + company_name

    password_strength = check_password_strength(
        password, forbidden_words)
print('Оценка сложности пароля:   {}'.format(password_strength))
