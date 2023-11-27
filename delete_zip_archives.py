import os, sys, glob

if len(sys.argv) == 2:
    path = os.path.join(os.getcwd(), sys.argv[1])
    pattern = '*.zip'
    matches = glob.glob(os.path.join(path, pattern))
    for match in matches:
        os.remove(match)
else:
    print("usage: delete_zip_archives.py [Directory]")