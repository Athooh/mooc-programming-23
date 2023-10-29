# Write your solution here:
def sort_by_remaining_stock(items: list):
    sorted_items_list = sorted([(item[2], item) for item in items])

    sorted_items_list = [item[1] for item in sorted_items_list]
    
    return sorted_items_list

if __name__ == '__main__':
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")
