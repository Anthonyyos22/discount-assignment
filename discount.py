def calculate_discount(price, discount_percent):
    """Calculate final price after discount if discount is 20% or more"""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def main():
    try:
        original_price = float(input("Enter the original price: $"))
        discount = float(input("Enter the discount percentage: "))
        
        if original_price < 0 or discount < 0:
            print("Error: Price and discount must be positive numbers")
            return
            
        final_price = calculate_discount(original_price, discount)
        
        if discount >= 20:
            print(f"Final price after {discount}% discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. Original price: ${original_price:.2f}")
    except ValueError:
        print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()