import sys
sys.setrecursionlimit(10 ** 6)


def make_tree(tree, parent_idx, node):
    idx, x, y = node
    (p_x, p_y), left, right = tree[parent_idx]

    if x < p_x:
        if left == 0:
            tree[parent_idx][1] = idx
            tree[idx] = [(x, y), 0, 0]
        else:
            make_tree(tree, left, node)
    else:
        if right == 0:
            tree[parent_idx][2] = idx
            tree[idx] = [(x, y), 0, 0]
        else:
            make_tree(tree, right, node)


def pre_order(tree, idx):
    res = []
    if idx == 0:
        return res

    res.append(idx)
    res += pre_order(tree, tree[idx][1])
    res += pre_order(tree, tree[idx][2])
    return res


def post_order(tree, idx):
    res = []
    if idx == 0:
        return res

    res += post_order(tree, tree[idx][1])
    res += post_order(tree, tree[idx][2])
    res.append(idx)
    return res


def solution(nodeinfo):
    sorted_node = []
    for idx, [x, y] in enumerate(nodeinfo, 1):
        sorted_node.append([idx, x, y])
    sorted_node.sort(key=lambda x: -x[2])

    tree = dict()
    root_idx, r_x, r_y = sorted_node.pop(0)
    tree[root_idx] = [(r_x, r_y), 0, 0]

    while sorted_node:
        node = sorted_node.pop(0)
        make_tree(tree, root_idx, node)

    return [pre_order(tree, root_idx), post_order(tree, root_idx)]
