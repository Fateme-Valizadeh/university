subtotal = eval(input("Enter the subtotal: "))
gratuityrate = eval(input("Enter the gratuity rate: "))

gratuity = subtotal * (gratuityrate / 100)
total = subtotal + gratuity

print("Gratuity: ", gratuity)
print("Total: ", total)
