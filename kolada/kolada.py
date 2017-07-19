#!/usr/bin/env python
"""

"""
import requests
from kolada.json_.structure import _metadata, _id_title, _data

BASE = 'http://api.kolada.se/v2/'
DATA = 'data/'
KPI = 'kpi'
KPI_GROUP = 'kpi_groups'
MUNICIPALITY = 'municipality'
MUNICIPALITY_GROUP = 'municipality_groups'
#OU =

class Kpi:
    """
    
    """

    @classmethod
    def kpi(cls, filter_kpis='', **kwargs) -> list:
        """
        Method that based on the parameters returns either kpi id and kpi name, kpi id or kpi name

        Parameters
        ----------
        filter_kpis : string, optional
                      Provides a possibilty to filters the kpis. 
                      \'\' is the default option and it returns all kpis
                      If \'K\' is passed only municipality kpis are returned
                      If \'L\' is passed only county kpis are returned\n
        inner_type : string, keyword argument
                     Provides a possibilty to decide the inner type
                     \'tuple\' is the default option and returns a list of tuples
                     \'list\' returns a list of lists\n
        id_or_name : string, keyword argument
                     Provides a possibilty to only get the kpi id or the kpi name as a list
                     '' is the default option and it returns both kpi id and kpi name according to the choices made in the other parameters
                     \'id\' returns only the kpi id's as a list. The returned list depends on the choice in fílter_kpis but not inner_type 
                     \'name\' returns only the kpi names's as a list. The returned list depends on the choice in fílter_kpis but not inner_type   
        
        Returns
        -------
        list of tuples
                      [(\'id1\', \'name1\'), (\'id2\', \'name2\')...]
        or
        list of lists
                      [[\'id1\', \'name1\'], [\'id2\', \'name2\']...]
        or
        list
            [\'id1\', \'id2\'...] 
        or 
        list
            [\'name1\', \'name2\'...]
        """
        data = None
        if not isinstance(filter_kpis, str):
            raise TypeError('filter_kpis must be a string')
        if  filter_kpis.upper() != 'K' and filter_kpis.upper() != 'L' and filter_kpis != '':
            raise KeyError('filter_kpis must be eiter \'\', \'L\' or \'K\'')        
        if 'inner_type' not in kwargs:
            inner_type = 'tuple'            
        else:
            inner_type = kwargs['inner_type']
            if not isinstance(inner_type, str):
                raise TypeError('inner_type must be a string')
        if 'id_or_name' not in kwargs:
            id_or_name = ''
        else:
            id_or_name = kwargs['id_or_name']
            if not isinstance(id_or_name, str):
                raise TypeError('id_or_name must be a string')
            if id_or_name != '' and id_or_name.lower() != 'id' and id_or_name.lower() != 'name':
                raise KeyError('id_or_name must either be \'\', \'id\' or \'name\'')            
        filter_kpis = filter_kpis.upper()
        url = BASE + KPI
        values = requests.get(url).json()['values']
        if filter_kpis == '':
            data = [_id_title(group, inner_type) for group in values]
        elif filter_kpis == 'K':
            data = [_id_title(group, inner_type) for group in values if group['municipality_type'] == 'K']
        elif filter_kpis == 'L':
            data = [_id_title(group, inner_type) for group in values if group['municipality_type'] == 'L']
        if id_or_name == 'id':
            data = [id[0] for id in data]
        elif id_or_name == 'name':
            data = [name[1] for name in data]
        return data

    @classmethod
    def group_names(cls, inner_type='tuple') -> list:
        '''kpigruppsid + kpigruppsnamn'''
        url = BASE + KPI_GROUP
        values = requests.get(url).json()['values']
        data = [_id_title(group, inner_type) for group in values]
        return data

    @classmethod
    def group(cls) -> list:
        '''kpigruppsid + kpiid'''
        url = BASE + KPI_GROUP
        values = requests.get(url).json()['values']
        data = [(group['id'], members['member_id'])
                for group in values for members in group['members']]
        return data

    @classmethod
    def metadata(cls, filter_kpis='') -> list:
        '''
        metadata
        '''
        if not isinstance(filter_kpis, str):
            raise TypeError('filter_kpis must be  a string')
        filter_kpis = filter_kpis.upper()
        url = BASE + KPI
        values = requests.get(url).json()['values']
        if filter_kpis == '':
            data = [_metadata(group) for group in values]
        if filter_kpis == 'K':
            data = [_metadata(group) for group in values if group['municipality_type'] == 'K']
        if filter_kpis == 'L':
            data = [_metadata(group) for group in values if group['municipality_type'] == 'L']
        return data


    @classmethod
    def data_per_year(cls, kpis: str, years: str) -> list:
        '''
        data per given kpi,

        if the method returns None then eihter there is no KPI with the given 
        ID or there is no data for the given KPI during the given year
        '''
        if not isinstance(kpis, str):
            raise TypeError('kpis must be a string, e.g. \'N00002, N00003\'.')
        elif not isinstance(years, str):
            raise TypeError('years must be  a string, e.g. "2016')
        url = BASE + DATA + KPI + '/' + kpis + '/year/' + years
        result = None
        data = []
        while result is None:
            try:
                response = requests.get(url).json()
                if response['count'] == 0:
                    break
                else:
                    values = response['values']
                    page = [_data(group, member)
                            for group in values for member in group['values']
                            if member['value'] is not None]
                    data = data + page
                    url = response['next_page']
            except KeyError:
                break
        if data == []:
            return None
        else:
            return data

    @classmethod
    def data_per_municipality(cls, kpis: str, municipalities: str) -> list:
        '''
        data per given municipality

        if the method returns None then eihter there is no KPI with the given 
        ID or there is no data for the given KPI for the given municipality
        '''
        if not isinstance(kpis, str):
            raise TypeError('kpis must be a string, e.g. \'N00002, N00003\'.')
        elif not isinstance(municipalities, str):
            raise TypeError('municipalities must be a string, e.g. \'0860\'.')
        url = BASE + DATA + KPI + '/' + kpis + '/' + MUNICIPALITY + '/' + municipalities
        result = None
        data = []
        while result is None:
            try:
                response = requests.get(url).json()
                if response['count'] == 0:
                    break
                else:
                    values = response['values']
                    page = [_data(group, member)
                            for group in values for member in group['values']
                            if member['value'] is not None]
                    data = data + page
                    url = response['next_page']
            except KeyError:
                break
        if data == []:
            return None
        else:
            return data

    @classmethod
    def metadata_search(cls, search_string: str, filter_kpis='', search_column='title', as_list='no') -> list:
        '''
        Search kpi
        '''
        if not isinstance(search_string, str):
            raise TypeError('the search string must be a string, e.g. \'Räddningstjänst\'.')
        elif not isinstance(filter_kpis, str):
            raise TypeError('filter_kpis must be a string, either \'\', \'K\' or \'L\'.')
        elif not isinstance(search_column, str):
            raise TypeError('search_column must be a string, e.g. \'operating_area\'.')

        def helper_f(col):
            '''
            helper function
            '''
            data = []
            data_origin = Kpi.metadata(filter_kpis=filter_kpis)
            for row in data_origin:
                if search_string.upper() in str(list(row)[col]).upper():
                    data.append(row)
                else:
                    continue
            return data

        if search_column == 'title':
            url = BASE + KPI + '?title=' + search_string
            values = requests.get(url).json()['values']
            if filter_kpis == '':
                data = [_metadata(group) for group in values]
            if filter_kpis.upper() == 'K':
                data = [_metadata(group) for group in values if group['municipality_type'] == 'K']
            if filter_kpis.upper() == 'L':
                data = [_metadata(group) for group in values if group['municipality_type'] == 'L']
        elif search_column == 'operating_area':
            data = helper_f(4)
        elif search_column == 'description':
            data = helper_f(12)
        else:
            data = None
        if as_list.lower() == 'yes' and data is not None:
            data = [id[0] for id in data]
        return data

class Municipality():
    '''
    municipality data
    '''

    @classmethod
    def groups(cls, inner_type='tuple') -> list:
        '''Kommungruppsid + Kommungruppsnamn'''
        url = BASE + MUNICIPALITY_GROUP
        values = requests.get(url).json()['values']
        data = [_id_title(group, inner_type) for group in values]
        return data

    @classmethod
    def group_members(cls) -> list:
        '''Kommungruppsid + kommunid'''
        url = BASE + MUNICIPALITY_GROUP
        values = requests.get(url).json()['values']
        data = [(group['id'], members['member_id'])
                for group in values for members in group['members']]
        return data

    @classmethod
    def municipalities(cls, filter_municipalities='', municipality_id='n', inner_type='tuple') -> list:
        '''Hämtar kommuner samt deras metadata. Sätts municipality_id till yes eller ja
        hämtas endast en lista av kommunernas id'''
        if not isinstance(filter_municipalities, str):
            raise TypeError('filter_municipalities must be a string')
        elif not isinstance(municipality_id, str):
            raise TypeError('municipality_id must be  a string')
        url = BASE + MUNICIPALITY
        values = requests.get(url).json()['values']
        if filter_municipalities == '':
            if municipality_id.startswith('y') or municipality_id.startswith('j'):
                data = [(group['id']) for group in values]
            else:
                data = [_id_title(group, inner_type) for group in values]
        if filter_municipalities == 'K':
            if municipality_id.startswith('y') or municipality_id.startswith('j'):
                data = [(group['id']) for group in values if not group['id'].startswith('00')]
            else:
                data = [_id_title(group, inner_type) for group in values if not group['id'].startswith('00')]
        if filter_municipalities == 'L':
            if municipality_id.startswith('y') or municipality_id.startswith('j'):
                data = [(group['id']) for group in values if group['id'].startswith('00')]
            else:
                data = [_id_title(group, inner_type) for group in values if  group['id'].startswith('00')]
        return data

    @classmethod
    def data_per_year(cls, municipalities: str, years: str) -> list:
        '''
        kpi
        '''
        if not isinstance(municipalities, str):
            raise TypeError('municipalities must be a string')
        elif not isinstance(years, str):
            raise TypeError('years must be  a string')
        url = BASE + DATA + MUNICIPALITY + '/' + municipalities + '/' + 'year' + '/' + years
        result = None
        data = []
        while result is None:
            try:
                response = requests.get(url).json()
                if response['count'] == 0:
                    break
                else:
                    values = response['values']
                    page = [_data(group, member)
                            for group in values for member in group['values']
                            if member['value'] is not None]
                    data = data + page
                    url = response['next_page']
            except KeyError:
                break
        if data == []:
            return None
        else:
            return data

#class Ou:
#
#    @classmethod
#    def data_per_year(cls, ous, years):
#        url = BASE + DATA + OU + ous
