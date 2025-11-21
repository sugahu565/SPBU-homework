def byte_to_bit(msg) -> str:
    #class <bytes> -> class <str>
    bit_msg = ""
    for i in msg:
        bit_msg += f"{i:08b}"
    return bit_msg


def bit_to_byte(msg) -> bytes:
    #class <str> -> class <bytes>
    byte_array = bytearray()
    for i in range(8, len(msg), 8):
        byte_array.append(int(msg[i - 8:i]))
    lost_symb = len(msg) - len(msg) % 8
    if lost_symb != 0:
        byte_array.append(int(msg[lost_symb:].ljust(8, "0")))
    return byte_array