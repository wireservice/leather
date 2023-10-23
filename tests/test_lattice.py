import leather


class TestLattice(leather.LeatherTestCase):
    def setUp(self):
        self.data1 = [
            (0, 3),
            (4, 5),
            (7, 9),
            (8, 4)
        ]

        self.data2 = [
            (0, 4),
            (1, 3),
            (2, 5),
            (5, 6),
            (9, 10)
        ]

    def test_add_one(self):
        lattice = leather.Lattice()
        lattice.add_one(self.data1)
        lattice.add_one(self.data2)

        svg = self.render_chart(lattice)

        self.assertElementCount(svg, '.axis', 4)
        self.assertElementCount(svg, '.series', 2)
        self.assertElementCount(svg, '.lines', 2)

    def test_add_many(self):
        lattice = leather.Lattice()
        lattice.add_many([self.data1, self.data2, self.data1])

        svg = self.render_chart(lattice)

        self.assertElementCount(svg, '.axis', 6)
        self.assertElementCount(svg, '.series', 3)
        self.assertElementCount(svg, '.lines', 3)

    def test_bars(self):
        data1 = [
            (2, 'foo'),
            (6, 'bar'),
            (9, 'bing')
        ]

        data2 = [
            (3, 'foo'),
            (5, 'bar'),
            (7, 'bing')
        ]

        lattice = leather.Lattice(shape=leather.Bars())
        lattice.add_many([data1, data2])

        svg = self.render_chart(lattice)

        self.assertElementCount(svg, '.axis', 4)
        self.assertElementCount(svg, '.series', 2)
        self.assertElementCount(svg, '.bars', 2)

    def test_bars_different(self):
        data1 = [
            (3, 'foo'),
            (5, 'bar'),
            (9, 'bing')
        ]

        data2 = [
            (3, 'foo'),
            (5, 'bar'),
            (9, 'baz')
        ]

        lattice = leather.Lattice(shape=leather.Bars())
        lattice.add_many([data1, data2])

        svg = self.render_chart(lattice)

        self.assertElementCount(svg, '.axis', 4)
        self.assertElementCount(svg, '.series', 2)
        self.assertElementCount(svg, '.bars', 2)
