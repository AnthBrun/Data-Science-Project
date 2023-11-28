import requests, re, subprocess, sys
if len(sys.argv) != 2:
    print("usage: download_zip.py [url]")
else:
    url = sys.argv[1]
    website_text = requests.get(url).text
    pattern = r'[\w]+.zip'
    expressions_list = re.findall(pattern=pattern, string=website_text)
    expressions = set(expressions_list)

    i = 0
    for expression in expressions:
        download_url = f"{url}/{expression}"
        cmd = f"curl -s -O {download_url}"
        subprocess.Popen(cmd, shell=True)
        i += 1
    print("download finished\nstart collecting...")
    filename = expressions_list[0].split('_', 2)
    filename = filename[0] + '_' + filename[1]
    cmd = f"python3 push_zip_in_directory.py {filename}"
    process = subprocess.Popen(cmd, shell=True)
    process.communicate()

