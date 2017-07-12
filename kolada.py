#!/usr/bin/env python
"""

"""
__version__ = 0.2

import requests

BASE = 'http://api.kolada.se/v2/'
DATA = 'data/'
KPI = 'kpi'
KPI_GROUP = 'kpi_groups'
MUNICIPALITY = 'municipality'
MUNICIPALITY_GROUP = 'municipality_groups'
#OU = 

class Kpi:
    '''
    kpi
    '''

    @classmethod
    def kpi(cls, filter_kpis='') -> list:
        '''
        Kpi id and name
        '''
        if not isinstance(filter_kpis, str):
            raise TypeError('filter_kpis must be  a string')
        filter_kpis = filter_kpis.upper()
        url = BASE + KPI
        values = requests.get(url).json()['values']
        if filter_kpis == '':
            data = [(group['id'],
                     group['title'])
                    for group in values]
        if filter_kpis == 'K':
            data = [(group['id'],
                     group['title'])
                    for group in values if group['municipality_type'] == 'K']
        if filter_kpis == 'L':
            data = [(group['id'],
                     group['title'])
                    for group in values if group['municipality_type'] == 'L']

        return data

    @classmethod
    def group_names(cls) -> list:
        '''kpigruppsid + kpigruppsnamn'''
        # url = 'http://api.kolada.se/v2/kpi_groups'
        url = BASE + KPI_GROUP
        values = requests.get(url).json()['values']
        data = [(group['id'], group['title']) for group in values]
        return data
    # print(kpiGroupsTitle())

    @classmethod
    def group(cls) -> list:
        '''kpigruppsid + kpiid'''
        # url = 'http://api.kolada.se/v2/kpi_groups'
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
            data = [(group['id'],
                     group['prel_publication_date'],
                     group['municipality_type'],
                     group['publ_period'],
                     group['operating_area'],
                     group['auspices'],
                     group['publication_date'],
                     group['perspective'],
                     group['is_divided_by_gender'],
                     group['ou_publication_date'],
                     str(group['has_ou_data']),
                     group['title'],
                     group['description'])
                    for group in values]
        if filter_kpis == 'K':
            data = [(group['id'],
                     group['prel_publication_date'],
                     group['municipality_type'],
                     group['publ_period'],
                     group['operating_area'],
                     group['auspices'],
                     group['publication_date'],
                     group['perspective'],
                     group['is_divided_by_gender'],
                     group['ou_publication_date'],
                     str(group['has_ou_data']),
                     group['title'],
                     group['description'])
                    for group in values if group['municipality_type'] == 'K']
        if filter_kpis == 'L':
            data = [(group['id'],
                     group['prel_publication_date'],
                     group['municipality_type'],
                     group['publ_period'],
                     group['operating_area'],
                     group['auspices'],
                     group['publication_date'],
                     group['perspective'],
                     group['is_divided_by_gender'],
                     group['ou_publication_date'],
                     str(group['has_ou_data']),
                     group['title'],
                     group['description'])
                    for group in values if group['municipality_type'] == 'L']

        return data


    @classmethod
    def data_yearly(cls, kpis: str, years: str) -> list:
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
        print(url)
        result = None
        data = []
        while result is None:  # 1
            try:
                response = requests.get(url).json()
                if response['count'] == 0:
                    break  # 2
                else:
                    values = response['values']
                    page = [(group['kpi'],
                             group['municipality'],
                             group['period'],
                             member['value'],
                             member['gender'])
                            for group in values for member in group['values']
                            if member['value'] is not None]
                    data = data + page
                    url = response['next_page']
                    # print(url)
            except KeyError:
                break  # 4
        if data == []:
            return None
        else:
            #data = [tuple(l) for l in data[0:]]
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
        print(url)
        result = None
        data = []
        while result is None:  # 1
            try:
                response = requests.get(url).json()
                if response['count'] == 0:
                    break  # 2
                else:
                    values = response['values']
                    page = [(group['kpi'],
                             group['municipality'],
                             group['period'],
                             member['value'],
                             member['gender'])
                            for group in values for member in group['values']
                            if member['value'] is not None]
                    data = data + page
                    url = response['next_page']
                    # print(url)
            except KeyError:
                break  # 4
        if data == []:
            return None
        else:
            #data = [tuple(l) for l in data[0:]]
            return data

    @classmethod
    def metadata_search(cls, search_string: str, filter_kpis='', search_column='title') -> list:
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
                data = [(group['id'],
                         group['prel_publication_date'],
                         group['municipality_type'],
                         group['publ_period'],
                         group['operating_area'],
                         group['auspices'],
                         group['publication_date'],
                         group['perspective'],
                         group['is_divided_by_gender'],
                         group['ou_publication_date'],
                         str(group['has_ou_data']),
                         group['title'],
                         group['description'])
                        for group in values]
            if filter_kpis.upper() == 'K':
                data = [(str(group['id']),
                         str(group['prel_publication_date']),
                         str(group['municipality_type']),
                         str(group['publ_period']),
                         str(group['operating_area']),
                         str(group['auspices']),
                         str(group['publication_date']),
                         str(group['perspective']),
                         str(group['is_divided_by_gender']),
                         str(group['ou_publication_date']),
                         str(group['has_ou_data']),
                         str(group['title']),
                         str(group['description']))
                        for group in values if group['municipality_type'] == 'K']
            if filter_kpis.upper() == 'L':
                data = [(group['id'],
                         group['prel_publication_date'],
                         group['municipality_type'],
                         group['publ_period'],
                         group['operating_area'],
                         group['auspices'],
                         group['publication_date'],
                         group['perspective'],
                         group['is_divided_by_gender'],
                         group['ou_publication_date'],
                         str(group['has_ou_data']),
                         group['title'],
                         group['description'])
                        for group in values if group['municipality_type'] == 'L']
        elif search_column == 'operating_area':
            data = helper_f(4)
        elif search_column == 'description':
            data = helper_f(12)
        else:
            data = None

        return data

class Municipality():
    '''
    municipality data
    '''

    @classmethod
    def groups(cls) -> list:
        '''Kommungruppsid + Kommungruppsnamn'''
        # url = 'http://api.kolada.se/v2/municipality_groups'
        url = BASE + MUNICIPALITY_GROUP
        values = requests.get(url).json()['values']
        data = [(group['id'], group['title']) for group in values]
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
    def municipalities(cls, filter_municipalities='', municipality_id='n') -> list:
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
                data = [(group['id'], group['title']) for group in values]
        if filter_municipalities == 'K':
            if municipality_id.startswith('y') or municipality_id.startswith('j'):
                data = [(group['id']) for group in values if not group['id'].startswith('00')]
            else:
                data = [(group['id'], group['title']) for group in values if not group['id'].startswith('00')]
        if filter_municipalities == 'L':
            if municipality_id.startswith('y') or municipality_id.startswith('j'):
                data = [(group['id']) for group in values if group['id'].startswith('00')]
            else:
                data = [(group['id'], group['title']) for group in values if  group['id'].startswith('00')]

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
        print(url)
        result = None
        data = []
        while result is None:  # 1
            try:
                response = requests.get(url).json()
                if response['count'] == 0:
                    break  # 2
                else:
                    values = response['values']
                    page = [(group['kpi'],
                             group['municipality'],
                             group['period'],
                             member['value'],
                             member['gender'])
                            for group in values for member in group['values']
                            if member['value'] is not None]
                    data = data + page
                    url = response['next_page']
                    # print(url)
            except KeyError:
                break  # 4
        if data == []:
            return None
        else:
            #data = [tuple(l) for l in data[0:]]
            return data

#class Ou:
#
#    @classmethod
#    def data_per_year(cls, ous, years):
#        url = BASE + DATA + OU + ous
