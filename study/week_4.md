# 3.4 시각화 (데이터 분석) + py-repl로 데이터 처리가능
이번 장에서는 `<py-config>`태그로 Python Package를 구성하여 간단하게 시각화를 해보겠습니다.

## 3.4.1 matplotlib
Python에서 시각화 라이브러리로 matplotlib이 있습니다.
matplotlib 공식 사이트에서 몇가지 샘플로 시각화를 해보겠습니다.

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
            bar_labels = ['red', 'blue', '_red', 'orange']
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

    ```html
    <!-- 생략 -->
    fig2, ax2 = plt.subplots()
    ax2.set_aspect('equal')
    tpc = ax2.tripcolor(triang, z, shading='gouraud')
    fig2.colorbar(tpc)
    ax2.set_title('tripcolor of Delaunay triangulation, gouraud shading')
    <!-- 생략 -->
    ```

    ![Triangulation](../asset/Gouraud-shading.png)


외에도 정말 다양한 시각화 샘플 코드가 있습니다.
관심 있으시다면 공식 사이트 방문을 권장드립니다.
`https://matplotlib.org/stable/gallery/index.html`

## 3.4.2 pandas

```html
<body>
    <py-config>
        packages = ["pandas"]
    </py-config>

    <script type="py">
        import pandas as pd
        
        data = pd.DataFrame(
            {
                'A': [1, 2, 3],
                'B': [4, 5, 6],
                'C': [7, 8, 9],
                'D': [10, 11, 12]},
            )


        display(data, target="out")
    </script>

    <div id="out"></div>
    <py-repl></py-repl>
</body>
```

![dataframe](../asset/dataframe.png)

- `<py-repl>`태그를 활용하여 시각화 해주기
- https://pandas.pydata.org/docs/user_guide/style.html#Formatting-the-Display

## 3.4.3 sklearn (보류) or 데이터를 읽어와서 사용

- repl 옵션 확인하기
- https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#measure-and-plot-the-results
