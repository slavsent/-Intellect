from modul_7 import timing


@timing(0.000005)
def words_in_str(try_file):
    with open(try_file, "r", encoding='utf8') as my_file:
        i = 1
        for line in my_file:
            words = len(line.split(' '))
            print(f'Строка {i} слов {words}')
            i += 1


if __name__ == '__main__':
    words_in_str("text1.txt")
