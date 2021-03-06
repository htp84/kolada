import requests
from kolada import Kolada
from kolada._json.structure import _metadata, _id_title, _data
from kolada._control._controls import _control_kpi
import kolada._json.structure as structure
import pandas as pd
import json
from typing import List, Dict, Union, Any


class Municipality(Kolada):
    """
    municipality data
    """

    def __init__(self, filter_=None):
        super().__init__()
        if isinstance(filter_, str):
            self._filter = filter_.upper()
        else:
            self._filter = None

    def __str__(self):
        return str(self.__class__)

    def __repr__(self):
        print("hej")

    def groups(self) -> Kolada:
        """Kommungruppsid + Kommungruppsnamn"""
        values = self._municipalityGroup["values"]
        self._data = [_id_title(group) for group in values]
        self._columns = structure.COLUMNS_ID_TITLE
        return self

    def groupMembers(self) -> Kolada:
        """Kommungruppsid + kommunid"""
        values = self._municipalityGroupMembers["values"]
        self._data = [
            (group["id"], members["member_id"])
            for group in values
            for members in group["members"]
        ]
        self._columns = structure.COLUMNS_ID_TITLE
        return self

    # TODO: move fiter to init, cretae mthod for mun id and rmove innertyåe
    def municipalities(self, municipality_id="n", inner_type="tuple") -> Kolada:
        """Hämtar kommuner samt deras metadata. Sätts municipality_id till yes eller ja
        hämtas endast en lista av kommunernas id"""
        if not isinstance(municipality_id, str):
            raise TypeError("municipality_id must be  a string")
        url = self.BASE + self.MUNICIPALITY
        values = requests.get(url).json()["values"]
        if not self._filter:
            if municipality_id.startswith("y") or municipality_id.startswith("j"):
                self._data = [(group["id"]) for group in values]
            else:
                self._data = [_id_title(group) for group in values]
        elif self._filter == "K":
            if municipality_id.startswith("y") or municipality_id.startswith("j"):
                self._data = [
                    (group["id"])
                    for group in values
                    if not group["id"].startswith("00")
                ]
            else:
                self._data = [
                    _id_title(group)
                    for group in values
                    if not group["id"].startswith("00")
                ]
        else:
            if municipality_id.startswith("y") or municipality_id.startswith("j"):
                self._data = [
                    (group["id"]) for group in values if group["id"].startswith("00")
                ]
            else:
                self._data = [
                    _id_title(group) for group in values if group["id"].startswith("00")
                ]
        self._columns = structure.COLUMNS_DATA
        return self

    def data_per_year(
        self, municipalities: str, years: str, from_date: Union[None, str] = None
    ) -> Kolada:
        """
        kpi
        """
        self.data = self._data_per_year(
            vars=municipalities,
            years=years,
            _subclass=__class__.__name__,
            from_date=from_date,
        )
        self._columns = structure.COLUMNS_DATA
        return self

