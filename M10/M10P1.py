repeat = input("Do you want to compute next month's forecast? (Yes or No): ")
while repeat.lower() == "yes":
    last_name = input("Enter last name: ")
    month = input("Enter month (e.g., Jan, Feb, etc.): ")
    sales = int(input("Enter sales: "))
    
    month = month.lower()
    if month in ["jan", "feb", "mar"]:
        forecast_percent = 10
    elif month in ["apr", "may", "jun"]:
        forecast_percent = 15
    elif month in ["jul", "aug", "sep"]:
        forecast_percent = 20
    elif month in ["oct", "nov", "dec"]:
        forecast_percent = 25
    else:
        forecast_percent = 0 
    
    next_sales = sales * (100 + forecast_percent) // 100
    print("Forecast for next month for", last_name, "is:", next_sales)
    print()
    repeat = input("Do you want to compute next month's forecast? (Yes or No): ")
