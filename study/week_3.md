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
우리가 작업하고자 하는 `HTML`파일 안에서 `<py-config>`태그를 활용하면, `Python`패키지를 사용할 수 있습니다.

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



## 2.3.3. Local Module 사용법과 예시 코드
https://docs.pyscript.net/latest/reference/elements/py-config.html#local-modules

## 2.3.4 추가 사용법과 예시 코드(gist)
