# 2.3 Py-config

## 2.3.1 py-config란?
`<py-config>` 태그를 사용하여 `Python`패키지 혹은 모듈을 설정하고 구성할 수 있습니다. 


- 구성은 `TOML(기본값)` 또는 `JSON` 형식으로 설정해야 합니다.

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
    
1. src에 경로(`./custom.toml`)를 설정하거나,
2. `<py-config>`태그 안에 직접 작성할 수 있습니다. 


- 참고: `<py-config>` 태그는 `TOML`과 `JSON`을 모두 지원하지만, 서로 다른 두 소스에서 전달된 구성 유형을 혼합할 수 없습니다. 즉, 인라인 구성은 `TOML` 형식이고 src의 구성은 `JSON` 형식인 경우는 허용되지 않습니다. 반대의 경우도 마찬가지입니다.

- `<py-config>` 요소는 `<body>` 요소 안에 배치하는 것을 권고합니다.

- 앞으로 예시 코드는 `TOML`형식으로 진행하겠습니다.

## 2.3.2 Package 사용법과 예시 코드
`PyScript`의 이점 중 하나라고 할 수 있는 `Python`의 패키지를 우리가 작업하고자 하는 `HTML`파일에서 사용할 수 있습니다.
사용하기 위해서는 `HTML`파일 안에서 `<py-config>`태그를 활용하여, 사용하고자 하는 `Python`패키지를 호출한 뒤, 일반 `Python`에서 사용하듯이 `from`과 `import`로 활용하여 사용할 수 있습니다.

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
위 코드는 `random`패키지를 사용하여, f-string문법으로 1부터 10까지의 랜덤 한 수가 display함수를 통해 웹에서 출력되도록 하는 코드입니다.

그 외에도 `Data Analysis`, `Machine Learning`, `Deep Learning`에서 주로 사용하는 `pandas`, `mabplotlib` 등을 사용할 수 있습니다.

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
`class`는 간단한 계산기를 구현했으며, `fucntion`의 경우 1부터 10 사이의 수를 랜덤 하게 더해주는 기능을 구현했습니다. 

이제 두 기능을 `<py-config>`태그를 활용해서 같은 경로에 있는`HTML`파일에서 사용하는 법을 알아보겠습니다.

```html
<!-- 생략 -->
<body>
    <py-config>
        [[fetch]]
        from = '.'
        files = ["func.py"]
    </py-config>
    <py-script>
        from func import random_add
        from func import Calculator


        select_num = int(input())
        answer_num = random_add(select_num)
        display(f'1부터 10까지의 랜덤한 수를 더한 값 : {answer_num}')

        cal = Calculator()
        display(f'더하기 : {cal.add(2, answer_num)}')
        display(f'빼기 : {cal.sub(answer_num, 2)}')
        display(f'곱하기 : {cal.mul(2, answer_num)}')
        display(f'나누기 : {cal.div(answer_num, 2)}')
    </py-script>
</body>
```

`<py-config>`태그 안에는 우선 `[[fetch]]`를 통해서 `from`은 파일 경로, `files`는 파일 이름을 적어줍니다.
여기서 파일 이름은 확장자까지 적어줘야 합니다.


## 2.3.4 추가 사용법과 예시 코드
### gist 사용법
만약, 사용하고자 하는 코드가 로컬에 있는것이 아니라, GitHub gist에 있다고 가정한다면, 번거롭게 가까운 경로에 파일을 새로 생성하여 코드를 작성하고 저장하여 호출할 것입니다.

하지만, 위 방법 보다는 직접 gist주소를 전달하여 호출하는 방법을 알아보겠습니다.

방법은 간단 합니다.

먼저 사용하고자 하는 `Python`코드가 있는 `gist`페이지에 접속합니다.
![alt text](../asset/gist1.png)
그 다음 빨간 박스에 있는 `Raw`를 누르면 아래와 같은 상태가 됩니다.
![alt text](../asset/gist2.png)
그럼 빨간 박스에 해당하는 url을 복사해서 `<py-config>`의 `from`에서 경로 설정을 해주면 되는데 여기서 마지막 파일 이름은 제외시키고 파일 이름은 `files`에 적어 줍니다.

```html
<py-config>
    [[fetch]]
    from = "https://gist.githubusercontent.com/AMinSC/169b9f6c973690f9310528e465d10688/raw/27bb8acea57d407789b0940f8b127db9b9a837a4/"
    files = ["todo.py"]
</py-config>
```
그러고 나서 아래와 같이 사용하면 됩니다.
```html
<!-- index.html -->
 <py-script>
    from todo import add_task, dd_task_event
</py-script>
```
- from `<.py 파일 이름>` import `<.py파일에서 사용하고 싶은 함수 이름>`

### `<py-config>`에서 지원하는 value값
| Value  | Type | Description |
| ------------- | ------------- | ------------- |
| `version`  | string  | 사용자 애플리케이션의 버전입니다. PyScript버전과는 관련이 없습니다.  |
| `fetch`  | List of Stuff to fetch  | 로컬 Python 모듈 또는 인터넷의 리소스를 지정하여 호출할 수 있습니다.  |
| `plugins`  | List of Plugins  | 플러그인 목록을 여기에 지정합니다.  |
| `interpreters`  | List of Interpreters  | 오픈 소스코드를 불러올 수 있습니다.  |

이 외에도 다양한 value 값들이 있습니다.

### `fetch` 구성
| Value  | Type | Description |
| ------------- | ------------- | ------------- |
| `from`  | string  | 가져올 리소스의 기본 URL입니다.  |
| `files`  | List of strings  | 다운로드할 파일 목록입니다.  |
| `to_folder`  | string  | 파일 시스템에 생성할 폴더의 이름입니다.  |
| `to_file`  | string  | 파일 시스템에 생성할 대상의 이름입니다.  |

-  `to_file`과 `files`은 함께 사용할 수 없습니다.

- info.txt
    ```txt
    This is PyScript
    ```

1. 단일 파일 가져오기
    ```html
    <body>
        <py-config>
            [[fetch]]
            files = ['info.txt']
        </py-config>
        <py-script>
            with open('info.txt', 'r') as fp:
                print(fp.read())
        </py-script>
    </body>
    ```
    ![alt text](../asset/fetch1.png)

2. 가져온 단일 파일을 이름을 변경하여 사용
    ```html
    <py-config>
        [[fetch]]
        from = 'info.txt'
        to_file = 'info_loaded_from_web.txt'
    </py-config>
    <py-script>
        with open('info_loaded_from_web.txt', 'r') as fp:
            print(fp.read())
    </py-script>
    ```

3. 가져온 파일을 다른 폴더로 이동
    ```html
    <body>
        <py-config>
            [[fetch]]
            files = ['info.txt']
            to_folder = 'infofiles/loaded_info'
        </py-config>
        <py-script>
            with open('infofiles/loaded_info/info.txt', 'r') as fp:
                print(fp.read())
        </py-script>
    </body>
    ```

4. 가져온 파일을 이름을 변경하여 다른 폴더로 이동
    ```html
    <body>
        <py-config>
            [[fetch]]
            from = 'info.txt'
            to_folder = 'infofiles/loaded_info'
            to_file = 'info_loaded_from_web.txt'
        </py-config>
        <py-script>
            with open('infofiles/loaded_info/info_loaded_from_web.txt', 'r') as fp:
                print(fp.read())
        </py-script>
    </body>
    ```

5. Single file from a folder to the current working directory

6. Single file from a folder to another folder (i.e. not the current working directory)

7. Multiple files preserving directory structure

8. From an API endpoint which doesn’t end in a filename

<!-- https://docs.pyscript.net/latest/reference/elements/py-config.html#use-cases -->
