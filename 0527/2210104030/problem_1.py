def get_prime(range_max=100):
    l = []
    for n in range(2, range_max + 1):
        flag = False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                flag = True
                break
        if not flag:
            l.append(n)
    return l


def calc_diff(set_a, set_b):
    sum_a = sum(set_a)
    sum_b = sum(set_b)
    return abs(sum_a - sum_b)


def solver(range_max=100):
    prime = get_prime(range_max)
    num_prime = len(prime)
    value_min = sum(prime) + 1

    for i in range(2 ** (num_prime - 1)):
        set_a = []
        set_b = []
        for j in range(num_prime):
            if (i >> j) & 1:
                set_b.append(prime[j])
            else:
                set_a.append(prime[j])
        if value_min < calc_diff(set_a, set_b):
            continue
        elif value_min > calc_diff(set_a, set_b):
            value_min = calc_diff(set_a, set_b)
            set_min = [(set_a, set_b)]
        elif value_min == calc_diff(set_a, set_b):
            set_min.append((set_a, set_b))
    return value_min, set_min


def main(print_full=False):
    '''Answer
    min: 0
    number of solution pairs: 51085
    example:
        set_a: {2, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 97}
        set_b: {7, 61, 67, 71, 73, 79, 83, 89}
    '''

    ans_value, ans_set = solver(100)
    if print_full:
        for s in ans_set:
            print(ans_value, s)
    else:
        print(ans_value, ans_set[0])
        print('...')
        print(ans_value, ans_set[-1])
    print(len(ans_set))


if __name__ == '__main__':
    main()
