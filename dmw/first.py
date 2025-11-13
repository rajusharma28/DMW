#Integrate data from multiple sources by merging and transforming datasets using Python's pandas library and data manipulation techniques.

import pandas as pd

# Load data from multiple sources
customers = pd.DataFrame({
    'Customer_ID':[101,102,103,104],
    'Name':['Raju','Amit','Priya','Kiran'],
    'city':['Mumbai','Delhi','Pune','Nashik'],
    'Age':[20,23,17,18]
})

purchases = pd.DataFrame({
    'Customer_ID':[101,102,104,105],
    'Product':['Laptop','Mobile','Tablet','Camera'],
    'Amount':[50000,2999,222223,32221]
})



# Merge datasets
merge_data = pd.merge(customers, purchases, on='Customer_ID', how='outer')
print("\nMerged Data:")
print(merge_data)

# Transform the data
merge_data['Name'].fillna('Unknown', inplace=True)
merge_data['city'].fillna('Unknown', inplace=True)
merge_data['Amount'].fillna(0, inplace=True)

# Add a new column
merge_data['Discounted_Amount'] = merge_data['Amount'] * 0.9
print("\nAfter Adding Discounted_Amount:")
print(merge_data)

# Sort by Age
sorted_data = customers.sort_values(by=['Age'])
print("\nSorted by Age:")
print(sorted_data)

# Filter rows where Age > 20
filtered = customers[customers['Age'] > 20]
print("\nFiltered (Age > 20):")
print(filtered)

# Remove duplicate rows
merge_data = merge_data.drop_duplicates()
merge_data = merge_data.drop_duplicates(subset='Name')
print("\nAfter Removing Duplicates:")
print(merge_data)
