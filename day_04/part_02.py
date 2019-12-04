def passes_criteria(n: int) -> bool:
    ns = str(n)

    for i in range(len(ns) - 1):
        if ns[i] > ns[i + 1]:
            return False

    for d in set(ns):
        if ns.count(d) == 2:
            return True

    return False


if __name__ == '__main__':
    min = 357253
    max = 892942

    pass_count = sum(1 for i in range(min, max + 1) if passes_criteria(i))

    print(f'different passwords: {pass_count}')
