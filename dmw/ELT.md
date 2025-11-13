
### **🔹 Objective**

To perform **Extraction**, **Transformation**, and **Loading (ETL)** operations on a dataset in **Power BI** and prepare it for analysis.

---

### **🔹 Step 1: Extraction (Importing Data)**

**Extraction** means collecting data from various sources and bringing it into Power BI.

**Steps:**

1. Open **Power BI Desktop**.
2. Go to the **Home** tab → click on **Get Data** → select the data source (Excel, CSV, SQL Server, or Web).

   * Example: Choose **Excel** → browse and select your file (e.g., *Sales_Data.xlsx*).
3. Click **Load** or **Transform Data** to open it in the **Power Query Editor**.

**Example Dataset (Sales_Data.xlsx):**

| Customer_ID | Product | Quantity | Price | Date       | Region |
| ----------- | ------- | -------- | ----- | ---------- | ------ |
| 101         | Pen     | 10       | 5     | 2024-05-10 | North  |
| 102         | Book    | 3        | 50    | 2024-05-11 | South  |
| 103         | Pencil  | 15       | 3     | 2024-05-12 | East   |

---

### **🔹 Step 2: Transformation (Data Cleaning and Processing)**

**Transformation** means modifying, cleaning, and reshaping the data for analysis.

**Common Transformations in Power Query:**

1. **Remove unwanted columns:**

   * Go to the Power Query Editor.
   * Select unnecessary columns → Right-click → **Remove Columns**.

2. **Rename columns:**

   * Double-click on a column name → rename it (e.g., *Price* → *Unit Price*).

3. **Change data types:**

   * Select the column → click **Data Type** → choose correct type (Date, Decimal, Text, etc.).

4. **Add new columns:**

   * Example: Create a *Total Sales* column = `Quantity * Unit Price`.

     * Go to **Add Column** → **Custom Column** → formula:

       ```
       = [Quantity] * [Unit Price]
       ```

5. **Handle missing values:**

   * Use **Replace Values** or **Remove Rows → Remove Blank Rows**.

6. **Filter rows:**

   * Apply filters (e.g., Region = “North”).

7. **Merge or Append queries:**

   * Merge two tables (e.g., Sales + Customer Info) using **Merge Queries**.
   * Append multiple tables using **Append Queries**.

8. **Group data:**

   * Use **Group By** to summarize total sales by Region or Date.

**Example Result After Transformation:**

| Customer_ID | Product | Quantity | Unit Price | Total Sales | Date       | Region |
| ----------- | ------- | -------- | ---------- | ----------- | ---------- | ------ |
| 101         | Pen     | 10       | 5          | 50          | 2024-05-10 | North  |
| 102         | Book    | 3        | 50         | 150         | 2024-05-11 | South  |
| 103         | Pencil  | 15       | 3          | 45          | 2024-05-12 | East   |

---

### **🔹 Step 3: Loading (Save and Use in Power BI Report)**

Once the data is cleaned and transformed, **load** it into Power BI for reporting and visualization.

**Steps:**

1. In Power Query Editor, click **Close & Apply**.
2. The cleaned data will now appear in the **Data View**.
3. Create visualizations such as:

   * **Bar Chart:** Total Sales by Region.
   * **Pie Chart:** Product-wise Sales Distribution.
   * **Line Chart:** Sales over Time.

---

### **🔹 Step 4: Example Visualization Ideas**

1. **Bar Chart:** Compare Total Sales by Region.
2. **Line Chart:** Track Total Sales over different Dates.
3. **Table Visualization:** Display detailed sales records.

---

### **🔹 Conclusion**

By completing this ETL process in Power BI:

* **Extraction:** Imported data from an Excel file.
* **Transformation:** Cleaned, formatted, and enhanced the data with new columns.
* **Loading:** Loaded the data for visualization and insights.

This workflow ensures your data is **accurate, consistent, and ready for analysis**, making Power BI a complete **ETL + Visualization** tool.

