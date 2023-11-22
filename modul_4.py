def revers(try_str):
    return ''.join(reversed(try_str))


def is_palindrome(try_str):
    revs_str = revers(try_str)

    # проверка на совпадение 2х строк
    if try_str == revs_str:
        return True
    return False


if __name__ == '__main__':
    begin_str = 'dsgdshfgjetyeghdf'
    print(revers(begin_str))
    print(is_palindrome(begin_str))
