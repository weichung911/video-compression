import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # 計算字符頻率
    freqs = defaultdict(int)
    for char in text:
        freqs[char] += 1

    print(freqs)

    # 創建所有節點
    nodes = [Node(char, freq) for char, freq in freqs.items()]


    # 將節點加入優先隊列中
    heapq.heapify(nodes)

    # 合併節點，直到只剩下一個節點
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
    if node.char is not None:
        huff_table[node.char] = code
    build_huffman_table(node.left, code + "0", huff_table)
    build_huffman_table(node.right, code + "1", huff_table)
    return huff_table

def encode(text, huff_table):
    encoded_text = ""
    for char in text:
        encoded_text += huff_table[char]
    return encoded_text

def decode(encoded_text, node):
    decoded_text = ""
    current_node = node
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = node
    return decoded_text

# 使用示例
text = "hello world"
root = build_huffman_tree(text)
huff_table = build_huffman_table(root)
print(huff_table)
encoded_text = encode(text, huff_table)
decoded_text = decode(encoded_text, root)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)

