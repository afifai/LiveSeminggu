import requests
import argparse
import tqdm

def place(filename):
    ext = filename.split('.')[-1]
    if ext in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
        return "images"
    elif ext in ['mp4', 'mkv', 'flv', 'mpeg']:
        return 'videos'
    elif ext in ['exe', 'msi', 'dmg', 'sh']:
        return 'programs'
    elif ext in ['rar', 'zip', '7z']:
        return 'compressed'
    elif ext in ['pdf', 'ppt', 'doc', 'docx', 'xls', 'xlsx', 'pptx']:
        return 'documents'
    else:
        return 'others'

ap = argparse.ArgumentParser()
ap.add_argument('-l', '--link', required=True, help = 'Link File')
ap.add_argument('-v', '--verbose', default=True)
args = vars(ap.parse_args())

r = requests.get(args['link'], stream=True)
filename = args['link'].split('/')[-1]
file_size = int(r.headers['Content-Length'])
chunk = 1
chunk_size = 1024
num_bars = int(file_size / chunk_size)
verbose = args['verbose']
if verbose:
    print(f"ukuran file : {file_size}")
    print(f"jumlah bar : {num_bars}")

    with open('downloads/' + place(filename) + '/' + filename, 'wb') as fp:
        for chunk in tqdm.tqdm(
                                r.iter_content(chunk_size=chunk_size),
                                total=num_bars,
                                unit='KB',
                                desc='ukuran file & waktu download',
                                leave=True
                                ):
            fp.write(chunk)
