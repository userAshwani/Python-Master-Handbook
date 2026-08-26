"""
Q2: write_csv_rows(path, rows) — write a list of dicts to a CSV file at
`path`, using the first dict's keys as the header row (csv module).

Input:  write_csv_rows("out.csv", [{"sku": "A1", "qty": 5}])
Output: a CSV file with header "sku,qty" and row "A1,5"
"""

import csv


def write_csv_rows(path, rows):
    # TODO
    pass


# --- TEST ---
# write_csv_rows("out.csv", [{"sku": "A1", "qty": 5}])
# then read out.csv: expected header 'sku,qty' and row 'A1,5'
