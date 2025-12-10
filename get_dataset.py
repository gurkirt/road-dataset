import os
import glob
import gdown
import zipfile

road_root = os.path.dirname('./')

for f in glob.glob(os.path.join(road_root, '*.part')):
    os.remove(f)

# ROAD dataset downloading
if not os.path.exists(os.path.join(road_root, 'videos.zip')):
    gdown.download(
        'https://drive.google.com/uc?id=1YQ9ap3o9pqbD0Pyei68rlaMDcRpUn-qz', 
        os.path.join(road_root, 'videos.zip')
    )
if not os.path.exists(os.path.join(road_root, 'road_trainval_v1.0.json')):
    gdown.download(
        'https://drive.google.com/uc?id=1uoyBiNZq1_SHif1CG_2R6d_pUWwUe7fL', 
        os.path.join(road_root, 'road_trainval_v1.0.json')
    )

# ROAD dataset unpacking
if not glob.glob(os.path.join(road_root, 'videos', '*')):
    with zipfile.ZipFile(os.path.join(road_root, 'videos.zip'), "r") as zf:
        zf.extractall(road_root)

# ROAD dataset validation test
if (len(glob.glob(os.path.join(road_root, 'videos', '*.mp4'))) == 18 
    and os.path.exists(os.path.join(road_root, 'road_trainval_v1.0.json'))):
    print("ROAD downloaded successfully!")
    os.remove(os.path.join(road_root, 'videos.zip'))
else:
    raise FileNotFoundError('ROAD dataset not complete!')