[![Build Status](https://travis-ci.org/htp84/kolada.svg?branch=master)](https://travis-ci.org/htp84/kolada)

## Kolada

The purpuse of this api is to provide an easy way to download data from Kolada using Python 3. The API uses the [requests](https://github.com/requests/requests) module.

Supports Python **3.3+**

```python
>>> from kolada_api import Kpi, Municipality
>>> data_m = Municipality.data_per_year('0860','2017')
>>> data_k = Kpi.data_per_year('N00002', '2017')
>>> print(data_m, data_k)
```

For more information about kolada on github see [hypergene/kolada](https://github.com/Hypergene/kolada)

For more information on kolada in general see Koladas [homepage](https://www.kolada.se)
