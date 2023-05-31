# Using the fetch from py-config

이 장에서는 `py-config`와 `py-script` 태그를 활용하여 다른 `.py`파일 안에 함수들을 `index.html`파일에서 `import`하여 사용하는 방법을 알아가 보도록 하겠습니다.


## Step 01
### `py-config`
우리는 `py-config` 태그를 활용해서 다른 `.py` 파일에서 필요한 함수를 불러올 수 있도록 경로를 설정해 줄 수 있습니다.

```html
<!-- index.html -->
<py-config>
    [[fetch]]
    files = ["./utils.py". "./func.py"]
</py-config>
```
`index.html`과 동일한 위치선상에 있는 `.py`파일의 경로는 위와 같이 작성할 수 있으며, 다른 경로에 있거나 <수정!! CDN 방식을 활용하여 정식 사이트의 샘플 코드, 혹은 GitHub의 raw도 이용 가능합니다.>
```html
<!-- index.html -->
<py-config>
    [[fetch]]
      from = "https://pyscript.net/examples/"
      files = ["utils.py"]
      [[fetch]]
      from = "https://gist.githubusercontent.com/FabioRosado/faba0b7f6ad4438b07c9ac567c73b864/raw/37603b76dc7ef7997bf36781ea0116150f727f44/"
      files = ["todo.py"]
</py-config>
```

또한, Python 고유의 Package를 추가하여 사용할 수도 있습니다.
```
<py-config>
    package = ["./utils.py". "./func.py"]
</py-config>
```

- 별도로 py-config 태그를 `.toml`파일로 관리할 수도 있습니다.

```toml
# .toml 확장자는 TOML(Tom's Obvious, Minimal Language) 형식의 설정 파일로, 사람이 읽고 쓰기 쉬운 최소한의 구성을 가진 명확한 언어입니다.
# 설정 파일, 프로젝트 설정, 데이터 저장 등 다양한 목적으로 사용되며, JSON, YAML 등과 유사한 역할을 합니다.

# This is a TOML document.

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # First class dates

# 위에 예시에서 `title`은 문자열, `[owner]`는 테이블 속성입니다.
```

## Step 02
### py-script
`Step 01`에서 `.py`파일의 경로를 지정 했다면, 이번 스탭에서는 `py-config`를 활용하여 `index.html`에서 사용할 수 있도록 `import`하는 법을 배워보겠습니다.
```html
 <py-script>
    from todo import add_task, dd_task_event
</py-script>
```
- from <.py 파일 이름> import <.py파일에서 사용하고 싶은 함수 이름>

또 다른 방법은, py-script에 src값으로 사용하는 방법입니다.

```html
<py-script src="./todo.py"></py-script>
```

