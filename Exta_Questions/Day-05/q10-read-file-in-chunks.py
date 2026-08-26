"""
Q10: read_in_chunks(path, chunk_size) — a generator that reads a file
piece by piece (chunk_size characters at a time) instead of loading the
whole file into memory at once.

Input:  read_in_chunks("big.txt", 1024)
Output: yields successive 1024-character strings until EOF
"""


def read_in_chunks(path, chunk_size):
    # TODO
    pass


# --- TEST ---
# for chunk in read_in_chunks("big.txt", 1024):
#     print(len(chunk))  # expected: prints 1024 repeatedly, then a smaller final chunk
