def find_cf_combo(input):
    for entry in input:
        if len(entry) == 2:
            return entry


def initial_uniqual_val_analysis(input):
    solution = dict()
    cf_combo = find_cf_combo(input)
    solution['c'] = cf_combo
    solution['f'] = cf_combo

    for entry in input:
        if len(entry) == 3:
            if cf_combo[0] in entry and cf_combo[1] in entry:
                new_str = entry.replace(
                    cf_combo[0], '').replace(cf_combo[1], '')
                solution['a'] = new_str
            else:
                solution['a'] = entry
        elif len(entry) == 4:
            if cf_combo[0] in entry and cf_combo[1] in entry:
                new_str = entry.replace(
                    cf_combo[0], '').replace(cf_combo[1], '')
                solution['b'] = new_str
                solution['d'] = new_str
            else:
                solution['b'] = entry
                solution['d'] = entry

    sum_initial_logic = sum([len(val) for val in solution.values()])
    if sum_initial_logic == 9:
        text = 'abcdefg'
        for char in 'abcdefg':
            if char in solution['c']+solution['a']+solution['b']:
                text = text.replace(char, '')

        solution['e'] = solution['g'] = text

    return solution


def fill_initial_digit(output: list):
    digit = {(i): ''for i in range(0, 10)}
    output_copy = output.copy()
    for val in output:
        if len(val) in (2, 4, 3, 7):
            lookup = {2: 1, 4: 4, 3: 7, 7: 8}
            digit[lookup[len(val)]] = val
            output_copy.remove(val)
    return digit, output_copy


def fill_in_5_seg(seg: str, digit: dict, solution: dict, facts: dict):

    for val in [2, 3, 5]:
        true_char = facts[val]['char']
        check_dup = set()
        for char in true_char:
            error_char = set(solution[char])
            if not error_char.issubset(check_dup):
                check_dup = check_dup.union(error_char)
            else:
                if error_char.issubset(set(seg)):
                    digit[val] = seg
    return digit


def fill_in_6_seg(seg: str, digit: dict, solution: dict, facts: dict):
    for val in [0, 6, 9]:
        true_char = facts[val]['char']
        unique_set = set()
        dup_set = set()
        for char in true_char:
            error_char = set(solution[char])
            if not error_char.issubset(unique_set):
                unique_set = unique_set.union(error_char)
            else:
                dup_set = dup_set.union(error_char)

        if dup_set.issubset(set(seg)):
            digit[val] = seg
    return digit


def fill_in_remaining(remain_list: list, digit: dict, solution: dict):
    facts = {
        0: {'segments': 6, 'char': 'abcefg'},
        1: {'segments': 2, 'char': 'cf'},
        2: {'segments': 5, 'char': 'acdeg'},
        3: {'segments': 5, 'char': 'acdfg'},
        4: {'segments': 4, 'char': 'bcdf'},
        5: {'segments': 5, 'char': 'abdfg'},
        6: {'segments': 6, 'char': 'abdefg'},
        7: {'segments': 3, 'char': 'acf'},
        8: {'segments': 7, 'char': 'abcdefg'},
        9: {'segments': 6, 'char': 'abcdfg'},
    }
    for seg in remain_list:
        if len(seg) == 5:
            fill_in_5_seg(seg, digit, solution, facts)
        else:
            fill_in_6_seg(seg, digit, solution, facts)
    return digit


def run_decoder(data):
    entry_split = data.split(' | ')
    entry_pattern = entry_split[0].split()
    entry_output = entry_split[1].split()
    solution = initial_uniqual_val_analysis(entry_pattern)

    digit, remain_segs = fill_initial_digit(entry_pattern)

    full_digit_mapping = fill_in_remaining(remain_segs, digit, solution)

    final_output = [0, 0, 0, 0]
    for idx, result in enumerate(entry_output):
        for key, val in full_digit_mapping.items():
            if len(set(result).symmetric_difference(set(val))) == 0:
                final_output[idx] = key

    return final_output
