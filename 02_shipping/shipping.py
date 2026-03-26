weight = 1.5

premium_shipping = 125

ground_flat_charge = 20.00



if weight <= 0:
    print("Error: Invalid weight")
else:
    #Ground Shipping
    if weight <= 2:
        ground_cost = (weight * 1.50) + ground_flat_charge
    elif weight <= 6:   
        ground_cost = (weight * 3.00) + ground_flat_charge
    elif weight <= 10:
        ground_cost = (weight * 4.00) + ground_flat_charge
    elif weight > 10:
        ground_cost = (weight * 4.75) + ground_flat_charge


    #Drone Shipping (There is not flat charge)

    if weight <= 2:
        drone_cost = (weight * 4.50) 
    elif weight <= 6:   
        drone_cost = (weight * 9.00) 
    elif weight <= 10:
        drone_cost = (weight * 12.00) 
    elif weight > 10:
        drone_cost = (weight * 14.25) 

    #Total Cost


    print(f"Total Ground Shipping cost is: ${ground_cost}")
    print(f"Total Drone Shipping cost is: ${drone_cost}")  
    print(f"The Ground Shipping Premium Cost is: {premium_shipping}")

    # Cheapest One

    if ground_cost < drone_cost and ground_cost < premium_shipping:
        print(f"The cheapest method is: Ground Shipping. Total: ${ground_cost}")
    elif drone_cost < ground_cost and drone_cost < premium_shipping:
        print(f"The cheapest method is: Drone Shipping. Total: ${drone_cost}")
    else:
        print(f"The cheapest method is: Premium Shipping. Total: ${premium_shipping}")