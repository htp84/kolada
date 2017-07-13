
def _metadata(group):
    return  (group['id'],
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

def _id_title(group):
    return (group['id'],
            group['title'])

def _data(group, member):
    return (group['kpi'],
            group['municipality'],
            group['period'],
            member['value'],
            member['gender'])
