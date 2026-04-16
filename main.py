import csv

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

all_rows = []

for file_name in files:
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["product"].lower() == "pink morsel":
                price = float(row["price"].replace("$", ""))
                quantity = int(row["quantity"])
                sales = price * quantity

                all_rows.append(
                    {
                        "Sales": sales,
                        "Date": row["date"],
                        "Region": row["region"],
                    }
                )


with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Sales", "Date", "Region"])
    writer.writeheader()

    for row in all_rows:
        row["Sales"] = format(row["Sales"], ".2f")
        writer.writerow(row)


print("output.csv has been created!!!!!")