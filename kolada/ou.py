import requests
from .kolada import Kolada
from ._json.structure import _metadata, _id_title, _data, _ou_structure
from ._control._controls import _control_kpi
import kolada._json.structure as structure
import pandas as pd
import json
from typing import List, Dict, Union, Any


class Ou(Kolada):
    """

    """

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

    def ous(self, search_title="", search_municipality=""):
        """

        """
        url = None
        self._data: List = []
        counter = 0
        while True:
            try:
                if counter == 0:
                    response = self._ou
                else:
                    response = requests.get(url).json()
                if response["count"] == 0:
                    break
                else:
                    values = response["values"]
                    _page = [_ou_structure(group) for group in values]
                    print(_page[0])
                    self._data.extend(_page)
                    url = response["next_page"]
                    counter += 1
            except KeyError:
                break
        self._columns = ["id", "municipality", "title"]
        return self

    def data_per_year(
        self, ous: str, years: str, from_date: Union[None, str] = None
    ) -> Kolada:
        """
        data per given kpi,

        if the method returns None then eihter there is no KPI with the given 
        ID or there is no data for the given KPI during the given year
        """
        self.data = self._data_per_year(
            vars=ous, years=years, _subclass=__class__.__name__, from_date=from_date
        )
        self._columns = structure.COLUMNS_DATA
        return self

    def data_per_municipality(
        self, ous: str, municipalities: str, from_date: Union[None, str] = None
    ) -> Kolada:
        """
        data per given kpi,

        if the method returns None then eihter there is no KPI with the given 
        ID or there is no data for the given KPI during the given year
        """
        self.data = self._data_per_municipality(
            vars=ous,
            municipalities=municipalities,
            _subclass=__class__.__name__,
            from_date=from_date,
        )
        self._columns = structure.COLUMNS_DATA
        return self
