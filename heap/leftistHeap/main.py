
import random
from collections import deque

class Node:
    def __init__(self, value):
        self.distance = 0
        self.value = value
        self.right_node = None
        self.left_node = None
    
    def __str__(self):
        return "[value({}) dist({})]".format(self.value, self.distance)


def merge(heap1: Node, heap2: Node):
    if heap1 == None: return heap2
    if heap2 == None: return heap1
    if heap1.value > heap2.value:
        heap1, heap2 = heap2, heap1
    
    if heap1.left_node == None:
        heap1.left_node = heap2
    else:
        heap1.right_node = merge(heap1.right_node, heap2)

    if heap1.left_node != None and heap1.right_node != None:
        if heap1.left_node.distance < heap1.right_node.distance:
            heap1.left_node, heap1.right_node = heap1.right_node, heap1.left_node
        heap1.distance = heap1.right_node.distance + 1

    return heap1

def sorting(heap: Node):
    result = []
    while heap != None:
        result.append(heap.value)
        heap = merge(heap.left_node, heap.right_node)
    return result
        
def build(values):
    dq = deque()
    for v in values:
        dq.append(Node(v))
    while len(dq) > 1:
        new_heap = merge(dq.popleft(), dq.popleft())
        dq.append(new_heap)
    
    return dq[0]

def print_heap(heap: Node):
    if heap == None:
        print(None, end=' ')
        return
    print(heap, end=' ')
    print_heap(heap.left_node)
    print_heap(heap.right_node)

if __name__ == "__main__":
    values = [x for x in range(10)]
    random.shuffle(values)
    heap1 = build(values)
    values2 = [x for x in range(11, 20)]
    random.shuffle(values2)
    heap2 = build(values2)
    heap = merge(heap1, heap2)
    # print_heap(heap)
    print(sorting(heap))
    

    
    

        