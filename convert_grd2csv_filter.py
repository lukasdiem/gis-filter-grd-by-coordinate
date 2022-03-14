import glob
import os
import shutil
from tqdm import tqdm
from pyproj import Transformer

def parse_grd(filename):
    x = 0
    y = 0

    with open(filename) as f:
        try:
            # skip the first two lines
            f.readline()
            f.readline()
            # read the x/y coordinate
            text = f.readline().lower()
            x = float(text.split(' ')[-1].strip())
            text = f.readline()
            y = float(text.split(' ')[-1].strip())
        except Exception as e:
            print(f"Error at file: {filename}. Exception: {e}")

    return (x, y)



if __name__ == "__main__":
    out_filename = "gis_data.csv"
    out_folder1 = "./GrdSet1"
    out_folder2 = "./GrdSet2"

    try:
        os.mkdir(out_folder1)
        os.mkdir(out_folder2)
    except:
        pass
    
    grd_files = glob.glob("*.grd")

    # setup the coordinate transformation
    # from: MGI / Austria GK East => to: WGS 84
    transformer = Transformer.from_crs('EPSG:31256', 'EPSG:4326')
    
    with open(out_filename, 'w') as f_out:
        text = f"Dateiname,X,Y,Lon,Lat\n"
        f_out.write(text)

        for filename in tqdm(grd_files):
            x, y = parse_grd(filename)
            # transform the coordinates
            lat, lon = transformer.transform(y, x)
            text = f"{filename},{x},{y},{lon},{lat}\n"

            if (15.25 <= lon <= 16.45) and lat >= 48.25:
                shutil.copy(filename, out_folder1)
            if (lon >= 16.45) and (lat >= 48.25):
                shutil.copy(filename, out_folder2)

            f_out.write(text)