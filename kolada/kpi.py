import requests
from .kolada import Kolada
from kolada._json.structure import _metadata, _id_title, _data
from kolada._control._controls import _control_kpi
import kolada._json.structure as structure
import pandas as pd
import json
from typing import List, Dict, Union, Any


class Kpi(Kolada):
    def __init__(self, filter_=None):
        super().__init__()
        if isinstance(filter_, str):
            self._filter = filter_.upper()
        else:
            self._filter = None

    def __str__(self):
        return self.__class__

    def __repr__(self):
        print("hej")

    def kpi(self) -> Kolada:
        """
        Method that based on the parameters returns either kpi id and kpi name, kpi id or kpi name

        Args:
        **Keyword arguments:
            filter_kpis (str): Provides a possibilty to filters the kpis. 
                \'\' is the default option and it returns all kpis
                If \'K\' is passed only municipality kpis are returned
                If \'L\' is passed only county kpis are returned\n
            inner_type (str): Provides a possibilty to decide the inner type
                \'tuple\' is the default option and returns a list of tuples
                \'list\' returns a list of lists\n
            id_or_name (str): Provides a possibilty to only get the kpi id or the kpi name as a list
                '' is the default option and it returns both kpi id and kpi name according to the choices made in the other parameters
                \'id\' returns only the kpi id's as a list. The returned list depends on the choice in fílter_kpis but not inner_type 
                \'name\' returns only the kpi names's as a list. The returned list depends on the choice in fílter_kpis but not inner_type   
        
        Returns:
            list of tuples: [(\'id1\', \'name1\'), (\'id2\', \'name2\')...], default return type
            
            list of lists: [[\'id1\', \'name1\'], [\'id2\', \'name2\']...], if keyword argument
            inner_type equals \'list\'
            
            list: [\'id1\', \'id2\'...] or [\'name1\', \'name2\'...] depending on 
            keyword argument id_or_name equals \'id\' or \'name\'
        
        Raises:
            TypeError: If keyword argument not is str
            KeyError: If wrong key is supplied

        """
        values = self._kpi["values"]
        if not self._filter:
            self._data = [(str(group["id"]), str(group["title"])) for group in values]
        elif self._filter == "K":
            self._data = [
                (str(group["id"]), str(group["title"]))
                for group in values
                if group["municipality_type"] == "K"
            ]
        else:  # filter_kpis == 'L':
            self._data = [
                (str(group["id"]), str(group["title"]))
                for group in values
                if group["municipality_type"] == "L"
            ]
        self._columns = ["id", "title"]
        return self

    def group_names(self) -> Kolada:
        """kpigruppsid + kpigruppsnamn"""
        values = Kolada()._group_names["values"]
        self._data = [(str(group["id"]), str(group["title"])) for group in values]
        self._columns = structure.COLUMNS_ID_TITLE
        return self

    def group(self) -> Kolada:
        """kpigruppsid + kpiid"""
        values = Kolada()._group["values"]
        self._data = [
            (group["id"], members["member_id"])
            for group in values
            for members in group["members"]
        ]
        self._columns = structure.COLUMNS_ID_TITLE
        return self

    def metadata(self) -> Kolada:
        """
        metadata
        """
        values = Kolada()._kpi["values"]
        if not self._filter:
            self._data = [_metadata(group) for group in values]
        elif self._filter == "K":
            self._data = [
                _metadata(group)
                for group in values
                if group["municipality_type"] == "K"
            ]
        else:
            self._data = [
                _metadata(group)
                for group in values
                if group["municipality_type"] == "L"
            ]
        self._columns = structure.COLUMNS_METADATA
        return self

    def data_per_year(
        self, kpis: str, years: str, from_date: Union[None, str] = None
    ) -> Kolada:
        """
        data per given kpi,

        if the method returns None then eihter there is no KPI with the given 
        ID or there is no data for the given KPI during the given year
        """
        self.data = self._data_per_year(
            vars=kpis, years=years, _subclass=__class__.__name__, from_date=from_date
        )
        self._columns = structure.COLUMNS_DATA
        return self

    def data_per_municipality(
        self, kpis: str, municipalities: str, from_date: Union[None, str] = None
    ) -> Kolada:
        """
        """
        self.data = self._data_per_municipality(
            vars=kpis,
            municipalities=municipalities,
            _subclass=__class__.__name__,
            from_date=from_date,
        )
        self._columns = structure.COLUMNS_DATA
        return self

    def metadata_search(self, search_string: str, search_column="title") -> Kolada:
        """
        Search kpi
        """
        if not isinstance(search_string, str):
            raise TypeError(
                "the search string must be a string, e.g. 'Räddningstjänst'."
            )
        elif not isinstance(search_column, str):
            raise TypeError("search_column must be a string, e.g. 'operating_area'.")

        if search_column == "title":
            url = self.BASE + self.KPI + "?title=" + search_string
            values = requests.get(url).json()["values"]
            if not self._filter:
                self._data = [_metadata(group) for group in values]
            elif self._filter == "K":
                self._data = [
                    _metadata(group)
                    for group in values
                    if group["municipality_type"] == "K"
                ]
            else:
                self._data = [
                    _metadata(group)
                    for group in values
                    if group["municipality_type"] == "L"
                ]
        elif search_column == "operating_area":
            self._data = self._customColumnSearch(4, search_string, filter_kpis=None)
        elif search_column == "description":
            self._data = self._customColumnSearch(12, search_string, filter_kpis=None)
        self._columns = structure.COLUMNS_METADATA
        return self

    def _customColumnSearch(self, col, search_string, filter_kpis) -> List[Any]:
        """
        helper function
        """
        data = []
        data_origin = self.metadata()._data
        for row in data_origin:
            if search_string.upper() in str(list(row)[col]).upper():
                data.append(row)
            else:
                continue
        return data
