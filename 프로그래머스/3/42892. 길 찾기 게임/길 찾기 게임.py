import sys
sys.setrecursionlimit(10 ** 6)


# 새 노드를 부모 노드와 연결시켜 트리를 만드는 함수
def make_tree(tree, parent_idx, node):
    idx, x, y = node
    (p_x, p_y), left, right = tree[parent_idx]

    # 새 노드의 x좌표가 부모 노드보다 작을 경우 왼쪽 서브 트리에 연결
    if x < p_x:
        # 부모의 왼쪽 자식 노드가 비어 있는 경우
        if left == 0:
            # 트리의 왼쪽 자식 자리에 새 노드를 연결
            tree[parent_idx][1] = idx
            # 연결된 새 노드에 정보를 저장(아직 자식이 없으므르 좌우 자식을 0으로 초기화)
            tree[idx] = [(x, y), 0, 0]
        # 부모의 왼쪽 자식 노드가 있는 경우
        else:
            # 왼쪽 자식 노드를 부모로하여 재귀
            make_tree(tree, left, node)

    # 오른쪽 서브 트리에 연결
    else:
        if right == 0:
            tree[parent_idx][2] = idx
            tree[idx] = [(x, y), 0, 0]
        else:
            make_tree(tree, right, node)

# 전위 순회 함수
def pre_order(tree, idx):
    res = []
    # 비어 있는 노드일 경우 번호를 저장하지 않음
    if idx == 0:
        return res

    '''
    전위 순회 이므로 루트 -> 왼쪽 자식 -> 오른쪽 자식 순서로 순회
    재귀의 형태인 이유는 왼쪽 자식을 순회한 다음 그 왼쪽 자식의 왼쪽, 오른쪽 자식을 순회한 다음
    루트의 오른쪽 자식을 탐색해야 하기 때문
    '''
    
    # 루트 노드를 저장
    res.append(idx)
    # 왼쪽 자식 저장
    res += pre_order(tree, tree[idx][1])
    # 오른쪽 자식 저장
    res += pre_order(tree, tree[idx][2])
    return res

# 후위 순회 함수
def post_order(tree, idx):
    res = []
    if idx == 0:
        return res

    '''
    후위 순회 이므로 왼쪽 자식 -> 오른쪽 자식 -> 루트 순서로 순회
    '''

    res += post_order(tree, tree[idx][1])
    res += post_order(tree, tree[idx][2])
    res.append(idx)
    return res


def solution(nodeinfo):
    sorted_node = []
    for idx, [x, y] in enumerate(nodeinfo, 1):
        sorted_node.append([idx, x, y])
    # y 좌표가 큰 노드부터 트리 생성
    sorted_node.sort(key=lambda x: -x[2])

    tree = dict()
    root_idx, r_x, r_y = sorted_node.pop(0)
    tree[root_idx] = [(r_x, r_y), 0, 0]

    # 모든 노드가 트리에 연결 될 때까지 레벨이 높은 노드부터 연결
    while sorted_node:
        node = sorted_node.pop(0)
        make_tree(tree, root_idx, node)

    return [pre_order(tree, root_idx), post_order(tree, root_idx)]
