import os, sys, glob
import pandas as pd
import numpy as np

if len(sys.argv) == 2:
    Path = os.path.join("..\\", sys.argv[1])
    Path = os.path.join(Path + "\\txt_files")
    file_name = sys.argv[1] + "_collected.csv"
    print(Path)

    csv_files = [f for f in os.listdir(Path) if f.endswith(".csv")]

    merged_df = pd.DataFrame()

    for csv_file in csv_files:
        file_path = os.path.join(Path, csv_file)
        single_df  = pd.read_csv(file_path, parse_dates=["MESS_DATUM_BEGINN", "MESS_DATUM_ENDE"])
        merged_df = pd.concat([merged_df, single_df], ignore_index=True)
    
    merged_df = merged_df.sort_values(by=["MESS_DATUM_BEGINN"])

    merged_df.to_csv(file_name)
else:
    print("usage: collect_csv.py [CSV]")