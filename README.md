## Usage grd_filter_copy

Kopiert *.grd Dateien entsprechend ihrer Koordinaten.

**Wichtig:** Die *.grd Dateien müssen im Verzeichnis der exe Datei liegen!

Man gibt dafür die folgenden Parameter an:
> grd_filter_copy.exe LonMin LonMax LatMin LatMax Ausgabeverzeichnis

Optional kann noch die Transformation der Koordinaten angepasst werden:
> grd_filter_copy.exe LonMin LonMax LatMin LatMax Ausgabeverzeichnis --crs_from EPSG:31256 --crs_to EPSG:4326

Beispiel:

```bash
D:\tmp\gis-sarah>grd_filter_copy.exe 15.25 16.45 48.28 80 test
Bounds: Lon=[15.25, 16.45], Lat=[48.28, 80.0]
Output Folder: test
100%|████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 18.63it/s]
```

Die Hilfe kann wie folgt aufgerufen werden:
> grd_filter_copy.exe -h
