def get_hats(value):
    return float(value) - 0.5


def get_mod(value):
    return abs(value)


def get_min(r_min, r_max):
    if r_min <= 0 <= r_max:
        return 0
    else:
        return min(get_mod(r_min), get_mod(r_max))


def get_max(r_min, r_max):
    return max(get_mod(r_min), get_mod(r_max))


def lemma_1(d, i, query_hyperrec) -> bool:
    for j in range(0, d):
        if j == i:
            continue
        else:
            q_imin, _ = get_that_dim_bounds(i, query_hyperrec)
            q_jmin, q_jmax = get_that_dim_bounds(j, query_hyperrec)
            rhs = -1 * get_min(get_hats(q_jmin), get_hats(q_jmax))
            lhs = get_hats(q_imin)
            return lhs <= rhs


def get_that_dim_bounds(i, query_hyperrec):
    q_imin, q_imax = query_hyperrec[i]
    return q_imin, q_imax


def get_curve_same(q_hat_min, q_hat_max, i, j, d):
    if i >= d or j >= d:
        raise ValueError("Invalid Input!")
    if i == j:
        return q_hat_min, min(q_hat_max, 0)
    else:
        return q_hat_min, q_hat_max


def get_bar(i, j, q_hyper, d):
    if i == j:
        return None
    max_q_i_curve, min_q_i_curve = get_q_j_min_max_curve(d, i, i, q_hyper)
    max_q_j_curve, min_q_j_curve = get_q_j_min_max_curve(d, i, j, q_hyper)

    if min_q_j_curve >= min_q_i_curve:  # as per the proof body. Lemma 2 statement formula is incorrect
        return max(min_q_i_curve, min_q_j_curve)
    else:
        return min_q_i_curve


def get_q_j_min_max_curve(d, i, j, q_hyper):
    q_j_min, q_j_max = get_that_dim_bounds(j, q_hyper)
    q_j_curve_min, q_j_curve_max = get_curve_same(get_hats(q_j_min), get_hats(q_j_max), i, j, d)
    max_q_j_curve = get_max(q_j_curve_min, q_j_curve_max)
    min_q_j_curve = get_min(q_j_curve_min, q_j_curve_max)
    return max_q_j_curve, min_q_j_curve


def lemma_2(d, i, query_hyperrec):
    case1 = False
    max_q_i_curve, _ = get_q_j_min_max_curve(d, i, i, query_hyperrec)
    h_high = max_q_i_curve
    for j in range(0, d):
        q_jmin, q_jmax = get_that_dim_bounds(j, query_hyperrec)
        if get_hats(q_jmin) <= 0 <= get_hats(q_jmax):
            case1 = True
        else:
            case1 = False
    if case1:
        h_low = 0
        return h_low, h_high
    else:  # case2
        bars = []
        for j in range(0, d):
            q_j_bar = get_bar(i, j, query_hyperrec, d)
            if q_j_bar is not None:
                bars.append(q_j_bar)
        h_low = min(bars)
        return h_low, h_high


dim = 2
q_hyper_main = [[0.2, 0.3], [0.6, 0.9]]
for pyramid in [0, 1]:
    if lemma_1(dim, pyramid, q_hyper_main):
        print(f"p{pyramid}:", lemma_2(dim, pyramid, q_hyper_main))
