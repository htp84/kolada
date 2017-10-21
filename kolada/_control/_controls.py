def _control_kpi(kwargs):
    """
    TODO: Add docstring
          add raise keyerror if illegal keys exist
    """
    filter_kpis = kwargs.pop('filter_kpis', None)
    inner_type = kwargs.pop('inner_type', 'tuple')
    id_or_name = kwargs.pop('id_or_name', None)
    column_names = kwargs.pop('column_names', False)

    #raise KeyError('The only accepted keyword arguments are filter_kpis, inner_type and id_or_name')
    if filter_kpis is not None:
        if not isinstance(filter_kpis, str):
            raise TypeError('filter_kpis must be a string')
        if  filter_kpis.upper() != 'K' and filter_kpis.upper() != 'L' and filter_kpis is not None:
            raise KeyError('filter_kpis must be eiter \'\', \'L\' or \'K\'') 
        filter_kpis = filter_kpis.upper()
    if not isinstance(inner_type, str):
        raise TypeError('inner_type must be a string')
    if id_or_name is not None:
        if not isinstance(id_or_name, str):
            raise TypeError('id_or_name must be a string')
        if id_or_name != '' and id_or_name.lower() != 'id' and id_or_name.lower() != 'name':
            raise KeyError('id_or_name must either be \'\', \'id\' or \'name\'')
    if not isinstance(column_names, bool):
        raise TypeError('column_names must be boolean')
    
    return filter_kpis, inner_type, id_or_name, column_names