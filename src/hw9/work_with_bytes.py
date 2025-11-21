def byte_to_bit(msg) -> str:
    #class <bytes> -> class <str>
    bit_msg = ""
    for i in msg:
        bit_msg += f"{i:08b}"
    return bit_msg


def bit_to_byte(msg) -> bytes:
    #class <str> -> class <bytes>
    byte_array = bytearray()
    need_len = len(msg) // 8 * 8
    for i in range(0, need_len, 8):
        byte_array.append(int(msg[i:i + 8], 2))
    lost_symb = msg[need_len:]
    if len(lost_symb) > 0:
        byte_array.append(int(lost_symb.ljust(8, "0"), 2))
    return byte_array