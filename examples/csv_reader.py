import csv

import leather

with open('examples/realdata/gii.csv') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)[:10]

    for row in data:
        row[1] = float(row[1]) if row[1] is not None else None

chart = leather.Chart('Data from CSV reader')
chart.add_bars(data, x=1, y=0)
chart.to_svg('examples/charts/csv_reader.svg')
