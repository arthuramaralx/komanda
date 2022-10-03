
from datetime import datetime


def calculate_tab(table: list[dict]):
    total = 0
    for itens in table:
        total += itens["amount"]
    return {"total": total, 'created_at': str(datetime.now()) }