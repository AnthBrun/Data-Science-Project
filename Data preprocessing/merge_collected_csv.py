import pandas as pd
import sys

if len(sys.argv) == 3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    dataframe_1 = pd.read_csv(file1, parse_dates=["MESS_DATUM_BEGINN", "MESS_DATUM_ENDE"])
    dataframe_2 = pd.read_csv(file1, parse_dates=["MESS_DATUM_BEGINN", "MESS_DATUM_ENDE"])

    merged_df = pd.merge(dataframe_1, dataframe_2, on=["STATIONS_ID", "MESS_DATUM_BEGINN"], how="outer")
    merged_df = merged_df.sort_values(by=["STATIONS_ID", "MESS_DATUM_BEGINN"])

    filename_1 = sys.argv[1].split(".")
    filename_2 = sys.argv[2].split(".")
    print(filename_1[0])
    print(filename_2[0])
    merged_df.drop(["Unnamed: 0_x", "eor_x", "Unnamed: 0_y"])
    merged_df.to_csv(path_or_buf=(filename_1[0] + "_" + filename_2[0] + "_merged.csv"))
else:
    print("usage: merge_collected_csv.py [CSV] [CSV]")
