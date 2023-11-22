import re


def email_in_str(try_file):
    with open(try_file, "r", encoding='utf8') as my_file:
        words = []

        for line in my_file:
            words += line.split(' ')

        reg_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        for word in words:
            if re.fullmatch(reg_email, word):
                yield word


if __name__ == '__main__':
    for el in email_in_str("text_email.txt"):
        print(el)
