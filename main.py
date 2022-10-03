from utils.json_handler import read_json, write_json
from management.tab_handler import calculate_tab


if __name__ == "__main__":
    # Utilize essa área para testes com print
    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]

    print(calculate_tab(table_1))
    ...
