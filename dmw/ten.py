from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Step 1: Simple shopping data
dataset = [
    ['milk', 'bread'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter'],
    ['bread'],
    ['milk', 'bread']
]

# Step 2: Convert to table (True/False for each item)
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Step 3: Find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
print("Frequent Itemsets:\n", frequent_itemsets)

# Step 4: Find association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
print("\nAssociation Rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence']])
