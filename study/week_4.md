# 3.4 시각화 (데이터 분석) + py-repl로 데이터 처리가능
이번 장에서는 `<py-config>`태그로 Python Package를 구성하여 간단하게 시각화를 해보겠습니다.

## 3.4.1 matplotlib
Python에서 시각화 라이브러리로 matplotlib이 있습니다.
matplotlib 공식 사이트에서 몇가지 샘플로 시각화를 해보겠습니다.

### 간단한 예
우선 라이브러리를 모두 불러오겠습니다.
```html
<py-config>
    package = ["matplotlib", "numpy"]
</py-config>
```

그 다음 시각화를 하기에 앞서 `<py-script>`태그에 직접 작성하는 방법과 `<py-repl>`태그로 jupyter 환경처럼 작성하는 방법 2가지를 알아보겠습니다.

우선, `<py-config>`태그에 직접 작성하는 방법입니다.
```html
<script type="py">
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np

    
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

    display(plt, target="out")
</script>
<div id="out"></div>
```
여기서 display함수의 target파라미터값으로 원하는 태그값의 id를 설정해주면 해당 태그의 자식노드에 div태그가 생성되고 div태그의 자식노드에서 img태그를 통해 화면에 표시가 되며, 파라미터를 작성하지 않을경우 py-script태그의 자식노드에 동일하게 생성되어 화면에서 확인할 수 있습니다. 

![bar graph](../asset/display.png)


이번엔 `<py-repl>`태그를 활용해보겠습니다.
```html
<body>
    <py-config>
        packages = ["matplotlib", "numpy"]
    </py-config>
    <py-repl auto-generate="true"> </py-repl>
</body>
```

이제 아래의 코드를 작성하고 실행해봅니다.
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

plt
```

![bar graph](../asset/matplotlib.png)



이 장에서는 matplotlib 라이브러리를 깊게 배우기보단, PyScript에서 Python 라이브러리를 응용하여 시각화를 할 수 있음에 초점을 두겠습니다.

matplotlib 라이브러리에 관심이 있으시다면, 공식 홈페이지 가이드를 참고 부탁드리겠습니다.
https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py

### Lines, bars and markers(선, 막대 및 마커)
1. Bar Color
    ```html
    <body>
        <py-config>
            packages = ["matplotlib"]
        </py-config>

        <script type="py">
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()

            fruits = ['apple', 'blueberry', 'cherry', 'orange']
            counts = [40, 100, 30, 55]
            bar_labels = ['red', 'blue', 'red', 'orange']
            bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

            ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

            ax.set_ylabel('fruit supply')
            ax.set_title('Fruit supply by kind and color')
            ax.legend(title='Fruit color')

            display(plt, target="bar")
        </script>

        <div id="bar"></div>
    </body>
    ```

    ![bar graph](../asset/bar.png)


2. Grouped bar chart with labels
    ```html
    <body>
        <py-config>
            packages = ["matplotlib"]
        </py-config>

        <script type="py">
            # data from https://allisonhorst.github.io/palmerpenguins/

            import matplotlib.pyplot as plt
            import numpy as np

            species = ("Adelie", "Chinstrap", "Gentoo")
            penguin_means = {
                'Bill Depth': (18.35, 18.43, 14.98),
                'Bill Length': (38.79, 48.83, 47.50),
                'Flipper Length': (189.95, 195.82, 217.19),
            }

            x = np.arange(len(species))  # the label locations
            width = 0.25  # the width of the bars
            multiplier = 0

            fig, ax = plt.subplots(layout='constrained')

            for attribute, measurement in penguin_means.items():
                offset = width * multiplier
                rects = ax.bar(x + offset, measurement, width, label=attribute)
                ax.bar_label(rects, padding=3)
                multiplier += 1

            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax.set_ylabel('Length (mm)')
            ax.set_title('Penguin attributes by species')
            ax.set_xticks(x + width, species)
            ax.legend(loc='upper left')
            ax.set_ylim(0, 250)

            display(plt, target="graph-bar")
        </script>

        <div id="graph-bar"></div>
    </body>
    ```

    ![Grouped bar chart](../asset/group-bar.png)


### Images, contours and fields

1. Pseudocolor plots of unstructured triangular grids.

    ```html
    <body>
        <py-config>
            packages = ["matplotlib"]
        </py-config>

        <script type="py">
            import matplotlib.pyplot as plt
            import matplotlib.tri as tri
            import numpy as np

            
            # First create the x and y coordinates of the points.
            n_angles = 36
            n_radii = 8
            min_radius = 0.25
            radii = np.linspace(min_radius, 0.95, n_radii)

            angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
            angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
            angles[:, 1::2] += np.pi / n_angles

            x = (radii * np.cos(angles)).flatten()
            y = (radii * np.sin(angles)).flatten()
            z = (np.cos(radii) * np.cos(3 * angles)).flatten()

            # Create the Triangulation; no triangles so Delaunay triangulation created.
            triang = tri.Triangulation(x, y)

            # Mask off unwanted triangles.
            triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                                    y[triang.triangles].mean(axis=1))
                            < min_radius)


            fig1, ax1 = plt.subplots()
            ax1.set_aspect('equal')
            tpc = ax1.tripcolor(triang, z, shading='flat')
            fig1.colorbar(tpc)
            ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

            display(plt, target="Triangulation")
        </script>

        <div id="Triangulation"></div>
    </body>
    ```

    ![Triangulation](../asset/Triangulation.png)


2. Illustrate Gouraud shading.

    ```python
    fig2, ax2 = plt.subplots()
    ax2.set_aspect('equal')
    tpc = ax2.tripcolor(triang, z, shading='gouraud')
    fig2.colorbar(tpc)
    ax2.set_title('tripcolor of Delaunay triangulation, gouraud shading')
    plt
    ```

    ![Triangulation](../asset/Gouraud-shading.png)


외에도 정말 다양한 시각화 샘플 코드가 있습니다.
관심 있으시다면 공식 사이트 방문을 권장드립니다.
`https://matplotlib.org/stable/gallery/index.html`

## 3.4.2 pandas
데이터 분석에 용이한 DataFrame을 사용할 수 있는 라이브러리인 pandas가 있습니다. 
보통 json, csv파일을 load 하여 사용하지만 이번 장에서는 다른 data를 사용하지 않고 임의에 데이터로 실습해 보겠습니다.

### json, csv 파일을 불러서 DataFrame을 만들어보는 간단한 예시
파일을 만들기 전에 `data`라는 폴더를 만들고 `data`폴더 안에 `json`파일과 `csv`파일을 만들어 보겠습니다.
- data1.json
    ```json
    [
        {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
        {"id": 2, "name": "Bob", "age": 22, "city": "Los Angeles"},
        {"id": 3, "name": "Charlie", "age": 35, "city": "Chicago"}
    ]

    ```

- data2.json
    ```json
    [
        {"id": 4, "name": "David", "age": 29, "city": "Miami"},
        {"id": 5, "name": "Eve", "age": 40, "city": "Dallas"},
        {"id": 6, "name": "Frank", "age": 33, "city": "Boston"}
    ]

    ```

- data1.csv
    ```csv
    id,name,age,city
    1,Alice,30,New York
    2,Bob,22,Los Angeles
    3,Charlie,35,Chicago

    ```

- data2.csv
    ```csv
    id,name,age,city
    4,David,29,Miami
    5,Eve,40,Dallas
    6,Frank,33,Boston

    ```


1. `<py-config>`태그로 패키지를 불러올 때, 만들어준 폴더에서 파일들을 불러오기 위해 경로와 파일설정을 같이 해줍니다.
    ```html
    <body>
        <py-config>
            packages = ["pandas", "matplotlib"]
            [[fetch]]
            from = './data/'
            files = ["data1.json", "data2.json", "data1.csv", "data2.csv"]
        </py-config>
        <py-repl auto-generate="true"> </py-repl>
    </body>
    ```


2. `<py-repl>`태그로 `<py-config>`로 경로를 지정해준 `data`폴더의 데이터들을 불러서 확인 해보겠습니다.
    ```python
    import pandas as pd


    data1_json = pd.read_json('data1.json')
    data2_json = pd.read_json('data2.json')

    data1_csv = pd.read_csv('data1.csv')
    data2_csv = pd.read_csv('data2.csv')
    ```


3. CSVode에서 Go Live를 누르면 아래와 같은 창을 확인하실수 있습니다.
    ![dataframe](../asset/pandas_load.png)


4. html파일에서 `<py-script>`태그로 불러온 json, csv파일을 확장자끼리 concat메서드로 DataFrame으로 만들어 줍니다.
    ![dataframe](../asset/pandas_load2.png)


5. DataFrame 변수로 확인해봅니다.
    ![dataframe](../asset/pandas_load4.png)


6. 특정 로우값을 확인해보면 index가 중복되어 값도 중복으로 나오는것을 확인할 수 있습니다.
![dataframe](../asset/pandas_load5.png)


7. reset_index 메서드를 활용하여 index값을 초기화해준 뒤, 값을 확인합니다.
    ![dataframe](../asset/pandas_load6.png)


### 간단한 예
pandas는 데이터분석 라이브러리로 주로 jupyter notebook이나 colab으로 합니다.
우리는 pyscript의 `<py-config>`태그를 활용하겠습니다.

1. 활용하기에 앞서 기본 Dict형 데이터 틀과 함께 html파일을 아래와 같이 작성한 뒤에 Go Live하여 진행하겠습니다.
    ```html
    <body>
        <py-config>
            packages = ["pandas", "matplotlib"]
        </py-config>

        <script type="py">
            import pandas as pd
            import matplotlib.pyplot as plt

            # Creating a DataFrame
            data = {'Year': [2016, 2017, 2018, 2019, 2020],
                    'Sales': [200, 300, 250, 320, 400],
                    'Costs': [150, 200, 180, 220, 250]}

            # df = pd.DataFrame(data)

            display(data, target="out")
        </script>

        <div id="out"></div>
        <py-repl auto-generate="true"> </py-repl>
    </body>
    ```

    ![dataframe](../asset/pandas01.png)


2. Dict형 데이터를 pandas를 활용하여 DataFrame으로 변환해줍니다.
    ```python
    df = pd.DataFrame(data)
    df
    ```

    ![dataframe](../asset/pandas02.png)


3. 위에서 시각화 해주기 위해 사용하였던 라이브러리인 matplotlib을 사용하여 DataFrame형 데이터를 시각화 합니다.
    ```python
    # Plotting the data
    plt.figure(figsize=(10, 5))

    # Plotting Sales data
    plt.plot(df['Year'], df['Sales'], label='Sales', color='blue', marker='o')

    # Plotting Costs data
    plt.plot(df['Year'], df['Costs'], label='Costs', color='red', marker='o')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Amount in USD')
    plt.title('Yearly Sales and Costs')
    plt.legend()

    plt
    ```

    ![dataframe](../asset/pandas03.png)

- 먼저 필요한 라이브러리인 pandas 및 matplotlib.pyplot을 가져옵니다.

- key가 column name이고 value가 data 목록인 Dict를 사용하여 DataFrame을 만들었습니다.

- matplotlib.pyplot을 사용하여 'Year' col 위에 'Sales' 및 'Costs' col의 선 도표를 만들었습니다.

- label, title, legend(범례)를 추가하여 플롯을 보다 유익하게 만들었습니다.

- 마지막으로 plt.show()를 사용하여 플롯을 표시하지만, `py-repl`에서는 plt로 표시했습니다.


### Table Visualization
이번에는 DataFrame의 데이터를 보기 좋게 시각화 하는법입니다.

1. 기존 DataFrame
    ```html
    <body>
        <py-config>
            packages = ["pandas", "numpy", "matplotlib", "Jinja2"]
        </py-config>

        <script type="py">
            import pandas as pd
            import numpy as np
            import matplotlib as mpl
            
            df = pd.DataFrame({
                "strings": ["Adam", "Mike"],
                "ints": [1, 3],
                "floats": [1.123, 1000.23]
            })
            data = df.style \
            .format(precision=3, thousands=".", decimal=",") \
            .format_index(str.upper, axis=1) \
            .relabel_index(["row 1", "row 2"], axis=0)
            display(data, target="out")
        </script>

        <div id="out"></div>
        <py-repl auto-generate="true"> </py-repl>
    </body>
    ```

    - Jinja2란?
        Jinja2는 Data와 Template를 결합하여 Documents를 렌더링 해주는 Python용 템플릿 엔진 입니다.

    ![dataframe](../asset/dataframe.png)


2. style 메서드로 시각화를 곁들인 DataFrame
    ```python
    weather_df = pd.DataFrame(np.random.rand(10,2)*5,
                            index=pd.date_range(start="2021-01-01", periods=10),
                            columns=["Tokyo", "Beijing"])

    def rain_condition(v):
        if v < 1.75:
            return "Dry"
        elif v < 2.75:
            return "Rain"
        return "Heavy Rain"

    def make_pretty(styler):
        styler.set_caption("Weather Conditions")
        styler.format(rain_condition)
        styler.format_index(lambda v: v.strftime("%A"))
        styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="YlGnBu")
        return styler

    weather_df
    ```

    ![dataframe](../asset/dataframe2.png)


    ```python
    weather_df.loc["2021-01-04":"2021-01-08"].style.pipe(make_pretty)
    ```

    ![dataframe](../asset/dataframe3.png)


## 3.4.3 scikit-learn (보류) or 데이터를 읽어와서 사용
scikit-learn이란 Python 프로그래밍 언어 용 머신러닝 라이브러리입니다.
오픈소스로써 누구나 사용할 수 있고, 해당 라이브러리에는 머신러닝용 데이터와 각종 알고리즘을 제공하고 있습니다.

우리는 scikit-learn을 PyScript에서 활용해보겠습니다.

1. `<py-config>`태그에 필요한 Python 라이브러리를 설정하고, 위에서 언급했던 것처럼 `<py-repl>`태그를 활용하겠습니다.
    ```html
    <body>
        <py-config>
            packages = ["pandas", "numpy", "matplotlib", "scikit-learn"]
        </py-config>
        <py-repl auto-generate="true"> </py-repl>
    </body>
    ```


2. sklearn 라이브러리로 붗꽃(iris) 데이터를 받아와서 그중에 5개의 raw값을 확인하겠습니다.
    ```python
    import numpy as np
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
    from sklearn.compose import ColumnTransformer

    X, y = load_iris(as_frame=True, return_X_y=True)
    sepal_cols = ["sepal length (cm)", "sepal width (cm)"]
    petal_cols = ["petal length (cm)", "petal width (cm)"]

    preprocessor = ColumnTransformer(
        [
            ("scaler", StandardScaler(), sepal_cols),
            ("kbin", KBinsDiscretizer(encode="ordinal"), petal_cols),
        ],
        verbose_feature_names_out=False,
    ).set_output(transform="pandas")

    X_out = preprocessor.fit_transform(X)
    X_out.sample(n=5, random_state=0)
    ```

    ![dataframe](../asset/sklearn-ml.png)


3. 머신러닝 알고리즘으로 학습
    ```python
    from sklearn.datasets import load_diabetes
    from sklearn.ensemble import HistGradientBoostingRegressor

    X, y = load_diabetes(return_X_y=True, as_frame=True)

    hist_no_interact = HistGradientBoostingRegressor(
        interaction_cst=[[i] for i in range(X.shape[1])], random_state=0
    )
    hist_no_interact.fit(X, y)
    ```

    ![dataframe](../asset/sklearn-ml2.png)


4. 예측된 오류값을 시각화 합니다.
    ```python
    import matplotlib.pyplot as plt
    from sklearn.metrics import PredictionErrorDisplay

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    _ = PredictionErrorDisplay.from_estimator(
        hist_no_interact, X, y, kind="actual_vs_predicted", ax=axs[0]
    )
    _ = PredictionErrorDisplay.from_estimator(
        hist_no_interact, X, y, kind="residual_vs_predicted", ax=axs[1]
    )
    ```

    ![dataframe](../asset/sklearn-ml3.png)


![dataframe](../asset/sklearn.png)

<!-- http 다운로드? 에러 및 마무리 멘트 작성, 전반적 오타 검토 및 멘트 확인 -->

- repl 옵션 확인하기
- https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn-datasets-load-iris
