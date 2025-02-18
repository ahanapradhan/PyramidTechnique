def get_j_max(d, v, j):
    for k in range(0, d):
        if k == j:
            continue
        else:
            if abs(0.5 - v[j]) >= abs(0.5 - v[k]):
                return j
    return None


def which_pyramid(d, v):
    for j in range(0, d):
        j_max = get_j_max(d, v, j)
        if j_max is None:
            # raise ValueError("Some problem!")
            continue
        if v[j_max] < 0.5:
            return j_max
        else:
            return j_max + d


dimensions = 2
points = [[0.1, 0.2], [0.5, 0.4], [0.2, 0.6], [0.8, 0.9], [0.6, 0.6]]
for p in points:
    i = which_pyramid(dimensions, p)
    print(f"point {p} is in Pyramid p{i}")
