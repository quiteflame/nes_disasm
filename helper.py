def bit_val(num, idx):
    return num & (1 << idx)


def flag_val(num, idx):
    return bit_val(num, idx) != 0


def high_nibble(num):
    return num >> 4


def low_nibble(num):
    return num & 0x0F  # 0x0F == 15


def combine_nibble(high, low):
    return (high << 4) | low
