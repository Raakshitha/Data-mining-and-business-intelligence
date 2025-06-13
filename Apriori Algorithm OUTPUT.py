Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
===== RESTART: C:\Users\raaks\Downloads\DMBI practical\Apriori algorithm.py ====
Transaction Data:
      Milk  Bread  Butter    Jam
TID                             
1     True   True   False   True
2    False   True    True  False
3     True  False    True  False
4     True   True    True  False
5    False   True   False   True

Frequent Itemsets:
   support         itemsets
0      0.6           (Milk)
1      0.8          (Bread)
2      0.6         (Butter)
3      0.4            (Jam)
4      0.4    (Milk, Bread)
5      0.4   (Milk, Butter)
6      0.4  (Butter, Bread)
7      0.4     (Jam, Bread)

Association Rules:
  antecedents consequents  antecedent support  ...  jaccard  certainty  kulczynski
0      (Milk)     (Bread)                 0.6  ...      0.4  -0.666667    0.583333
1      (Milk)    (Butter)                 0.6  ...      0.5   0.166667    0.666667
2    (Butter)      (Milk)                 0.6  ...      0.5   0.166667    0.666667
3    (Butter)     (Bread)                 0.6  ...      0.4  -0.666667    0.583333
4       (Jam)     (Bread)                 0.4  ...      0.5   1.000000    0.750000

[5 rows x 14 columns]
