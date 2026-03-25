Sistema de Gerenciamento de Estoque

Sistema simples de gerenciamento de estoque em Python.

   Requisitos

- Python 3.6+

   Como rodar

python inventory.py

   Funções disponíveis

- `add_item(item, price, stock)` — Adiciona um novo item ao inventário
- `update_stock(item, quantity)` — Atualiza o estoque de um item (use valores negativos para remover)
- `check_availability(item)` — Retorna o estoque atual de um item
- `sales_report(sales)` — Processa um dicionário de vendas e retorna a receita total

   Exemplo de uso


add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)

sales = {"Apple": 30, "Banana": 20, "Orange": 10}
print(sales_report(sales))
# Error: Item 'Orange' not found.
# Total revenue: $19.00

print(check_availability("Apple"))  # 20
