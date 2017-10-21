#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kolada_api` package."""


from context import kolada
import pytest


def test_Kpi_type_000():
    """Test something."""
    with pytest.raises(TypeError):
        kolada.Kpi.kpi(filter_kpis=1)

    
def test_Kpi_Key_000():
    """Test something."""
    with pytest.raises(KeyError):
        kolada.Kpi.kpi(filter_kpis='s')


def test_Kpi_instance_tuple():
    """Test something."""
    assert isinstance(kolada.Kpi.kpi()[0], tuple)


def test_Kpi_instance_list():
    """Test something."""
    assert isinstance(kolada.Kpi.kpi(inner_type='list')[0], list)

def test_Kpi_key_001():
    """Test something."""
    with pytest.raises(KeyError):
        kolada.Kpi.kpi(inner_type='str')


def test_Kpi_type_001():
    """Test something."""
    with pytest.raises(TypeError):
        kolada.Kpi.kpi(inner_type=1)

