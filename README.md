[![Build Status](https://travis-ci.org/htp84/kolada.svg?branch=master)](https://travis-ci.org/htp84/kolada)

## Kolada

The purpuse of this api is to provide an easy way to download data from Kolada using Python 3. The API uses the [requests](https://github.com/requests/requests) module.

Supports Python **3.6**

```python
>>> from kolada import Kpi
>>> kpi = Kpi()
>>> result = kpi.data_per_municipality('N00002', '0860').data
>>> print(data))
```

For more information about kolada on github see [hypergene/kolada](https://github.com/Hypergene/kolada)

For more information on kolada in general see Koladas [homepage](https://www.kolada.se)
