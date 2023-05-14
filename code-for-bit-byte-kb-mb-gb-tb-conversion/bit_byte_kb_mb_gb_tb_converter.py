# Define conversion factors
BITS_IN_BYTE = 8
BYTES_IN_KB = 1024
BYTES_IN_MB = BYTES_IN_KB ** 2
BYTES_IN_GB = BYTES_IN_KB ** 3
BYTES_IN_TB = BYTES_IN_KB ** 4

# A function which convert bits to bytes
def bits_to_bytes(bits):
    return bits / BITS_IN_BYTE

# A function which convert bytes to kilobytes
def bytes_to_kb(bytes):
    return bytes / BYTES_IN_KB

# A function which convert kilobytes to megabytes
def kb_to_mb(kb):
    return kb / BYTES_IN_MB

# A function which convert megabytes to gigabytes
def mb_to_gb(mb):
    return mb / BYTES_IN_GB

# A function which convert gigabytes to terabytes
def gb_to_tb(gb):
    return gb / BYTES_IN_TB

# Example for usage:
bits = 10000000
bytes = bits_to_bytes(bits)
kb = bytes_to_kb(bytes)
mb = kb_to_mb(kb)
gb = mb_to_gb(mb)
tb = gb_to_tb(gb)
print(f"{bits} bits is equal to {bytes} bytes, {kb} KB, {mb} MB, {gb} GB, and {tb} TB.")
