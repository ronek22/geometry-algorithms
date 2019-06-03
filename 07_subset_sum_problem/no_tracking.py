from heapq import merge


def trim(data, delta):
    output = []
    last = 0

    for element in data:
        if element > last * (1 + delta):
            output.append(element)
            last = element

    return output

def merge_lists(*iterables):
    """Using heapq.merge, that have linear time complexity"""
    last, output = None, []
    for val in merge(*iterables):
        if val != last:
            last = val
            output.append(val)
    return output

def subset_sum(data, target, epsilon):
    acc = [0]
    count = len(data)

    for i, element in enumerate(data, start=1):
        augmented_list = [element+a for a in acc]
        acc = merge_lists(acc, augmented_list)
        acc = trim(acc, delta=float(epsilon) / (2 * count))
        acc = [val for val in acc if val <= target]

    return acc[-1]

if __name__ == "__main__":

    data = [650, 1200, 1350, 450, 2875, 1625, 1500, 1875]
    target = 3450
    epsilon = 0.2

    print(subset_sum(data, target, epsilon=epsilon), sep="\n")