import re
import sys


def check_both_case_letters(password):
    letters = set(password)

    lower = any(letter.islower() for letter in letters)
    upper = any(letter.isupper() for letter in letters)

    return lower and upper


def check_inclusion_numerical_digits(password):
    set_of_numerical_digits = {str(digit) for digit in range(10)}
    set_password = set(password)
    return not set_of_numerical_digits.isdisjoint(set_password)


def check_inclusion_spec_characters(password):
    set_spec_characters = {'@', '#', '$'}
    set_password = set(password)
    return not set_spec_characters.isdisjoint(set_password)


def check_use_forbidden_words(password):
    file_forbidden_words = './forbidden_words.txt'
    with open(file_forbidden_words, 'r') as file_contents:
        set_forbidden_words = set(file_contents.read().splitlines())

    set_password = {password}
    return set_forbidden_words.isdisjoint(set_password)


def check_use_personal_info(password):
    set_personal_information = {'aleksey', 'aleksei'}
    set_password = {password}
    return set_personal_information.isdisjoint(set_password)


def check_use_corp_info(password):
    set_corp_info = {'yandex', 'ya'}
    set_password = {password}
    return set_corp_info.isdisjoint(set_password)


def check_use_commonly_used_formats(password):
    return not bool(re.search('\d{4,}', password))


def get_password_strength(password):
    list_checking_functions = [
        check_both_case_letters,
        check_inclusion_numerical_digits,
        check_inclusion_spec_characters,
        check_use_forbidden_words,
        check_use_personal_info
    ]
    list_additional_checking_functions = [
        check_use_corp_info,
        check_use_commonly_used_formats
    ]
    rating = 0
    for func in list_checking_functions:
        if func(password):
            rating += 2
    for func in list_additional_checking_functions:
        if not func(password):
            rating -= 2
    return rating


if __name__ == '__main__':
    user_password = input("Введите пароль: ")
    if user_password:
        print('Оценка пароля:', get_password_strength(user_password))
    else:
        print('Вы не ввели пароль')
    # user_password = str(sys.argv[1])
