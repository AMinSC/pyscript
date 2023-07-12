## 1. 전국 휴게소 status

1. py-config 설정
    ```html
    <body>
        <py-config>
            packages = ["folium", "pandas", "numpy"]
            [[fetch]]
            from = "./data/"
            files = ["rest-area1.csv", "rest-area2.csv", "rest-area3.csv"]
        </py-config>
    </body>
    ```

2. PyScript
    ```html
    <py-script>
        import numpy as np
        import pandas as pd
        import folium


        m = folium.Map(
            location = [36.4989, 127.9606],
            zoom_start = 8
        )

        tooltip = 'Click!!'

        o = pd.read_csv('rest-area3.csv', encoding='CP949')

        
        for i in range(o.shape[0]):
            folium.Marker(
                [o.iloc[i]['위도'], o.iloc[i]['경도']],
                popup = f'<div style="width: 120px;"><strong>{o.iloc[i]["휴게소명"]}</strong><br> 전기차충전소유무 : <strong>{o.iloc[i]["전기차충전소유무"]}</strong><br> 세차장 : <strong>{o.iloc[i]["세차장"]}</strong><br> 휴게소대표음식명 : <strong>{o.iloc[i]["휴게소대표음식명"]}</strong></div>',
                tooltip = tooltip
            ).add_to(m)

        display(m, target='map')
    </py-script>
    <div id="map"></div>
    <py-repl auto-generate="true"></py-repl>
    ```

3. python
    ```python
    import numpy as np
    import pandas as pd
    import folium


    m = folium.Map(
        location = [36.4989, 127.9606],
        zoom_start = 8
    )

    tooltip = 'Click!!'

    o = pd.read_csv('rest-area3.csv', encoding='CP949')


    for i in range(o.shape[0]):
        folium.Marker(
            [o.iloc[i]['위도'], o.iloc[i]['경도']],
            popup = f'<div style="width: 120px;"><strong>{o.iloc[i]["휴게소명"]}</strong><br> 전기차충전소유무 : <strong>{o.iloc[i]["전기차충전소유무"]}</strong><br> 세차장 : <strong>{o.iloc[i]["세차장"]}</strong><br> 휴게소대표음식명 : <strong>{o.iloc[i]["휴게소대표음식명"]}</strong></div>',
            tooltip = tooltip
        ).add_to(m)

    m
    ```


출처 - inflearn : 공공데이터와 Folium(Python Library)으로 만드는 제주 오름 지도 안내 서비스
- https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8F%B4%EB%A6%AC%EC%9B%80-%EC%A7%80%EB%8F%84%EC%84%9C%EB%B9%84%EC%8A%A4/dashboard

- data
    1. https://www.data.go.kr/data/15025446/standard.do
    2. http://data.ex.co.kr/portal/rest/restList


## 2. 
