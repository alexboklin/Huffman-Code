from helpers import *
input_string = input()

frequencies = {}
for element in input_string:
    if not element in frequencies:
        frequencies[element] = 1
    else:
        frequencies[element] += 1

tree = []
for key,value in frequencies.items():
    tree.append(binaryTree(key, '', value))

priority_queue = sorted(tree, key=lambda item:item.priority)

if len(priority_queue) == 1:
    leaf_one = priority_queue.pop(0)

    new_node = binaryTree("EMPTY", '' , leaf_one.priority)

    leaf_one.setParent(new_node)

    new_node.setLeftBranch(leaf_one)

    priority_queue = enqueue(new_node, priority_queue)

while len(priority_queue) > 1:
    leaf_one = priority_queue.pop(0)
    leaf_two = priority_queue.pop(0)

    new_node = binaryTree("EMPTY", '' , leaf_one.priority + leaf_two.priority)

    leaf_one.setParent(new_node)
    leaf_two.setParent(new_node)

    new_node.setLeftBranch(leaf_two)
    new_node.setRightBranch(leaf_one)

    priority_queue = enqueue(new_node, priority_queue)

codes = encode(priority_queue[0])

print(len(frequencies), len(encode_string(input_string, codes)))
priority_queue[0].printTree(priority_queue[0])
print(encode_string(input_string, codes))
