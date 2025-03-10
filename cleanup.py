import pandas as pd

csv_path = "/Users/erjon/Library/CloudStorage/OneDrive-AlteKantonsschuleAarau/BBB/Module/2. Jahr/M259/LB/charts.csv"

print("Lese CSV ein... Bitte warten (kann etwas dauern bei großen Dateien).")
df = pd.read_csv(csv_path)

print("Datei erfolgreich eingelesen!")
print("Anzahl Zeilen:", len(df))

df_small = df.head(10000)

df_small.drop_duplicates(inplace=True)

df_small.dropna(axis=1, how="all", inplace=True)

output_path = "charts_cleaned_sample.csv"
df_small.to_csv(output_path, index=False)

print("Bereinigte CSV gespeichert als:", output_path)
print("Zeilen in der verkleinerten CSV:", len(df_small))
