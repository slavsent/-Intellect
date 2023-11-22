def no_chet_str():
    end_str = ''
    for i in range(1, 100, 2):
        end_str += str(i)
    return end_str


if __name__ == '__main__':
    my_str = no_chet_str()
    print(my_str)
    my_str = ''.join(['' + str(i) for i in range(1, 100, 2)])
    print(my_str)
