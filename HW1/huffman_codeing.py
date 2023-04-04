import heapq
from collections import defaultdict

class Node:
    def __init__(self, sym, freq):
        self.sym = sym
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def build_huffman_tree(symbol,probability):
    # 計算字符頻率
    freqs = defaultdict(int)

    for num in symbol:
        freqs[num] += probability[num]


    # 創建所有節點
    nodes = [Node(sym, freq) for sym, freq in freqs.items()]

    heapq.heapify(nodes)
    # print([node.sym for node in nodes])
    # print([node.freq for node in nodes])

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(nodes, new_node)

    return nodes[0]

def build_huffman_table(node, code="", huff_table={}):
    if node is None:
        return
    if node.sym is not None:
        huff_table[node.sym] = code
    build_huffman_table(node.left, code + "0", huff_table)
    build_huffman_table(node.right, code + "1", huff_table)
    return huff_table

def encode(text, huff_table):
    encoded_text = ''
    for char in text:
        encoded_text += huff_table[int(char)]
    return encoded_text

def decode(encoded_text, node):
    decoded_text = ""
    current_node = node
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.sym is not None:
            decoded_text += str(current_node.sym)
            current_node = node
    return decoded_text