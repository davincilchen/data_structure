import random
from collections import deque

class Node:
    def __init__(self, value):
        self.child = []
        self.value = value


def merge(heap1: Node, heap2: Node):
    if heap1 == None: return heap2
    if heap2 == None: return heap1
    if heap1.value > heap2.value:
        heap1, heap2 = heap2, heap1

    heap1.child.append(heap2)
    return heap1

def build(values: list):
    dq = deque()
    for v in values:
        dq.append(Node(v))
    
    while len(dq) > 1:
        new_heap = merge(dq.popleft(), dq.popleft())
        dq.append(new_heap)

    return dq[0]  

def sorting(heap: Node):
    result = []
    result.append(heap.value)
    while heap.child:
        dq = deque(heap.child)
        while len(dq) > 1:
            new_node = merge(dq.popleft(), dq.popleft())
            dq.append(new_node)
        heap = dq[0]
        result.append(heap.value)
    return result

def print_heap(heap: Node):
    print(heap.value, end=' ')
    if not heap.child:
        print(None, end=' ')
        return
    for c in heap.child:
        print_heap(c)

def print_heap2(heap: Node):
    print(heap.value, end=' ')
    if not heap.child:
        print("no child")
        return
    print("heap child: ", end='')
    for c in heap.child:
        print(c.value, end= ' ')
    print()
    for c in heap.child:
        print_heap2(c)

if __name__ == "__main__":
    values = [x for x in range(10)]
    print(values)
    random.shuffle(values)
    heap = build(values)
    # print_heap2(heap)
    print(sorting(heap))

    