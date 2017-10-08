#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kolada_api` package."""


import unittest

#from kolada import Kpi, Municipality
from context import kolada

class TestPython_kolada_api(unittest.TestCase):
    """Tests for `python_boilerplate` package."""

    def Kpi_type_000(self):
        """Test something."""
        with self.assertRaises(TypeError):
            kolada.Kpi.kpi(filter_kpis=1)

        
    def Kpi_Key_000(self):
        """Test something."""
        with self.assertRaises(KeyError):
            kolada.Kpi.kpi(filter_kpis='s')
    
    
    def Kpi_instance_tuple(self):
        """Test something."""
        self.assertIsInstance(kolada.Kpi.kpi()[0][0], tuple)
    
    
    def Kpi_instance_list(self):
        """Test something."""
        self.assertIsInstance(kolada.Kpi.kpi(inner_type='list')[0][0], list)
    
    def Kpi_key_001(self):
        """Test something."""
        with self.assertRaises(KeyError):
            kolada.Kpi.kpi(inner_type='str')
    

    def Kpi_type_001(self):
        """Test something."""
        with self.assertRaises(TypeError):
            kolada.Kpi.kpi(inner_type=1)

            

if __name__ == '__main__':
    unittest.main()