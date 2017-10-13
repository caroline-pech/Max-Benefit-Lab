# classes is a list of tuples [(g_1, b_1), (g_2, b_2), ... , (g_{n-1}, b_{n-1})] (see handout for definitions).
# T is some positive number.

def allocate_time(classes, T):
    ratio_dict = {}
    for i in classes:
        ratio = i[1]/i[0]
        if ratio not in ratio_dict:
            ratio_dict[ratio] = [i[0]]
        else:
            ratio_dict[ratio].append(i[0])
    keys = list(ratio_dict.keys())
    sorted_keys = sorted(keys)
    hours = 0
    real_hrs = 0
    benefit = 0
    i = len(sorted_keys) - 1
    while real_hrs < T:
        max_benefit = sorted_keys[i]
        temp_benefit = 0
        temp_hours = 0
        for j in ratio_dict[max_benefit]:
            temp_hours += j
        if temp_hours + real_hrs <= T:
            real_hrs += temp_hours
            temp_benefit += max_benefit * temp_hours
        elif temp_hours + real_hrs > T:
            temp_benefit += max_benefit * (T - real_hrs)
            real_hrs += (T - real_hrs)
        benefit += temp_benefit
        del ratio_dict[max_benefit]
        i -= 1
    return benefit

