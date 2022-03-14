import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument("lon", nargs=2, type=float, help="Longitudinal coordinate bounds (min, max)")
    parser.add_argument("lat", nargs=2, type=float, help="Latitudinal coordinate bounds (min, max)")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument("--crs_from", default='EPSG:31256', help="From Transformation (CRS Format, default=EPSG:31256). You can find the transforms here: https://epsg.io")
    parser.add_argument("--crs_to", default='EPSG:4326', help="To Transformation (CRS Format, default=EPSG:4326. You can find the transforms here: https://epsg.io")
    args = parser.parse_args()

    lon_bounds = sorted(args.lon)
    lat_bounds = sorted(args.lat)
    print(f"Bounds: Lon={lon_bounds}, Lat={lat_bounds}")
    print(f"Output Folder: {args.output_dir}")

    try:
        os.mkdir(args.output_dir)
    except:
        pass
    
    grd_files = glob.glob("*.grd")

    # setup the coordinate transformation
    # from: MGI / Austria GK East => to: WGS 84
    transformer = Transformer.from_crs(args.crs_from, args.crs_to)
    
    
    for filename in tqdm(grd_files):
        x, y = parse_grd(filename)
        # transform the coordinates
        lat, lon = transformer.transform(y, x)
        text = f"{filename},{x},{y},{lon},{lat}\n"

        if (lon_bounds[0] <= lon <= lon_bounds[1]) and (lat_bounds[0] <= lat <= lat_bounds[1]):
            shutil.copy(filename, args.output_dir)
