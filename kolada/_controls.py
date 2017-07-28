def _control_kpi(kwargs):
    for key, _ in kwargs.items():
        if key == 'filter_kpis' or key == 'inner_type' or key == 'id_or_name':
            pass
        else:
            raise KeyError('The only accepted keyword arguments are filter_kpis, inner_type and id_or_name')
    if 'filter_kpis' not in kwargs:
        filter_kpis = ''
    else:
        filter_kpis = kwargs['filter_kpis']
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
    return filter_kpis, inner_type, id_or_name  