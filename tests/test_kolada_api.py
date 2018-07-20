#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `kolada_api` package."""

import pytest
import pandas as pd
from pathlib import Path
import shutil

from kolada import Kolada, Kpi, Municipality, Ou

kolada = Kolada()
kpi = Kpi()

kpis = kpi.kpi()
groupnames = kpi.group_names()


def test_class_kpi_method_kpi():
    assert isinstance(kpis.list_of_list, list)
    assert isinstance(kpis.list_of_list[0], list)
    assert isinstance(kpis.data, list)
    assert isinstance(kpis.data[0], tuple)
    assert isinstance(kpis.dataframe, pd.DataFrame)
    assert isinstance(kpi.columns, list)
    assert isinstance(kpi.columns[0], str)


def test_class_kpi_method_group_names():
    assert isinstance(groupnames.list_of_list, list)
    assert isinstance(groupnames.list_of_list[0], list)
    assert isinstance(groupnames.data, list)
    assert isinstance(groupnames.data[0], tuple)
    assert isinstance(groupnames.dataframe, pd.DataFrame)
    assert isinstance(groupnames.columns, list)
    assert isinstance(groupnames.columns[0], str)


def test_class_kolada():
    assert isinstance(kolada._kpi, dict)
    assert isinstance(kolada._group, dict)
    assert isinstance(kolada._group_names, dict)
    assert isinstance(kolada._municipalityGroup, dict)
    assert isinstance(kolada._municipalityGroupMembers, dict)


def test_to_csv():
    p = Path('./TEMP')
    try:
        p.mkdir()
    except FileExistsError:
        pass
    name = 'testToCsv.csv'
    groupnames.to_csv(p / name)
    assert len(list(p.glob('**/*.csv'))) == 1
    shutil.rmtree(p)


def test_to_excel():
    p = Path('./TEMP')
    try:
        p.mkdir()
    except FileExistsError:
        pass
    name = 'testToExcel.xlsx'
    groupnames.to_excel(p / name)
    assert len(list(p.glob('**/*.xlsx'))) == 1
    shutil.rmtree(p)

    #rewrite for pytest
