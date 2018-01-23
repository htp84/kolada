[![Build Status](https://travis-ci.org/htp84/kolada.svg?branch=master)](https://travis-ci.org/htp84/kolada)
[![Coverage Status](https://coveralls.io/repos/github/htp84/kolada/badge.svg?branch=master)(https://coveralls.io/github/htp84/kolada?branch=master)

## Kolada

The purpose of this api is to provide an easy way to download data from Kolada using Python 3. The API uses the [requests](https://github.com/requests/requests) module.

Supports Python **3.3+**

```python
>>> from kolada import Kpi
>>> DATA_KPI = Kpi.data_per_municipality('N00002', '0860')
>>> print(DATA_KPI)
```

For more information about kolada on github see [hypergene/kolada](https://github.com/Hypergene/kolada)

For more information on kolada in general see Koladas [homepage](https://www.kolada.se)
