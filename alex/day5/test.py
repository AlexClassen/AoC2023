def merge_overlapping_pairs(pair_list):
    pair_list.sort()

    merged_pairs = [pair_list[0]]

    for current_pair in pair_list[1:]:
        previous_pair = merged_pairs[-1]

        if current_pair[0] <= previous_pair[0] + previous_pair[1]:
            merged_pairs[-1] = (previous_pair[0], max(previous_pair[0] + previous_pair[1], current_pair[0] + current_pair[1]) - previous_pair[0])
        else:
            merged_pairs.append(current_pair)

    return merged_pairs

# Example usage:
pairs = [(10, 10), (15, 10), (0, 5), (8, 5)]

for pair in merge_overlapping_pairs(pairs):
    print(str(pair[0]) + "-->" + str(pair[0] + pair[1]))