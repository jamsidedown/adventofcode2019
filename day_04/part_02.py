def match(ns: str) -> bool:
    return sorted(ns) == [*ns] and 2 in [ns.count(d) for d in {*ns}]


if __name__ == '__main__':
    min, max = 357253, 892942
    matches = sum(match(str(n)) for n in range(min, max + 1))
    print(f'different passwords: {matches}')
