Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
==== RESTART: C:\Users\raaks\Downloads\DMBI practical\Data preprocessing.py ====
Original Data:
    Age   Salary  Score
0  25.0  50000.0   90.0
1  30.0  60000.0   85.0
2   NaN  55000.0   88.0
3  35.0      NaN   75.0
4  40.0  65000.0    NaN

Data After Handling Missing Values:
    Age   Salary  Score
0  25.0  50000.0   90.0
1  30.0  60000.0   85.0
2  32.5  55000.0   88.0
3  35.0  57500.0   75.0
4  40.0  65000.0   75.0

Normalized Data:
        Age    Salary     Score
0  0.000000  0.000000  1.000000
1  0.333333  0.666667  0.666667
2  0.500000  0.333333  0.866667
3  0.666667  0.500000  0.000000
4  1.000000  1.000000  0.000000
