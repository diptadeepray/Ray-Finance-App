from openpyxl import Workbook

# Function to create and save an Excel file
def create_and_save_excel(filename, data):
    wb = Workbook()
    ws = wb.active

    # Writing data to the Excel file
    for row in data:
        ws.append(row)

    # Saving the file
    wb.save(filename)
    print(f"File '{filename}' saved successfully.")

# Data for the first Excel file
data1 = [
    [],
    [],
         ]


# Data for the second Excel file
data2 = [
    [],
    [],
         ]

# Create and save the first file
create_and_save_excel("file1.xlsx", data1)

# Create and save the second file
create_and_save_excel("file2.xlsx", data2)
