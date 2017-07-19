#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kolada_api` package."""


import unittest

from kolada import Kpi, Municipality


class TestPython_kolada_api(unittest.TestCase):
    """Tests for `python_boilerplate` package."""

    def test_000_something(self):
        """Test something."""
        with self.assertRaises(TypeError):
            Kpi.kpi(filter_kpis=1)

    '''    
    def test_001_something(self):
        """Test something."""
        with self.assertRaises(KeyError):
            Kpi.kpi(filter_kpis='s')
    '''

    def test_002_something(self):
        """Test something."""
        self.assertIsInstance(Kpi.kpi()[0], tuple)
    
    '''
    def test_003_something(self):
        """Test something."""
        self.assertIsInstance(Kpi.kpi(inner_type='list')[0], list)

    def test_004_something(self):
        """Test something."""
        with self.assertRaises(KeyError):
            Kpi.kpi(inner_type='str')
    '''

    def test_005_something(self):
        """Test something."""
        with self.assertRaises(TypeError):
            Kpi.kpi(inner_type=1)

            

if __name__ == '__main__':
    unittest.main()