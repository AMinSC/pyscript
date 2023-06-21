# 2.3 Py-config

## 2.3.1 py-config란?
`HTML`안에서 `<py-config>` 태그를 사용하여 PyScript 애플리케이션의 종속성을 선언하는 것과 함께 일반 메타데이터를 설정하고 구성할 수 있습니다. 구성은 TOML(기본값) 또는 JSON 형식으로 설정해야 합니다.

- TOML 형식
    ```html
    <!-- 1 -->
    <py-config src="./custom.toml"></py-config>
    
    <!-- 2 -->
    <py-config>
    [[fetch]]
    files = ["./utils.py"]
    </py-config>
    ```

- JSON 형식
    ```html
    <!-- 1 -->
    <py-config type="json" src="./custom.json"></py-config>

    <!-- 2 -->
    <py-config>
    {
        "fetch": [{
        "files": ["./utils.py"]
        }]
    }
    </py-config>
    ```
    
- 1. src에 경로(`./custom.toml`)를 설정하거나,
    2. `<py-config>`태그 안에 직접 작성할 수 있습니다. 


- 참고: `<py-config>` 태그는 TOML과 JSON을 모두 지원하지만, 서로 다른 두 소스에서 전달된 구성 유형을 혼합할 수 없습니다. 즉, 인라인 구성은 TOML 형식이고 src의 구성은 JSON 형식인 경우는 허용되지 않습니다. 반대의 경우도 마찬가지입니다.

- `<py-config>` 요소는 `<body>` 요소 안에 배치하는것을 권고 합니다.

## 2.3.2 Package 사용법과 예시 코드
`PyScript`의 이점 중 하나라고 할 수 있는 `Python`의 패키지를 우리가 작업하고자 하는 `HTML`파일 안에서 `<py-config>`태그를 활용하면, 사용하고자 하는 `Python`패키지를 사용할 수 있습니다.

```html
<body>
    <py-config>
        package = ["random"]
    </py-config>
    <py-script>
        import random

        display(f'random (1 ~ 10) : {random.randint(1, 10)}')
    </py-script>
</body>
```
위 코드는 `random`패키지를 사용하여, f-string문법으로 1부터 10까지의 랜덤한 수가 display함수를 통해 웹에서 출력되도록 하는 코드입니다.

그 외에도 `Data Analysis`, `Machine Learning`, `Deep Learning`에서 주로 사용하는 `pandas`, `mabplotlib` 등등 사용할 수 있습니다.

## 2.3.3. Local Module 사용법과 예시 코드
만약, 사용하고자 하는 기능이 이전에 `Python`에서 만들었거나, `Python`으로 만들면 좋을 것 같은 `Function`과 `Class`를 `HTML`에서 사용하는 법을 알아보겠습니다.

알아보기에 앞서, `func.py`파일 내용이 아래와 같다고 가정하겠습니다.
```py
import random


class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed"
        else:
            return a / b


def random_add(num):
    return num + random.randint(1, 10)
```
`class`는 간단한 계산기를 구현했으며, `fucntion`의 경우 1부터 10 사이의 수를 랜덤하게 더해주는 기능을 구현했습니다.

이제 두 기능을 `<py-config>`태그를 활용해서 같은 경로에 있는`HTML`파일에서 사용하는 법을 알아보겠습니다.

```html
<!-- 생략 -->
<body>
    <py-config>
        files = ["func.py"]
    </py-config>
    <py-script>
        from func import Calculator
        from func import random_add


        select_num = int(input())
        answer_num = random_add(select_num)
        
        display(f'결과물 : {answer_num}')
    </py-script>
</body>
```


## 2.3.4 추가 사용법과 예시 코드(gist)
