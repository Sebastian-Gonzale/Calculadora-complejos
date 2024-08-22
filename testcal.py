import calculator1 as lc
import unittest 

class TestCplxOperations(unittest.TestCase):

    # Prueba para cplxsum
    def test_cplxsum(self):
        suma = lc.cplxsum((3, 5), (-2.6, 6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)

        suma = lc.cplxsum((2, 2), (2, 2))
        self.assertAlmostEqual(suma[0], 4)
        self.assertAlmostEqual(suma[1], 4)

    # Prueba para cplxrest
    def test_cplxrest(self):
        resta = lc.cplxrest((3, 5), (-2.6, 6.8))
        self.assertAlmostEqual(resta[0], 5.6)
        self.assertAlmostEqual(resta[1], -1.8)

        resta = lc.cplxrest((2, 2), (2, 2))
        self.assertAlmostEqual(resta[0], 0)
        self.assertAlmostEqual(resta[1], 0)

    # Prueba para clpxmult
    def test_clpxmult(self):
        producto = lc.clpxmult((3, 5), (-2.6, 6.8))
        self.assertAlmostEqual(producto[0], -41.8)
        self.assertAlmostEqual(producto[1], 7.4)

        producto = lc.clpxmult((2, 2), (2, 2))
        self.assertAlmostEqual(producto[0], 0)
        self.assertAlmostEqual(producto[1], 8)
    
    # Prueba para clpxdiv
    def test_clpxmdiv(self):

        division = lc.clpxmdiv((2, 2), (2, 2))
        self.assertAlmostEqual(division[0], 1)
        self.assertAlmostEqual(division[1], 0)
    
    # Prueba para clpxmou
    def test_clpxmou(self):
        modulo = lc.clpxmou((3, 5))
        self.assertAlmostEqual(modulo, 5.830951894845301)

        modulo = lc.clpxmou((2, 2))
        self.assertAlmostEqual(modulo, 2.8284271247461903)
    
    # Prueba para clpxconj
    def test_clpxconj(self):
        conjugado = lc.clpxconj((3, 5))
        self.assertAlmostEqual(conjugado[0], 3)
        self.assertAlmostEqual(conjugado[1], -5)

        conjugado = lc.clpxconj((2, 2))
        self.assertAlmostEqual(conjugado[0], 2)
        self.assertAlmostEqual(conjugado[1], -2)

if __name__ == "__main__":
    unittest.main()
