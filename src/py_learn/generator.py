numbers = [1, 2, 43, 5, 6]


def my_generator(numbers):
    for ele in numbers:
        yield ele


def test_generator(numbers):
    # 第一种，用生成器方式
    for ele in my_generator(numbers):
        print(ele)


big_list = range(1000000)
for even_num in big_list:
    if even_num % 2 == 0:
        print(even_num)
