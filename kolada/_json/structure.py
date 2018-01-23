
def _metadata(group):
    return  (str(group['id']),
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
       
COLUMNS_METADATA = ['id',
                    'prel_publication_date',
                    'municipality_type',
                    'publ_period',
                    'operating_area',
                    'auspices',
                    'publication_date',
                    'perspective',
                    'is_divided_by_gender',
                    'ou_publication_date',
                    'has_ou_data',
                    'title',
                    'description']

def _id_title(group, inner_type):
    if inner_type.lower() == 'tuple':
        return (str(group['id']),
                str(group['title']))
    elif inner_type.lower() == 'list':
        return [str(group['id']),
                str(group['title'])]
    else:
        raise KeyError('inner_type can only be \'tuple\' or \'list\'.')

COLUMNS_ID_TITLE = ['id',
                    'title']

def _data(group, member):
    return (group['kpi'],
            group['municipality'],
            group['period'],
            member['value'],
            member['gender'])

COLUMNS_DATA = ['kpi',
                'municipality',
                'period',
                'value',
                'gender']

def _ou(group):
    return (group['id'],
            group['municipality'],
            group['title'])

