#!/usr/bin/env python
"""

"""
import requests
from kolada._json.structure import _metadata, _id_title, _data, _ou
from kolada._control._controls import _control_kpi
import kolada._json.structure as structure
import pandas as pd
import json
from typing import List, Dict, Union, Any


class Kolada():
    """
    
    """
    BASE = 'http://api.kolada.se/v2/'
    DATA = 'data/'
    KPI = 'kpi'
    KPI_GROUP = 'kpi_groups'
    MUNICIPALITY = 'municipality'
    MUNICIPALITY_GROUP = 'municipality_groups'
    OU = 'ou'

    def __init__(self, ):
        self._data = []
        self._columns = None

    @property
    def _kpi(self):
        """
        """
        url = self.BASE + 'kpi'
        return requests.get(url).json()

    @property
    def _group_names(self):
        """
        """
        url = self.BASE + 'kpi_groups'
        return requests.get(url).json()

    @property
    def _group(self):
        """
        """
        url = self.BASE + self.KPI_GROUP
        return requests.get(url).json()

    @property
    def _municipalityGroup(self):
        """
        """
        url = self.BASE + self.MUNICIPALITY_GROUP
        return requests.get(url).json()

    @property
    def _municipalityGroupMembers(self):
        url = self.BASE + self.MUNICIPALITY_GROUP
        return requests.get(url).json()

    @property
    def data(self):
        return self._data

    @property
    def columns(self):
        return self._columns

    @property
    def dataframe(self) -> pd.DataFrame:
        """

        """
        df = pd.DataFrame(data=self._data, columns=self.columns)
        return df

    @property
    def list_of_list(self):
        data = [list(i) for i in self._data]
        return data

    def to_excel(self, filename, columns=None):
        if not columns:
            df = self.dataframe
            df.to_excel(filename)
        else:
            self.dataframe[columns].to_excel(filename)

    def to_csv(self, path):
        self.dataframe.to_csv(path)
