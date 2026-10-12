orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]
unique_products = []

for product in orders:
    if product not in unique_products:
        unique_products.append(product)

print(unique_products)
frequencies = [
    (product, orders.count(product))
    for product in unique_products
]

print(frequencies)
most_popular = ""
highest_count = 0

for product, count in frequencies:
    if count > highest_count:
        highest_count = count
        most_popular = product

print(most_popular, highest_count)
last_three = orders[-1:-4:-1]
print(last_three)