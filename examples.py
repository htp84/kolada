'''
A file with examples
'''
from  kolada_api import Kpi, Municipality

#METADATA = Kpi.metadata()
#KPI = Kpi.kpi()
METADATA_SEARCH = Kpi.metadata_search('räddning', 'K', 'operating_area')
#MUNICIPALITY_GROUP_MEMBERS = Municipality.group_members()

if __name__ == '__main__':
    #print(METADATA)
    #print(KPI)
    print(METADATA_SEARCH)
    #print(MUNICIPALITY_GROUP_MEMBERS)