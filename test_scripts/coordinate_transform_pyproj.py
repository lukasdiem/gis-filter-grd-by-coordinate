
from pyproj import Proj, transform

inProj = Proj(init='epsg:31256')
outProj = Proj(init='epsg:4326')
x1,y1 = (-96250.5, 319999.5)
x2,y2 = transform(inProj,outProj,x1,y1)
print (x2,y2)

from pyproj import Transformer
transformer = Transformer.from_crs('EPSG:31256', 'EPSG:4326')

x1,y1 = (-96250.5, 319999.5)
x3, y3 = transformer.transform(y1, x1)
print (x3,y3)