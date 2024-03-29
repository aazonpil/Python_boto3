def generate_receipt(order):

# Write the receipt content to a text file.
    with open('receipt.txt', 'w') as file:
        file.write(receipt_content)
    
    # Iterate through the order to build the list of items and their prices.
        for item, price in order.items():
            file.write(f'{item}: $ \t{price:.2f}\n')
    
    # Calculate the total price of the order.
    total_price = sum(order.values())
    
    # Construct the message showing the total cost.
    message_end = f'the total cost of your order is :{total_price:.2f}\n'
    
    # Define the receipt's header.
    receipt_header = "RECEIPT \t"
    
    # Combine all parts to create the receipt content.
    receipt_content = receipt_header + "\n\n" +  "Total cost: $" + str(total_price) + "\n" + message_end

    
    # Indicate that the receipt has been generated.
    print("Receipt has been successfully generated and saved to 'receipt.txt'.")

# Main
order = {"tomato": 30, "thyme": 4.5, "garlic": 7.5, "rice": 10, "onion": 4, "fish": 9.99}
# Call the function with the given order.
generate_receipt(order)



