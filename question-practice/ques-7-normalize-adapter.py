"""
QUESTION: csv_row_adapter/json_api_adapter/legacy_xml_adapter(raw) — three Adapter
functions that map raw records from 3 different source shapes into one canonical
PyMart schema. Needed by pro-2-data-normalizer to unify multi-vendor inventory feeds.

Input:  csv_row_adapter({"sku": "A1", "qty": "10", "price": "9.99"})
Output: {"sku": "A1", "quantity": 10, "unit_price": 9.99, "source": "csv"}
"""


def csv_row_adapter(raw):
    # TODO
    pass


def json_api_adapter(raw):
    # TODO
    pass


def legacy_xml_adapter(raw):
    # TODO
    pass


# --- TEST ---
# print(csv_row_adapter({"sku": "A1", "qty": "10", "price": "9.99"}))
# expected: {'sku': 'A1', 'quantity': 10, 'unit_price': 9.99, 'source': 'csv'}
