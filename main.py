import time


def main():
    min_barrier = int(input())
    max_barrier = int(input())
    start_time = time.time()
    if min_barrier <= max_barrier:
        all_roots = []
        for i in range(min_barrier, max_barrier + 1):
            max_range_dgt = 100000
            min_range_dgt = -100000 + i
            interval = [max_range_dgt, min_range_dgt]
            while interval[1] != max_range_dgt:
                current_discriminant = discriminant_calc(interval[0], interval[1])
                if current_discriminant is not None:
                    all_roots.append(current_discriminant)
                interval[0] -= 1
                interval[1] += 1
        print(len(all_roots))
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("min_barrier > max_barrier")


def discriminant_calc(b_coef, c_coef):
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