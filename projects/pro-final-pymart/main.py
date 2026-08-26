"""
pro-final-pymart — main.py
PyMart Inventory & Analytics Engine — Capstone Project

HOW TO RUN (after all 4 modules are complete):
    python projects/pro-final-pymart/main.py

EXPECTED OUTPUT:
    Step 1: Normalized 5 inventory records
    Step 2: Applied RBAC for role "analyst"
    Step 3: Analytics Report Generated

    --- PIVOT TABLE (warehouse x status) ---
    {'WH-1': {'in_stock': 320, 'backordered': 40}, 'WH-2': {'in_stock': 90}}

    --- RUNNING TOTAL ---
    [120, 260, 410, 500, 500]  (cumulative quantity)

    --- SUMMARY ---
    {'total': 500, 'average': 100.0, 'min': 40, 'max': 200, 'count': 5}

    --- AUDIT TRAIL (1 change detected) ---
    {'status': {'from': 'pending', 'to': 'in_stock'}}
"""

# --- STEP 1: Import all 4 modules (uncomment as you complete each) ---
# from projects.pro_1_py_utils.utils import pipe, deep_copy
# from projects.pro_2_data_normalizer.normalizer import normalize_batch, deep_diff
# from projects.pro_3_rbac_engine.rbac import apply_rbac
# from projects.pro_4_analytics_engine.analytics import pivot_table, running_total, multi_key_sort

# --- SAMPLE RAW DATA (legacy nested feed from Warehouse WH-1) ---
RAW_INVENTORY = [
    {"sku": "SKU-1001", "qty": "120", "status": "in_stock", "warehouse": "WH-1", "contact_email": "ops1@supplier.com"},
    {"sku": "SKU-1002", "qty": "140", "status": "in_stock", "warehouse": "WH-1", "contact_email": "ops2@supplier.com"},
    {"sku": "SKU-1003", "qty": "40", "status": "backordered", "warehouse": "WH-1", "contact_email": "ops3@supplier.com"},
    {"sku": "SKU-1004", "qty": "90", "status": "in_stock", "warehouse": "WH-2", "contact_email": "ops4@supplier.com"},
    {"sku": "SKU-1005", "qty": "110", "status": "in_stock", "warehouse": "WH-1", "contact_email": "ops5@supplier.com"},
]


# --- PIPELINE STEPS ---

def step1_normalize(raw_batch, source_type):
    # TODO: call normalizer.normalize_batch(raw_batch, source_type)
    # Returns: list of canonical {sku, quantity, status, warehouse, contact_email, source}
    print(f"Step 1: Normalized {len(raw_batch)} inventory records")
    return raw_batch  # replace with real call


def step2_apply_rbac(records, role):
    # TODO: call rbac.apply_rbac(record, role) for each record
    # Returns: records with restricted fields masked per role
    print(f'Step 2: Applied RBAC for role "{role}"')
    return records  # replace with real call


def step3_generate_report(records):
    # TODO: call analytics functions to produce the full report
    # Returns: {"pivot": ..., "running_total": ..., "summary": ...}
    print("Step 3: Analytics Report Generated\n")

    # pivot = analytics.pivot_table(records, "warehouse", "status", "quantity")
    # print("--- PIVOT TABLE (warehouse x status) ---")
    # print(pivot)

    # rt = analytics.running_total(records, "quantity")
    # print("\n--- RUNNING TOTAL ---")
    # print(rt)

    # summary = { ... }
    # print("\n--- SUMMARY ---")
    # print(summary)

    return {}  # replace with real report dict


def step4_audit_trail(before, after):
    # TODO: call normalizer.deep_diff(before, after) + safe_json_dumps(diff)
    # diff = normalizer.deep_diff(before, after)
    # log = safe_json_dumps(diff)
    # print("\n--- AUDIT TRAIL ---")
    # print(log)
    pass


# --- LAZY STREAM (for large inventory feeds) ---

def stream_records(raw_batches, source_type):
    # TODO: lazily yield one normalized record at a time
    # Use ques-19-lazy-stream.py logic to avoid loading everything into RAM
    for batch in raw_batches:
        # yield from normalize_batch(batch, source_type)
        yield batch  # replace with real normalized record


def safe_json_dumps(value):
    # TODO: see ques-20-safe-json.py — handle circular references safely
    pass


# --- MAIN ENTRY POINT ---

def main():
    role = "analyst"

    normalized = step1_normalize(RAW_INVENTORY, "legacy_xml")
    masked = step2_apply_rbac(normalized, role)
    report = step3_generate_report(masked)

    # Audit example: detect what changed between two records
    before = {"sku": "SKU-1001", "status": "pending", "quantity": 120}
    after = {"sku": "SKU-1001", "status": "in_stock", "quantity": 120}
    step4_audit_trail(before, after)


if __name__ == "__main__":
    main()
