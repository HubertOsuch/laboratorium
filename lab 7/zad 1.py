import pandas as pd
data = {'Nr_albumu' : [7003, 6876, 5454, 6734, 7001],
        'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Władek'],
        'Nazwisko' : ['Nowak', 'Kowalski', 'Pietrucha', 'Czartoryski', 'Stefański'],
        'Wiek': [22, 21, 24, 23, 31],
        'Ocena': [4.5, 5.0, 3.5, 4.0, 4.0]}
df = pd.DataFrame(data)
print(df)
#a
for row in df.itertuples():
    if row.Ocena >4:
        print((row.Ocena, row.Imię),)
#b
print(df.sort_values('Ocena'))
#c
print(df.groupby('Ocena').get_group(4.0))
print(df.groupby('Ocena')['Wiek'].mean())
#d
pop_data = {'Nr_albumu' : [5454, 6734],
            'Ocena_poprawiona': [4.5, 4.5]}
pop_df = pd.DataFrame(pop_data)

dodane_df = pd.merge(df, pop_df, on='Nr_albumu')

print(dodane_df)
#e
df.to_csv('Studenci_grupaSLO2.csv', index=False)
#f
dane_z_pilku_df = pd.read_csv('Studenci_grupaSLO2.csv')
print(dane_z_pilku_df)
print("Wczytano poprawnie dane")
#g
nowy_student_df = {'Nr_albumu': 6997,
                'Imię': 'Karolina',
                'Nazwisko': 'Kozłowska',
                'Wiek': 25,
                'Ocena': 4.5}

nowy_df = df._append(nowy_student_df, ignore_index=True)

print(nowy_df)
#h
data = {'Nr_albumu' : [7003, 6876, 5454, 6734, 7001],
        'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Władek'],
        'Nazwisko' : ['Nowak', 'Kowalski', 'Pietrucha', 'Czartoryski', 'Stefański'],
        'Wiek': [22, 21, 24, 23, 31],
        'Ocena': [4.5, 5.0, 3.5, 4.0, 4.0]}
df = pd.DataFrame(data)
print(df)
unikalne_df = df['Ocena'].unique()
print("Unikalne wartości w kolumnie z ocenami: ", unikalne_df)
#i
ocena_5 = (df['Ocena'] == 5).sum()

print("Liczba studentów mających ocenę równą 5:", ocena_5)
