# from os.path import join, dirname, abspath
# import sys
# sys.path.append(join(dirname(abspath(__file__)), '..'))
import unittest

from pyircor import tau, tauap


# Test data
set1 = {
    'x': [0.897, 0.372, 0.908, 0.898, 0.661, 0.062, 0.177, 0.384, 0.498, 0.992],
    'y': [0.82, 0.406, 0.817, 0.953, 0.673, 0.073, 0.364, 0.547, 0.589, 0.988],
    'x_ties': [0.9, 0.4, 0.9, 0.9, 0.7, 0.1, 0.2, 0.4, 0.5, 1],
    'y_ties': [0.8, 0.4, 0.8, 1, 0.7, 0.1, 0.4, 0.5, 0.6, 1]
}

set2 = {
    'x': [0.266, 0.573, 0.202, 0.945, 0.629, 0.206, 0.687, 0.77, 0.718, 0.38],
    'y': [0.263, 0.843, 0.728, 0.928, 0.08, 0.114, 0.467, 0.641, 0.973, 0.644],
    'x_ties': [0.3, 0.6, 0.2, 0.9, 0.6, 0.2, 0.7, 0.8, 0.7, 0.4],
    'y_ties': [0.3, 0.8, 0.7, 0.9, 0.1, 0.1, 0.5, 0.6, 1, 0.6]
}

set3 = {
    'x': [0.185, 0.573, 0.944, 0.129, 0.468, 0.553, 0.761, 0.405, 0.976, 0.445],
    'y': [0.845, 0.272, 0.275, 0.924, 0.605, 0.334, 0.162, 0.872, 0.018, 0.25],
    'x_ties': [0.2, 0.6, 0.9, 0.1, 0.5, 0.6, 0.8, 0.4, 1, 0.4],
    'y_ties': [0.8, 0.3, 0.3, 0.9, 0.6, 0.3, 0.2, 0.9, 0, 0.2]
}


class TestPyircor(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures, if any."""

    def test_tau(self):
        self.assertAlmostEqual(tau.tau(set1['x'], set1['y']), 0.9111, delta=5e-5)
        self.assertAlmostEqual(tau.tau(set2['x'], set2['y']), 0.2889, delta=5e-5)
        self.assertAlmostEqual(tau.tau(set3['x'], set3['y']), -.6889, delta=5e-5)

        # check symmetry
        self.assertAlmostEqual(tau.tau(set1['y'], set1['x']), 0.9111, delta=5e-5)
        self.assertAlmostEqual(tau.tau(set2['y'], set2['x']), 0.2889, delta=5e-5)
        self.assertAlmostEqual(tau.tau(set3['y'], set3['x']), -.6889, delta=5e-5)

    def test_tau_a(self):
        # check that it's the same as tau when there are no ties
        self.assertAlmostEqual(tau.tau_a(set1['x'], set1['y']), 0.9111, delta=5e-5)
        self.assertAlmostEqual(tau.tau_a(set2['x'], set2['y']), 0.2889, delta=5e-5)
        self.assertAlmostEqual(tau.tau_a(set3['x'], set3['y']), -.6889, delta=5e-5)

        # and symmetry
        self.assertAlmostEqual(tau.tau_a(set1['y'], set1['x']), 0.9111, delta=5e-5)
        self.assertAlmostEqual(tau.tau_a(set2['y'], set2['x']), 0.2889, delta=5e-5)
        self.assertAlmostEqual(tau.tau_a(set3['y'], set3['x']), -.6889, delta=5e-5)

        # now with ties in y
        self.assertAlmostEqual(tau.tau_a(set1['x'], set1['y_ties']), 0.8889, delta=5e-5)
        self.assertAlmostEqual(tau.tau_a(set2['x'], set2['y_ties']), 0.3333, delta=5e-5)
        self.assertAlmostEqual(tau.tau_a(set3['x'], set3['y_ties']), -.6222, delta=5e-5)

    def test_tau_b(self):
        # check that it's the same as tau when there are no ties
        self.assertAlmostEqual(tau.tau_b(set1['x'], set1['y']), 0.9111, delta=5e-5)
        self.assertAlmostEqual(tau.tau_b(set2['x'], set2['y']), 0.2889, delta=5e-5)
        self.assertAlmostEqual(tau.tau_b(set3['x'], set3['y']), -.6889, delta=5e-5)

        # and symmetry
        self.assertAlmostEqual(tau.tau_b(set1['y'], set1['x']), 0.9111, delta=5e-5)
        self.assertAlmostEqual(tau.tau_b(set2['y'], set2['x']), 0.2889, delta=5e-5)
        self.assertAlmostEqual(tau.tau_b(set3['y'], set3['x']), -.6889, delta=5e-5)

        # now with ties
        self.assertAlmostEqual(tau.tau_b(set1['x_ties'], set1['y_ties']), 0.9398, delta=5e-5)
        self.assertAlmostEqual(tau.tau_b(set2['x_ties'], set2['y_ties']), 0.3765, delta=5e-5)
        self.assertAlmostEqual(tau.tau_b(set3['x_ties'], set3['y_ties']), -.6510, delta=5e-5)
        # and symmetry
        self.assertAlmostEqual(tau.tau_b(set1['y_ties'], set1['x_ties']), 0.9398, delta=5e-5)
        self.assertAlmostEqual(tau.tau_b(set2['y_ties'], set2['x_ties']), 0.3765, delta=5e-5)
        self.assertAlmostEqual(tau.tau_b(set3['y_ties'], set3['x_ties']), -.6510, delta=5e-5)

    def test_tauap(self):
        self.assertAlmostEqual(tauap.tauap(set1['x'], set1['y']), 0.8519, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap(set2['x'], set2['y']), 0.2504, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap(set3['x'], set3['y']), -.6971, delta=5e-5)

    def test_tauap_a(self):
        # check that it's the stauap.ame as tau_ap when there are no ties
        self.assertAlmostEqual(tauap.tauap_a(set1['x'], set1['y']), 0.8519, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_a(set2['x'], set2['y']), 0.2504, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_a(set3['x'], set3['y']), -.6971, delta=5e-5)

        # now with ties in y
        self.assertAlmostEqual(tauap.tauap_a(set1['x'], set1['y_ties']), 0.7454, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_a(set2['x'], set2['y_ties']), 0.2692, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_a(set3['x'], set3['y_ties']), -.5558, delta=5e-5)

    def test_tauap_b(self):
        # check that it's the stauap.ame as symmetric tau_ap when there are no ties
        self.assertAlmostEqual(tauap.tauap_b(set1['x'], set1['y']), 0.8333, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_b(set2['x'], set2['y']), 0.2880, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_b(set3['x'], set3['y']), -.668, delta=5e-5)

        # now with ties
        self.assertAlmostEqual(tauap.tauap_b(set1['x_ties'], set1['y_ties']), 0.7321, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_b(set2['x_ties'], set2['y_ties']), 0.297, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_b(set3['x_ties'], set3['y_ties']), -.7047, delta=5e-5)
        # and symmetry
        self.assertAlmostEqual(tauap.tauap_b(set1['y_ties'], set1['x_ties']), 0.7321, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_b(set2['y_ties'], set2['x_ties']), 0.297, delta=5e-5)
        self.assertAlmostEqual(tauap.tauap_b(set3['y_ties'], set3['x_ties']), -.7047, delta=5e-5)
    
    def test_all_ties_bmodels(self):
        # check all `b` models correctly outputs undefined numbers {-np.inf, +np.inf, np.nan}
        import math

        full_tie = [0] * 10
        for vec in [set1['x'], set2['x'], set3['x']]:
            res = tauap.tauap_b(vec, full_tie)
            judge = math.isnan(res) or math.isinf(res)
            self.assertEqual(judge, True)

            res2 = tauap.tauap_b(full_tie, vec)
            judge = math.isnan(res2) or math.isinf(res2)
            self.assertEqual(judge, True)