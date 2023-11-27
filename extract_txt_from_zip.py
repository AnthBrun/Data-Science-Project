import zipfile, os, sys, glob, re, subprocess

if len(sys.argv) == 2:
    print(f"start extracting files from {sys.argv[1]}")
    directory_path = os.path.join(os.getcwd(), sys.argv[1])

    txt_path = os.path.join(directory_path, "txt_files")
    if not os.path.exists(txt_path):
        target_path = os.makedirs(txt_path)

    print(txt_path)
    matching_zip_path = glob.glob(os.path.join(directory_path, '*.zip'))
    for match in matching_zip_path:
        with zipfile.ZipFile(match, 'r') as zip_ref:
            file = [file for file in zip_ref.namelist() if re.match(r'produkt_[\w]*.txt', file)]
            zip_ref.extract(file[0], txt_path)

    cmd = f"python3 txt_files_to_csv {txt_path}"
    process = subprocess.Popen(cmd, shell=True)
    process.communicate()
else:
    print("usage: [Directory]")
    print("extract_txt_from_zip.py is not written as standalone.")
    print("Please prefer to use download_zip.py instead.")