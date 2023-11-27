import os, glob, shutil, sys, subprocess

if len(sys.argv) == 2:
    pattern = '*.zip'
    path = os.getcwd()
    dest_path = os.path.join(path, sys.argv[1])

    if not os.path.exists(dest_path):
        print("creating directory")
        os.makedirs(dest_path)

    matching_files = glob.glob(os.path.join(path, pattern))

    for match in matching_files:
        file = os.path.join(dest_path, os.path.basename(match))
        shutil.move(match, dest_path)
    
    print("collecting finished")
    cmd = f"python3 extract_txt_from_zip.py {os.path.basename(dest_path)}"
    process = subprocess.Popen(cmd, shell=True)
    process.communicate()
else: 
    print("usage: push_zip_in_directory [Filename]")
    print("push_zip_in_directory.py is not written as standalone.")
    print("Please prefer to use download_zip.py instead.")