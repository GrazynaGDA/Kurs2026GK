### Plik .csv z danymi o różnych Pokemonach
# https://hub.gesis.mybinder.org/user/kflisikowsky-awdp-q36hawa9/lab/tree/data/pokemon.csv

import pandas as pd

### Plik .csv z danymi o różnych Pokemonach
# 
df_pokemony = pd.read_csv("pokemon_lok.csv")

# print(df_pokemony.head(5))
# print('----------------- a -------------------')
# print(df_pokemony['Name'].head(5))
# print(df_pokemony.shape)
# print (df_pokemony.sort_values("Name").head(5))
# Jaka jest Szybkość Pokemona z najwyższym Atakiem?
# print ("Szybkość Pokemona z najwyższym Atakiem ",
# #        df_pokemony.sort_values("Attack", ascending = False)["Speed"].head(1))
# print('------------------ b ----- od Copilota ---')
# print( df_pokemony.loc[df_pokemony["Attack"].idxmax(), "Speed"])
print('------------------ c ----- Najwyższe Attack---')
max_Attack_row = df_pokemony.sort_values("Attack", ascending = False).head(1)
print('------------------ d ----- Najwyższe Attack---')
max_Attack_row = df_pokemony.sort_values("Attack").tail(1)
print (max_Attack_row)
print('------------------ e ----- Najwyższe Attack---')
print(max_Attack_row)
