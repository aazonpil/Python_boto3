def generate_receipt(order):
    # Created empty list to store keys and values
    items_price_list = ""
    
    # Iterate through the order to build the list of items and their prices.
    for item, price in order.items():
        items_price_list += f'{item}: $ \t{price:.2f}\n'
    
    # Calculate the total price of the order.
    total_price = sum(order.values())
    
    # Construct the message showing the total cost.
    message_end = f'the total cost of your order is :{total_price:.2f}\n'
    
    # Define the receipt's header.
    receipt_header = "RECEIPT \t"
    
    # Combine all parts to create the receipt content.
    receipt_content = receipt_header + "\n\n" + items_price_list + "Total cost: $" + str(total_price) + "\n" + message_end

    # Write the receipt content to a text file.
    with open('receipt.txt', 'w') as file:
        file.write(receipt_content)
    
    # Indicate that the receipt has been generated.
    print("Receipt has been successfully generated and saved to 'receipt.txt'.")

# Main
order = {"tomato": 30, "thyme": 4.5, "garlic": 7.5, "rice": 10, "onion": 4, "fish": 9.99}
# Call the function with the given order.
generate_receipt(order)








    