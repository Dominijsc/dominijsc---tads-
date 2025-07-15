import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'idade': [1, 5, 3, 10, 15],
    'nome': ['domini', 'jose', 'coutinho', 'jiliany', 'vitoria']
})

plt.hist(df['idade'])

