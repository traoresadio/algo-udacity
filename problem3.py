import heapq


class Huffman:

    def __init__(self):
        self.prefix_code = {}
        self.heap = []

    def get_occurence(self, string):
        result = {}
        for char in string:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
        return result

    def populate_heap(self, result_occ):

        for key in result_occ:
            node = Node(key, result_occ[key])
            heapq.heappush(self.heap, node)
        #print(self.heap)
        return self.heap

    def building_tree(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            addition = Node(None, node1.value + node2.value)
            addition.left = node1
            addition.right = node2
            heapq.heappush(self.heap, addition)
        #print(self.heap)
        return self.heap

    def creating_prefix(self):
        root = heapq.heappop(self.heap)
        current_node = ""
        self.traversing_tree(root, current_node)

    def traversing_tree(self, node, current_node):
        if node is None:
            return
        elif node.key is not None:
            self.prefix_code[node.key] = current_node
        else:
            self.traversing_tree(node.left, current_node + "0")
            self.traversing_tree(node.right, current_node + "1")

    def create_result(self, initial_string):
        result = ""
        for char in initial_string:
            result += self.prefix_code[char]
        return result

    def huffman_encoding(self, string):
        encoded_data = ""
        my_dict = self.get_occurence(string)
        pop_heap = self.populate_heap(my_dict)
        my_tree = self.building_tree()
        print(my_tree)
        self.creating_prefix()
        encoded_data = self.create_result(string)
        return encoded_data, my_tree

    def huffman_decoding(self, encoded_dta, tree):
        result = ""
        node = tree.pop()
        print(tree)
        for bit in encoded_dta:
            if bit == 0:
                node = node.left

            else:
                node = node.right
            if node.key is not None:
                result += node.key
                node = tree
        return result


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, value):
        self.left = value

    def set_right(self, value):
        self.right = value

    def __gt__(self, other):
        if not other:
            return False
        if not isinstance(other, Node):
            return False
        return self.value > other.value

    def __lt__(self, other):
        if not other:
            return False
        if not isinstance(other, Node):
            return False
        return self.value < other.value

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return other.value == self.value


if __name__ == "__main__":
    text = "AAAABBBNNNVVCC"
    huffmanClass = Huffman()
    code, tree = huffmanClass.huffman_encoding(text)
    print(code)
    #print(tree)
    result = huffmanClass.huffman_decoding(code, tree)
    print(result)
