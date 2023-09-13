'''import openpyxl

# Define default values for each stage
default_values = {
    "Startup": {
        "temperature": 0.5,
        "expense_ratio": 0.8,
        "sales_growth": 1.05
    },
    "Growth": {
        "temperature": 0.6,
        "expense_ratio": 0.7,
        "sales_growth": 1.3
    },
    "Mature": {
        "temperature": 0.7,
        "expense_ratio": 0.6,
        "sales_growth": 1.0
    }
}

try:
    # Create a new Excel file
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Ask the user for the business stage
    stage = input("Enter the stage of the business (Startup/Growth/Mature): ")

    # Validate the stage input
    if stage not in default_values:
        print("Invalid stage input. Please enter one of: Startup, Growth, Mature")
    else:
        # Initialize startup costs
        startup_costs = {}

        # Ask for startup costs if it's the Startup stage
        if stage == "Startup":
            print("Enter startup costs (enter blank to finish):")
            while True:
                item = input("Enter item name (or blank to finish): ")
                if not item:
                    break
                amount = float(input("Enter item amount: "))
                startup_costs[item] = amount

        # Initialize assets
        assets = {}

        # Ask for existing assets and new assets if it's not the Startup stage
        if stage != "Startup":
            print("Enter existing assets (enter blank to finish):")
            while True:
                asset_name = input("Enter asset name (or blank to finish): ")
                if not asset_name:
                    break
                asset_amount = float(input("Enter asset amount: "))
                assets[asset_name] = asset_amount

            print("Enter new assets (enter blank to finish):")
            while True:
                asset_name = input("Enter new asset name (or blank to finish): ")
                if not asset_name:
                    break
                asset_amount = float(input("Enter new asset amount: "))
                assets[asset_name] = asset_amount

        # Ask the user for inputs
        sales = float(input("Enter current sales: "))

        # Create headers for the financial statements
        headers = ["Period", "Sales", "COGS", "Gross Profit", "General & Admin", "R&D", "Depreciation", "Net Income"]
        sheet.append(headers)

        # Calculate projections for 36 periods
        for period in range(1, 37):
            # Calculate projections based on user input and default values
            stage_values = default_values[stage]
            cogs = sales / (1 + stage_values["expense_ratio"])
            gross_profit = sales - cogs
            general_admin = gross_profit * 0.2  # You can adjust this as needed
            research_dev = gross_profit * 0.1  # You can adjust this as needed
            depreciation = 5000  # You can adjust this as needed
            net_income = sales - (cogs + general_admin + research_dev + depreciation)

            # Update the Excel sheet with the projections for the current period
            row_data = [period, sales, cogs, gross_profit, "", general_admin, research_dev, depreciation, net_income]
            sheet.append(row_data)

            # Update startup costs for period 0 (Startup stage only)
            if period == 1 and stage == "Startup":
                for item, amount in startup_costs.items():
                    row_data = [0, "", "", "", item, "", "", amount, ""]
                    sheet.append(row_data)

            # Update sales for the next period based on the sales growth rate
            sales *= stage_values["sales_growth"]

        # Save the updated Excel file
        workbook.save("Pro Forma.xlsx")
        print("Projections updated successfully.")

except Exception as e:
    print("An error occurred:", str(e))
'''