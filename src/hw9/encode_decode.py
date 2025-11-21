from queue import PriorityQueue


def give_huffman_code(graph: dict, root: str, huffDict: dict, path: str):
    if root in graph:
        child1, child2 = graph[root]
        give_huffman_code(graph, child1, huffDict, path + "0")
        give_huffman_code(graph, child2, huffDict, path + "1")
    else:
        huffDict[root] = path


def encode(msg: str) -> tuple[str, dict[str, str]]:
    entry_of_symb = {}
    for c in msg:
        if c in entry_of_symb:
            entry_of_symb[c] += 1
        else:
            entry_of_symb[c] = 1

    q = PriorityQueue()
    len_queue = 0
    for symb, entry in entry_of_symb.items():
        q.put((entry, symb))
        len_queue += 1

    graph = {}
    # key = parent, value = (child1, child2)
    while len_queue > 1:
        min_symb1 = q.get()
        min_symb2 = q.get()
        s = min_symb1[1] + min_symb2[1]
        graph[s] = (min_symb1[1], min_symb2[1])
        q.put((min_symb1[0] + min_symb2[0], s))
        len_queue -= 1

    root = q.get()[1]
    huffmanDict = {}

    if len(root) == 1:
        huffmanDict[root] = "1"
    else:
        give_huffman_code(graph, root, huffmanDict, "")

    encoded_msg = ""
    for c in msg:
        encoded_msg += huffmanDict[c]
    return (encoded_msg, huffmanDict)


def decode(encoded: str, table: dict[str, str]) -> str:
    reversed_table = {}
    for key, value in table.items():
        reversed_table[value] = key
    msg = ""
    symb = ""
    for c in encoded:
        symb += c
        if symb in reversed_table:
            msg += reversed_table[symb]
            symb = ""
    return msg


def encode_f(msg) -> str:
    """
    returns encoded message with table in it
    struct of table:
    1. number of characters used (16 bits)
    2. UTF-8 character code (16 bits) + Huffman code symbol lenght (16 bits) + Huffman code of symbol
    point 2 for each unique symbol
    """
    encoded_msg, huffmanDict = encode(msg)
    table = ""
    used_symbols = len(huffmanDict)
    table += f"{used_symbols:016b}"
    for symb, code in huffmanDict.items():
        table += f"{ord(symb):016b}{len(code):016b}{code}"
    s = table + encoded_msg
    extra_symb = (8 - len(s) % 8) % 8
    return f"{extra_symb:08b}" + s


def decode_f(msg) -> str:
    if len(msg) < 24:
        raise ValueError("invalid file, table doesn't exist")
    extra_symb = int(msg[:8], 2)
    used_symbols = int(msg[8:24], 2)
    # start new line of table
    start = 24
    huffmanDict = {}
    while used_symbols > 0:
        code_of_symb = msg[start : start + 16]
        symb = chr(int(code_of_symb, 2))
        len_huff_code = int(msg[start + 16 : start + 32], 2)
        start += 32
        huff_code = ""
        for i in range(start, start + len_huff_code):
            huff_code += msg[i]
        huffmanDict[symb] = huff_code
        start = start + len_huff_code
        used_symbols -= 1
    return decode(msg[start:-extra_symb], huffmanDict)
