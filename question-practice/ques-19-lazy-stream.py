"""
QUESTION: stream_records(batches) — a generator that lazily yields one
normalized record at a time across multiple batches, without loading every
batch into memory at once. Used by the pro-final-pymart capstone to stream
large inventory feeds efficiently.

Input:  stream_records([[{"sku": "A1"}, {"sku": "A2"}], [{"sku": "B1"}]])
Output: yields {"sku": "A1"}, {"sku": "A2"}, {"sku": "B1"} one at a time
"""


def stream_records(batches):
    # TODO
    pass


# --- TEST ---
# batches = [[{"sku": "A1"}, {"sku": "A2"}], [{"sku": "B1"}]]
# print(list(stream_records(batches)))
# expected: [{'sku': 'A1'}, {'sku': 'A2'}, {'sku': 'B1'}]
