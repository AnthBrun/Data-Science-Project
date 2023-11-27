import sys, os

if len(sys.argv) == 2:
    print(f"start replacing in {sys.argv[1]}")
    file = os.path.join(sys.argv[1])
    data = ""
    with open(file, 'r') as txt:
        data = txt.read()

    data = data.replace(';',',')

    with open(file, 'w') as txt:
        txt.write(data)        
    print("finish")
else:
    print("usage: replace_semicolon_with_comma.py [File]")