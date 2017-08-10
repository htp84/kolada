'''
A file with examples
'''
from kolada import Kpi, Municipality, Ou

#METADATA = Kpi.metadata()
#KPI = Kpi.kpi(filter_kpis='', id_or_name='name')
#KPI_AS_LIST = Kpi.kpi(inner_type='list')
#METADATA_SEARCH = Kpi.metadata_search('räddning', 'K', 'operating_area')
#METADATA_SEARCH_AS_LIST = Kpi.metadata_search('räddning', 'K', 'operating_area', 'yes')
#KPIS = str(METADATA_SEARCH_AS_LIST).replace("\'","").replace('[', '').replace(']','').replace(' ', '')
#MUNICIPALITY_GROUP_MEMBERS = Municipality.group_members()
#DATA_KPI = Kpi.data_per_municipality('N00002', '0860')
#data_m = Municipality.data_per_year('0860','2016')
#data_k = Kpi.data_per_year('N00002', '2016')
OU = Ou.ous(search_title='skola', search_municipality='0860')


if __name__ == '__main__':
    #print(METADATA)
    #print(KPI)
    #print(KPI_AS_LIST)
    #print(METADATA_SEARCH)
    #print(METADATA_SEARCH_AS_LIST)
    #print(Kpi.data_per_municipality(KPIS, '0860'))
    #print(MUNICIPALITY_GROUP_MEMBERS)
    #print(DATA_KPI)
    #print(data_k)
    print(OU)
    
