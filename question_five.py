def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))