# Data Repository Download and Preprocessing Scripts
These scripts are written for data-repository-urls like opendata.dwd.de with a huge amount of zip archieves. They are purposed to automatically donwload, organization and converting by a cascading direction. To preprocess the data you can use the scripts in the directory Data preprocessing.

## Usage
### Download and organize scripts:
1. Run 'download_zip.py': This script starts the download from all zip archives on the url.
2. The downloaded zip archives are collected in a directory named like the **first** archive (e.g. wetter_monatswerte).
3. The zip archives will be extracted by the scripts themself and collected in a txt_file directory.
4. Finally, the txt files will be converted from SSV to CSV files. 

**Note:** Each script is designed to start automatically the next step in the process.

### Data preprocessing 
1. Change to the Data preprocessing directory. Make sure you use the same directory tree as the scripts would build.
2. Collect all of your CSV files of one topic together in one CSV file with collect_csv.py.
3. Also you can merge two of your CVS files with merge_collected_csv.py

## Examples
```bash
python3 download_zip.py [data-repository-url]
```
```bash
python3 collect_csv [Directory]
python3 merge_collected_csv.py [csv1] [csv2]
```

&copy; by JuicyLady
