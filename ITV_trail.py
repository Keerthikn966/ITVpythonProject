import pandas as pd
import os
from csv import reader
# Data from the question
DataLst = []
absolutePath = os.path.abspath('Resources/DataList.csv')
with open(absolutePath, 'r') as read_obj:
       csv_reader = reader(read_obj)
       header = next(csv_reader)
       for row in csv_reader:
           DataLst.append(row)
# The data as a DataFrame
df = pd.DataFrame(DataLst, columns=['Start time', 'End time'], dtype='datetime64[ns]')
min_time = df['Start time'].min()
max_time = df['End time'].max()
ts_index = pd.date_range(min_time, max_time, freq='S')
starts = pd.Series(1, df['Start time'])
ends = pd.Series(-1, df['End time'] + pd.Timedelta('1 sec'))
concurrency_changes = pd.concat([starts, ends]) \
                      .groupby(level=0).sum() \
                      .cumsum()
concurrency = concurrency_changes.reindex(ts_index, method='ffill')
a = concurrency.resample('1S').max()
b = a.max()
print(b)
