import requests
from .kolada import Kolada
from ._json.structure import _metadata, _id_title, _data, _ou
from ._control._controls import _control_kpi
import kolada._json.structure as structure
import pandas as pd
import json
from typing import List, Dict, Union, Any


class Ou(Kolada):
    """

    """

    def __init__(
            self,
            filter_=None,
    ):
        super().__init__()
        if isinstance(filter_, str):
            self._filter = filter_.upper()
        else:
            self._filter = None

    def ous(self, search_title='', search_municipality=''):
        """

        """
        data = []
        url = self.BASE + self.OU
        if search_title == '' and search_municipality == '':
            url = url
        elif search_title != '' and search_municipality == '':
            url += '?title=' + search_title
        elif search_title == '' and search_municipality != '':
            url += '?municipality=' + search_municipality
        elif search_title != '' and search_municipality != '':
            url += '?municipality=' + search_municipality + '&title=' + search_title
        result = None
        while result is None:
            try:
                response = requests.get(url).json()
                if response['count'] == 0:
                    break
                else:
                    values = response['values']
                    page = [_ou(group) for group in values]
                    data = data + page
                    url = response['next_page']
            except KeyError:
                break
        if data == []:
            return None
        else:
            self._data = data
            self._columns = ['id', 'municiplaity_id', 'title']
            return self


#    @classmethod
#    def data_per_year(cls, ous, years):
#        url = BASE + DATA + OU + ous
