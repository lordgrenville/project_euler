import pandas as pd

df = pd.read_csv('p022_names.txt', delim_whitespace=True, lineterminator=',', header=None, na_filter=False)
# No na_filter because NA is a name! delim_ in order to start a new line at each comma
df = df.sort_values(by=0).reset_index().reset_index()
df.set_index('index', inplace=True)
df.columns = ['Rank', 'Names']
# keep original index (bonus), get alphabetic index as score
gematria = {val: idx + 1 for idx, val in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
df['Gematria'] = df['Names'].map(lambda x: sum([gematria[i] for i in x]))
df['Score'] = (df['Rank'] + 1) * df['Gematria']
print(sum(df['Score'].values))
