"""
Strip out the latitude and longitude for food spots and put them in their own columns to keep Google Fusion Tables happy
"""
import csv
import os

import settings

def main():
    stripTable(settings.TABLE_FILE_LOC)

def stripTable(table_loc):
    name, ext = os.path.splitext(table_loc)
    newName = name + "_fusion" + ext
    with open(table_loc) as f, open(newName, 'w') as w:
        reader = csv.reader(f)
        writer = csv.writer(w)

        header = next(reader)
        header.extend(['Lat', 'Long'])
        writer.writerow(header)

        for row in reader:
            location = row[4]
            beginCoordIndex = location.find('(')
            endCoordIndex = location.find(')')
            coordinatesString = location[beginCoordIndex + 1:endCoordIndex]
        
            latLong = []
            for item in coordinatesString.split(','):
                latLong.append(item.strip())
            
            row.extend(latLong)
            writer.writerow(row)

if __name__ == '__main__': main()
