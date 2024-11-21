import pandas as pd

items_ordered = pd.read_excel("items_ordered.xlsx")
customers = pd.read_excel("customers.xlsx")

# Задача 1: Найти максимальную цену любого товара
items_ordered['price'] = pd.to_numeric(items_ordered['price'], errors='coerce')
max_price = items_ordered['price'].max()
print("1. Максимальная цена любого товара:", max_price)

# Задача 2: Рассчитать среднюю цену товаров, заказанных в декабре
items_ordered['order_date'] = pd.to_datetime(items_ordered['order_date'], errors='coerce')
december_ordered = items_ordered[items_ordered['order_date'].dt.month == 12]
average_december_price = december_ordered['price'].mean()
print("2. Средняя цена товаров, заказанных в декабре:", average_december_price)

# Задача 3: Общее количество строк в таблице
rows = len(items_ordered)
print("3. Общее количество строк в таблице items_ordered:", rows)

# Задача 4: Найти минимальную цену палатки
tent_orders = items_ordered[items_ordered['item'].str.contains('Tent', case=False, na=False)]
tent_min_price = tent_orders['price'].min()
print("4. Минимальная цена палатки:", tent_min_price)

# Задача 5: Подсчитать количество людей в каждом уникальном штате
# state_counts_dict = {}

# for state in customers['state']:
#     if state in state_counts_dict:
#         state_counts_dict[state] += 1 
#     else:
#         state_counts_dict[state] = 1  

# state_counts = pd.DataFrame(list(state_counts_dict.items()), columns=['state', 'number_of_people'])

# print("5. Количество людей в каждом штате:")
# print(state_counts)

state_counts = customers['state'].value_counts().reset_index()
state_counts.columns = ['state', 'number_of_people']
print("5. Количество людей в каждом штате:")
print(state_counts)

# Задача 6: Найти максимальную и минимальную цену для каждого товара
item_price_stats = items_ordered.groupby('item')['price'].agg(['max', 'min']).reset_index()
item_price_stats.columns = ['item', 'max_price', 'min_price']
print("6. Максимальная и минимальная цена для каждого товара:")
print(item_price_stats)

# Задача 7: Подсчитать количество заказов и их сумму для каждого покупателя
customer_orders = items_ordered.groupby('customerid').agg(
    number_of_orders=('item', 'count'),
    sum_of_orders=('price', 'sum')
).reset_index()
print("7. Количество заказов и их сумма для каждого покупателя:")
print(customer_orders)
