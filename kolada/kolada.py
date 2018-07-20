#!/usr/bin/env python
"""

"""
import requests
import tablib
import json
import warnings
from typing import List, Dict, Union, Any
from ._json.structure import _metadata, _id_title, _data, _ou_structure


class Kolada:
    """
    
    """

    BASE = "http://api.kolada.se/v2/"
    DATA = {
        "Kpi": ["data/", "kpi"],
        "Municipality": ["data/", "municipality"],
        "Ou": ["oudata/", "ou"],
    }
    KPI = "kpi"
    KPI_GROUP = "kpi_groups"
    MUNICIPALITY = "municipality"
    MUNICIPALITY_GROUP = "municipality_groups"
    OU = "ou"

    def __init__(self):
        self._data = []
        self._columns = []

    @property
    def _kpi(self):
        """
        """
        url = self.BASE + self.KPI
        return requests.get(url).json()

    @property
    def _group_names(self):
        """
        """
        url = self.BASE + self.KPI_GROUP
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
    def _ou(self):
        """
        """
        url = self.BASE + self.OU
        return requests.get(url).json()

    def _data_per_year(
        self, vars: str, years: str, _subclass: str, from_date: Union[None, str] = None
    ):
        """
        data per given kpi,

        if the method returns None then eihter there is no KPI with the given 
        ID or there is no data for the given KPI during the given year
        """
        if not isinstance(vars, str):
            raise TypeError(f"{_subclass}'s must be a string, e.g. 'N00002, N00003'.")
        elif not isinstance(years, str):
            raise TypeError('years must be  a string, e.g. "2016')
        if not from_date:
            _from = ""
        else:
            _from = "?from_date=" + from_date
        url = (
            self.BASE
            + self.DATA[_subclass][0]
            + self.DATA[_subclass][1]
            + "/"
            + vars
            + "/year/"
            + years
            + _from
        )
        # print(url)
        _temp_data: List = []
        while True:
            try:
                response = requests.get(url).json()
                if response["count"] == 0:
                    break
                else:
                    values = response["values"]
                    _page = [
                        _data(group=group, member=member, _subclass=_subclass)
                        for group in values
                        for member in group["values"]
                        if member["value"] is not None
                    ]
                    self._data = _temp_data + _page
                    url = response["next_page"]
            except KeyError:
                break
        # self._columns = structure.COLUMNS_DATA
        return self

    def _data_per_municipality(
        self,
        vars: str,
        municipalities: str,
        _subclass: str,
        from_date: Union[None, str] = None,
    ):
        """
        data per given municipality

        if the method returns None then eihter there is no KPI with the given 
        ID or there is no data for the given KPI for the given municipality
        """
        if not isinstance(vars, str):
            raise TypeError(
                f"{_subclass}'s must be a string, must be a string, e.g. 'N00002, N00003'."
            )
        elif not isinstance(municipalities, str):
            raise TypeError("municipalities must be a string, e.g. '0860'.")
        if not from_date:
            _from = ""
        else:
            _from = "?from_date=" + from_date
        url = (
            self.BASE
            + self.DATA[_subclass][0]
            + self.DATA[_subclass][1]
            + "/"
            + vars
            + "/"
            + self.MUNICIPALITY
            + "/"
            + municipalities
            + _from
        )
        _temp_data: List = []
        while True:
            try:
                response = requests.get(url).json()
                if response["count"] == 0:
                    break
                else:
                    values = response["values"]
                    _page = [
                        _data(group=group, member=member, _subclass=_subclass)
                        for group in values
                        for member in group["values"]
                        if member["value"] is not None
                    ]
                    self._data = _temp_data + _page
                    url = response["next_page"]
            except KeyError:
                break
        # self._columns = structure.COLUMNS_DATA
        return self

    @property  # write proper refernce to https://github.com/kennethreitz/records/blob/master/records.py
    def dataset(self):
        """A Tablib Dataset containing the row."""
        data = tablib.Dataset(*self._data, headers=self._columns)

        return data

    def export(
        self, format, **kwargs
    ):  # write proper refernce to https://github.com/kennethreitz/records/blob/master/records.py
        """Exports the row to the given format."""
        if self.countMaxLengthOfHeader() and format == "dbf":
            # hack because it is not possible to reset headers
            self._dbfWarning()
            _headers = [h[:10] for h in self._columns]
            data = tablib.Dataset(*self._data, headers=_headers)
            return data.export(format, **kwargs)
        else:
            return self.dataset.export(format, **kwargs)

    def list_of_tuples(self):
        """
        """
        return self._data

    def list_of_lists(self):
        """
        """
        return [list(data) for data in self._data]

    def countMaxLengthOfHeader(self) -> bool:
        """
        """
        _length = [0 if len(h) < 11 else 1 for h in self._columns]
        if sum(_length) == 0:
            return False
        else:
            return True

    @staticmethod
    def _dbfWarning():
        warnings.warn(
            ".dfb allows fields with a maximuim length of 10 characters. If one header is longer it gets truncated."
        )
