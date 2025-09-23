# using camelCase 
def calculate_total_cost() : 
    new_car_price = float(input("Enter the price of a new car (in Euro): "))
    yearly_km = float(input("Enter the estimated kilometers traveled/year: "))                # kM = 30,000
    fuel_cost = float(input("Enter the estimated cost of fuel/litre(in Euro): "))             # Gasoline = 2 euro/Litre 
    efficiency = float(input("Enter the efficiency (in km/litre): "))
    resale_value = float(input("Enter the resale value of the used car after 5 years(in Euro): "))

    yearly_fuel_consum = yearly_km / efficiency         # total fuel consumption in a single year
    total_fuel_consum = yearly_fuel_consum * 5          # in 5 years
    total_fuel_cost = total_fuel_consum * fuel_cost     # total fuel cost in 5 years
    final_cost = new_car_price + total_fuel_cost - resale_value     # total cost of ownership of the car for 5 years

    return final_cost

def main() : 
    print("👋 Let's calculate the cost for a **Hybrid Car**:\n")
    hybrid_cost = calculate_total_cost()

    print("\n\n👋 Now calculate the cost for a **Gasoline Car**:\n")
    gasoline_cost = calculate_total_cost()


    print("\n🔍 Cost Comparison")
    print(f"\t- Hybrid Car Total Cost:    €{hybrid_cost:.2f}")
    print(f"\t- Gasoline Car Total Cost:  €{gasoline_cost:,.2f}")

    if hybrid_cost < gasoline_cost:
        print("🚀 Verdict: The **Hybrid** car is more cost-effective! ✅")
    elif gasoline_cost < hybrid_cost:
        print("🛢️ Verdict: The **Gasoline** car is more cost-effective! ✅")
    else:
        print("🤝 Verdict: Both cars cost the same. Choose based on preferences!")
 
    
if __name__ == "__main__" : 
    main() 
