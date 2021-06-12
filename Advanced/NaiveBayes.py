import pandas as pd

def naive_bayes(data_table):
    # step 1: convert data-set into frequency table

columns = ['Person', 'height (feet)', 'Weight (lbs)', 'foot size (inches)']
data_set = [
    ['male', 6, 180, 12],
    ['male', 5.92, 190, 11],
    ['male', 5.58, 170, 12],
    ['male', 5.92, 165, 10],
    ['female', 5, 100, 6],
    ['female', 5.5, 150, 8],
    ['female', 5.42, 130, 7],
    ['female', 5.75, 150, 9]
]
df = pd.DataFrame(data_set, columns=columns)
naive_bayes(df)