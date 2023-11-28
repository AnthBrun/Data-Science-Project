import sys, os, glob, subprocess, time

if len(sys.argv) == 2:
    time.sleep(1)
    print(f"start converting txt to csv")
    directory_path = os.path.join(os.getcwd(), sys.argv[1])
    directory_path = os.path.join(directory_path)
    print(f"directory_path: {directory_path}")
    pattern = '*.txt'
    file_path = glob.glob(os.path.join(directory_path, pattern))
    print(f"filepath: {file_path}")
    files = [os.path.basename(file) for file in file_path]
    print(f"files : {files}")
    for file in files:
        path = os.path.join(directory_path, file)
        cmd = f"python3 replace_semicolon_with_comma.py {os.path.join(sys.argv[1], file)}"
        process = subprocess.Popen(cmd,shell=True)
        process.communicate()
        os.rename(path, os.path.splitext(path)[0]+".csv")        
else:
    print("usage: txt_file_to_csv.py [Directory]")
    print("txt_files_to_csv.py is not written as standalone.")
    print("Please prefer to use download_zip.py instead.")
