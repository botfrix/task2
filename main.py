import time


def main():
    min_barrier = int(input('Enter minimal barrier (l): '))
    max_barrier = int(input('Enter maximum barrier (r): '))
    start_time = time.time()
    if min_barrier <= max_barrier:
        all_roots = []
        for i in range(min_barrier, max_barrier + 1):
            min_range_dgt = -100000 + i
            max_range_dgt = 100000
            interval = [max_range_dgt, min_range_dgt]
            while interval[1] != max_range_dgt:
                current_roots = equal_calc(interval[0], interval[1])
                if current_roots is not None:
                    all_roots.append(current_roots)
                interval[0] -= 1
                interval[1] += 1
        if len(all_roots) > 200000:
            print(-1)
        else:
            print(f'All roots: {all_roots}\nNumber of roots: {len(all_roots)}')
        print(f'Lead time: {time.time() - start_time} seconds')
    else:
        print("min_barrier > max_barrier")


def equal_calc(b_coef, c_coef):
    discriminant = b_coef ** 2 - 4 * c_coef
    roots = [0, 0]
    if discriminant > 0:
        roots[0] = (-b_coef + discriminant ** 0.5) / 2
        roots[1] = (-b_coef - discriminant ** 0.5) / 2
        if roots[0] % 1 == 0 and roots[1] % 1 == 0:
            return roots
    else:
        return None


if __name__ == "__main__":
    main()
