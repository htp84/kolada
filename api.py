# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:07:25 2016
Updated on Tue Apr 04 22:04:00 2017

@author: Henric Sundberg

Alla funktioner i modulen använder sig av http://api.kolada.se/v2/ som bas.
För mer informattion om version 2 av koladas api se:
https://github.com/Hypergene/kolada/blob/master/README.rst

"""
__version__ = 0.1

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
    def group_names(cls) -> list:
        '''kpigruppsid + kpigruppsnamn'''
        # url = 'http://api.kolada.se/v2/kpi_groups'
        url = BASE + KPI_GROUP
        response = requests.get(url)
        values = response.json()['values']
        data = [(group['id'], group['title']) for group in values]
        return data
    # print(kpiGroupsTitle())

    @classmethod
    def group(cls) -> list:
        '''kpigruppsid + kpiid'''
        # url = 'http://api.kolada.se/v2/kpi_groups'
        url = BASE + KPI_GROUP
        response = requests.get(url)
        values = response.json()['values']
        data = [(group['id'], members['member_id'])
                for group in values for members in group['members']]
        return data

    @classmethod
    def metadata(cls, filter_kpis='') -> list:
        '''
        metadata
        '''
        filter_kpis = filter_kpis.upper()
        url = BASE + KPI
        response = requests.get(url).json()
        values = response['values']
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
    def data_yearly(cls, kpi_list: str, years: str) -> list:
        '''
        kpi
        '''
        url = BASE + DATA + KPI + '/' + kpi_list + '/year/' + years
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
    def data_per_municipality(cls, kpi_list: str, municipalities: str) -> list:
        '''
        kpi
        '''
        url = BASE + DATA + KPI + '/' + kpi_list + '/' + MUNICIPALITY + '/' + municipalities
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
            response = requests.get(url).json()
            values = response['values']
            #print(url)
            #print(values)
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
            data = ['emelie är söt']

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
        response = requests.get(url)
        values = response.json()['values']
        data = [(group['id'], group['title']) for group in values]
        return data

    @classmethod
    def group_members(cls) -> list:
        '''Kommungruppsid + kommunid'''
        # url = 'http://api.kolada.se/v2/municipality_groups'
        url = BASE + MUNICIPALITY_GROUP
        response = requests.get(url)
        values = response.json()['values']
        data = [(group['id'], members['member_id'])
                for group in values for members in group['members']]
        return data

    @classmethod
    def municipalities(cls, filter_municipalities='', municipality_id='n') -> list:
        '''Hämtar kommuner samt deras metadata. Sätts municipality_id till yes eller ja
        hämtas endast en lista av kommunernas id'''

        url = BASE + MUNICIPALITY
        response = requests.get(url)
        values = response.json()['values']
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


if __name__ == '__main__':
    #X = Kpi.metadata_search(search_string='räddning', filter_kpis='k',
    #                        search_column='operating_area') # type: A
    #X = Kpi.metadata().translate()
    #data = Kpi.data_yearly('N00002', '2016,2017')
    import csv
    #data = Kpi.metadata('k')
    #data = Municipality.municipalities('K')
    data = Municipality.groups()
    print(data)
    '''
    with open('municipalitygroups.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['MunicipalityGroupId', 'MunicipalityGroupName'])
        for row in data:
            csv_out.writerow(row)
    '''
    '''
    mu = ['0860','0821','0834','0840','0861','0862','0880','0881','0882','0883','0884','0885']
    years = ['2013','2014','2015','2016','2017']
    with open('test.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['Kpi', 'Municipality', 'Year', 'Value', 'Sex'])
    for m in mu:
        for y in years:
            data = Municipality.data_per_year(m, y)
            with open('test.csv', 'a') as out:
                csv_out = csv.writer(out)
                for row in data:
                    csv_out.writerow(row)
    '''

  
    #print(data, len(data))


#sprint(Kpi.metadata()[0:1])
#print(Municipality.group_members())
#print(Kpi.data_yearly('N00945', '2015,2016'))
#print(Kpi.data_per_municipality('N00945', '0860'))
#print(Municipality.data_per_year('086', '2016'))


# Ous, search strings
# https://github.com/Hypergene/kolada


# def kolada_data(data, year, urltype='', fromdate='', timeunit='', num=''):
#     '''Hämtar json data från kolada. Resultat innhehåller följande kolumner:
#        kpi, municipality, period, value och gender.


#        Keyword arguments:

#        data -- string, kpi id , tex 'N0002' och 'N0002,N0003' eller kommunid,
#        tex '0860' och '0860, 1860'. data måste anges;

#        year -- string eller range, år, tex '2014', '2014,2015' och
#        range(2010, 2015). det som anges i range är from tom istället för from
#        till som det är i original range(), tex range(2010, 2015) är
#        from 2010 tom 2015. year måste anges;

#        urltype -- string, default='', anger om man anropet baseras på kpi
#        eller kommun. Anges inget ('') eller en string som börjar på k så sätts
#        urltype till 'kpi\'. Annars sätts urltype till 'municipality\'

#        fromdate -- string, default='', datum i formatet yyyy-mm-dd,
#        tex '2015-01-01'. APIet kollar om datan har uppdaterats sedan det
#        angivna datumet. Har det inte upppdaterats finns det ingen data;

#        timeunit -- string, default='', istället för att ange ett datum
#        manuellt i fromdate anges här vilken enhet som man vill använda för att
#        ta bort dagar/veckor från dagens datum, 'days' eller 'weeks'. Denna
#        funkar endast om fromdate='' och num anges;

#        num -- int, default='', antal enheter som det ska räknas tillbaka från
#        dagens datum, används tillsammans med timeunit;


#        Antalet kpis (kommuner)/år som anges är begränsat av maxlängden för
#        urlen. Detta varierar mellan webbläsare. Finns det behov att gå igenom
#        flera kpis (kommuner) och/eller år så går det att skapa en lista av
#        kpis (kommuner)/år och göra en for loop som går igenom denna lista ett
#        nyckeltal/år i taget, tex:
#            for kpi in kpis:
#                koladaData(kpi, year,....)

#        Kombineras fromdate med timedelta och num så är fromdate default. Tex
#        ger print(koladaData(kpi, year, '2016-01-01', 'weeks', 1)) '2016-01-01'.


#        Returns: List of tuples i.e. [(a,b,c,d,e),(f,g,h,i,j),(k,l,m,n,o)] eller
#        None (om data saknas)'''

#     url = kolada_data_url(data, year, urltype, fromdate, timeunit, num)
#     print(url)
#     result = None
#     data = []
#     while result is None:  # 1
#         try:
#             response = requests.get(url).json()
#             if response['count'] == 0:
#                 break  # 2
#             else:
#                 values = response['values']
#                 page = [(group['kpi'],
#                          group['municipality'],
#                          group['period'],
#                          member['value'],
#                          member['gender'])
#                         for group in values for member in group['values']
#                         if member['value'] is not None]
#                 data = data + page
#                 url = response['next_page']
#                 # print(url)
#         except KeyError:
#             break  # 4
#     if data == []:
#         return None
#     else:
#         #data = [tuple(l) for l in data[0:]]
#         return data
#         # 1: http://stackoverflow.com/questions/4606919/in-python-try-until-no-error
#         #    en fullösning (?) för att starta while-loopen
#         # 2: avbryter loopen om data saknas
#         # 3: Hoppar över rader med None som värde, tar onödig plats i datbasen
#         # 4: Avbryter loopen om next_page saknas
#         # borde skirva in att om value= None så ska den hoppa över resultatet


# def kolada_data_url(data, year, urltype, fromdate, timeunit, num):
#     '''Används för att bestämma urln för KoladaData funktionen. För förklaring
#         av keywords se koladaDatas docstring. De olika testen förklaras nedan:

#         1: testar vad som ska anges i url'n, kpi/ eller municipality/

#         2: testar om kpis och year är tomma. Är någon av det så returnera
#         KeyError.

#         3: Kontrollerar så kpi (kommun) är sträng. Omdet inte är det så
#         returneras TypeError

#         4: Kontrollerar så year är sträng. Om det inte är det så castas year
#         om till sträng

#         5: Kontrollerar om endast ett år angivits. Har fler år angivits
#         så måste year vara sträng. Är det inte det så returneras TypeError

#         6: kontrollerar så inte kommunid kombineras med kpi i url'n

#         7: kontrollerar så inte kpiis kombineras med kommun i url'n

#         8: kontrollerar om fromdate har ett värde,har den ett värde så sätts
#         det på slutet i urln.

#         9: Kontrollerar om fromdate är tom och timeunit och num har ett
#         värde. Stämmer detta så anges ett url med ett datum baserat på
#         timunit och num.

#         10: om inte 8 eller 9 stämmer så anges ett url utan datum

#         11: om range funktionen används [range(x, y)] så gör denna om range
#         till sträng samt lägger stop året som slutår
#         '''

#     if urltype == '' or urltype.startswith('k'):  # 1
#         urltype = 'kpi/'
#     else:
#         urltype = 'municipality/'
#     if str(year).startswith('range'):  # 11
#         years = list(year)
#         endyear = [years[-1] + 1]
#         years.extend(endyear)
#         year = ','.join(str(year) for year in years)
#     if data == '' or year == '':  # 2
#         raise KeyError('kpis (kommun) och/eller year måste anges')
#     if isinstance(data, str) is False:  # 3
#         raise TypeError('kpis (kommuner) MÅSTE vara sträng')
#     if isinstance(year, str) is False and len(str(year)) == 4:  # 4
#         year = str(year)
#     if isinstance(year, str) is False and len(str(year)) != 4:  # 5
#         raise TypeError(
#             'Anges mer än ett år och range inte används så MÅSTE year vara sträng')
#     if data[0].isdigit() is True and urltype == 'kpi/':  # 6
#         raise ValueError('kommunid och kpi url ska ej kombineras: ' +
#                          'http://api.kolada.se/v2/data/' + urltype + data + '/year/' + year)
#     if data[0].isdigit() is False and urltype == 'municipality/':  # 7
#         raise ValueError('kpis och muniipality url ska ej kombineras: ' +
#                          'http://api.kolada.se/v2/data/' + urltype + data + '/year/' + year)
#     if fromdate != '':  # 8
#         url = 'http://api.kolada.se/v2/data/' + urltype + \
#             data + '/year/' + year + '?from_date=' + fromdate
#     elif fromdate == '' and timeunit != '' and num != '':  # 9
#         fromdate = str(datetime.date.today() -
#                        datetime.timedelta(**{timeunit: num}))
#         url = 'http://api.kolada.se/v2/data/' + urltype + \
#             data + '/year/' + year + '?from_date=' + fromdate
#     else:
#         url = 'http://api.kolada.se/v2/data/' + urltype + data + '/year/' + year  # 10
#     return url


