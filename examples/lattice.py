import leather

data1 = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

data2 = [
    (3, 4),
    (3, 4),
    (5, 6),
    (7, 10),
    (8, 2)
]

data3 = [
    (2, 4),
    (3, 5),
    (6, 2),
    (8, 3),
    (10, 5)
]

lattice = leather.Lattice()
lattice.add_many([data1, data2, data3], titles=['First', 'Second', 'Third'])
lattice.to_svg('examples/charts/lattice.svg')
