import csv

import leather

with open('examples/realdata/gii.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)[:10]

    for row in data:
        mmr = row['Maternal mortality ratio']
        row['Maternal mortality ratio'] = float(mmr) if mmr is not None else None

chart = leather.Chart('Data from CSV reader')
chart.add_bars(data, x='Maternal mortality ratio', y='Country')
chart.to_svg('examples/charts/csv_dict_reader.svg')
