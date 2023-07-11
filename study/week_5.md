```python
import numpy as np
import pandas as pd
import folium
```

```html
<body>
    <py-config>
        packages = ["numpy", "pandas", "folium"]
        [[fetch]]
        from = "./data/"
        files = ["o.csv"]
    </py-config>
    <py-repl auto-generate="true"> </py-repl>
</body>
```

```python
m = folium.Map(
    location = [33.3684, 126.5291],
    zoom_start = 10
)

tooltip = 'Click!!'

folium.Marker(
    [33.3684, 126.5291],
    popup = '<strong>한라산</strong>',
    tooltip = tooltip,
    icon = folium.Icon(color='#ff0000', icon='info-sign')
).add_to(m)

folium.Marker(
    [33.5104, 126.4913],
    popup = '<strong>제주국제공항</strong>',
    tooltip = tooltip,
    icon = folium.Icon(color='green', icon='bookmark')
).add_to(m)

folium.Marker(
    [33.3684, 126.5291],
    popup = '<strong>바울랩</strong>',
    tooltip = tooltip
).add_to(m)

m
```

- data
    https://www.data.go.kr/data/15096996/fileData.do


```python

o = pd.read_csv('o.csv')
o
```

```python
m = folium.Map(
    location = [33.3684, 126.5291],
    zoom_start = 10
)

tooltip = 'Click!!'

for i in range(o.shape[0]):
    folium.Marker(
        [o.iloc[i]['위도'], o.iloc[i]['경도']],
        popup = f"<strong>{o.iloc[i]['오름명']}</strong>",
        tooltip = tooltip
    ).add_to(m)

m
```

출처 - inflearn : 공공데이터와 Folium(Python Library)으로 만드는 제주 오름 지도 안내 서비스
