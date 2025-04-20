import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 28],
    'City': ['Seoul', 'New York', 'London']
}
df = pd.DataFrame(data)
print(df)