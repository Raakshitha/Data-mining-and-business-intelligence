
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = {
    'TID': [1, 2, 3, 4, 5],
    'Milk':   [1, 0, 1, 1, 0],
    'Bread':  [1, 1, 0, 1, 1],
    'Butter': [0, 1, 1, 1, 0],
    'Jam':    [1, 0, 0, 0, 1]
}

df = pd.DataFrame(data).set_index('TID')

df = df.astype(bool)

print("Transaction Data:")
print(df)

min_support = 0.4
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_itemsets)

min_confidence = 0.6
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
print("\nAssociation Rules:")
print(rules)
