import heapq


class Huffman:

    def __init__(self):
        self.prefix_code = {}

    def get_occurence(self, string):
        result = {}
        for char in string:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
        return result

    def populate_heap(self, result_occ):
        heap =[]
        for key in result_occ:
            node = Node(key, result_occ[key])
            heapq.heappush(heap, node)
        #print(heap)
        return heap

    def building_tree(self,heap):
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            addition = Node(None, node1.value + node2.value)
            addition.left = node1
            addition.right = node2
            heapq.heappush(heap, addition)
        print(heap)
        return heap

    def creating_prefix(self,heap):
        root = heap[0]
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
        my_tree = self.building_tree(pop_heap)
        print(my_tree)
        self.creating_prefix(my_tree)
        encoded_data = self.create_result(string)
        return encoded_data, my_tree

    def huffman_decoding(self, encoded_dta, param_tree):
        decoded = ""
        node = heapq.heappop(param_tree)
        print('node')
        print(node)
        left = node.get_left()
        print('lefti')
        print(left)

        for bit in encoded_dta:
            if bit == '0':
                node = node.left

            else:
                node = node.right
            if node.key is not None:
                decoded += node.key
                node = param_tree
        print(decoded)
        return decoded


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

    def has_right(self):
        return self.right is not None

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
    code, the_tree = huffmanClass.huffman_encoding(text)
    print(code)
    print('main')
    print(the_tree)
    result = huffmanClass.huffman_decoding(code, the_tree)
    print(result)
