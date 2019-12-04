# part 1
print(sum(sorted(s) == [*s] and len({*s}) < len(s)
          for s in [str(n) for n in range(357253, 892942)]))

# part 2
print(sum(sorted(s) == [*s] and 2 in [s.count(d) for d in {*s}]
          for s in [str(n) for n in range(357253, 892942)]))
