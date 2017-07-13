'''
A file with examples
'''
from  kolada_api import Kpi, Municipality

#METADATA = Kpi.metadata()
KPI = Kpi.kpi()
KPI_AS_LIST = Kpi.kpi(as_list='yes')
#METADATA_SEARCH = Kpi.metadata_search('räddning', 'K', 'operating_area')
METADATA_SEARCH_AS_LIST = Kpi.metadata_search('räddning', 'K', 'operating_area', 'yes')
KPIS = str(METADATA_SEARCH_AS_LIST).replace("\'","").replace('[', '').replace(']','').replace(' ', '')
#MUNICIPALITY_GROUP_MEMBERS = Municipality.group_members()
#DATA_KPI = Kpi.data_per_municipality('N00002', '0860')


if __name__ == '__main__':
    #print(METADATA)
    #print(KPI)
    #print(KPI_AS_LIST)
    #print(METADATA_SEARCH)
    print(METADATA_SEARCH_AS_LIST)
    print(Kpi.data_per_municipality(KPIS, '0860'))
    #print(MUNICIPALITY_GROUP_MEMBERS)
    #print(DATA_KPI)
    
