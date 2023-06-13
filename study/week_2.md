# Using Async/Await and Asyncio `Deprecated` Implicit Coroutine Scheduling / Top-Level Await
## Async/Await 및 Asyncio 사용 
`더 이상 사용되지 않음` 암시적 코루틴 스케줄링/최상위 대기

### 2022.09.01 기준 버전 업데이트
PyScript 2022.09.01 이전 버전에서는 `<py-sciprt>` 태그는 암시적으로 *코루틴 스케줄링이 가능했습니다.
```py
<py-script>
import asyncio

for i in range(3):
    print(i)
    await asyncio.sleep(1)
</py-script>
```

하지만, 이후 버전에서는 비동기 처리 함수를 하기 위해서는 `async` 를 작성해줘야 합니다.
```py
<py-script>
import asyncio

async def main():
    for i in range(3):
        print(i)
        await asyncio.sleep(1)

asyncio.ensure_future(main())
</py-script>
```

- *코루틴(coroutine)은 서로 협력하는 루틴(cooperative routine)을 의미합니다.
여기서는 코루틴을 자세히 다루지 않고, 간략하게 말씀드리겠습니다.
코루틴은 두 가지 유형의 코루틴이 있습니다.
첫 번째로는 `yield` 키워드를 사용하여 일시 중지하고 다시 시작하는 데 사용할 수 있으며, 두 번째로는 비동기 I/O를 위한 `asyncio` 라이브러리의 일부로 `async`와 `await` 키워드를 활용하여 비동기처리를 할 수 있습니다.

- `yield`키워드를 활용한 샘플 코드
    ```py
    def producer(coroutine):
        print('Starting producer')
        for i in range(1, 5):
            print(f'Producing data {i}')
            coroutine.send(i)
        print('Producer done')
        coroutine.close()

    def consumer():
        print('Starting consumer')
        while True:
            i = (yield)  # Receive a 'i' value from the producer
            print(f'Consuming data {i}')

    c = consumer()
    next(c)  # Start consumer coroutine
    producer(c)

    ```

- asyncio 라이브러리를 활용한 예시 코드
    ```py
    import asyncio

    async def task(name, time):
        print(f'Task {name} will run for {time} seconds.')
        await asyncio.sleep(time)
        print(f'Task {name} is complete.')

    async def main():
        # Create the tasks
        tasks = [task('A', 2), task('B', 1), task('C', 3)]

        # Run the tasks
        await asyncio.gather(*tasks)

    # Run the main function
    asyncio.run(main())

    ```

---
# display(*values, target=None, append=True)

## Parameters
- `*values` - 표시할 개체를 받습니다. 문자열 객체는 있는 그대로를 출력하고, 문자열이 아닌 다양한 타입인 객체의 경우, eval()과 동일한 기능을 하려고 하지만, 그렇지 못한 경우 객체의 이름과 주소 등 추가 정보와 함께 객체 타입의 이름을 포함하는 리스트 형식으로 대괄호로 묶인 문자열을 표현합니다.

|Method|Inferred MIME type|
|:------|:-------:|
|`__repr__`|text/plain|
|`_repr_html_`|text/html|
|`_repr_svg_`|image/svg+xml|
|`_repr_png_`|image/png*|
|`_repr_pdf_`|application/pdf|
|`_repr_jpeg_`|image/jpeg*|
|`_repr_json_`|application/json|
|`_repr_javascript_`|application/javascript*|
|`savefig`|application/javascript*|


- `target` - 엘리먼트의 ID입니다. 대상의 기본값은 현재 py-script 태그 ID이며, 이 매개변수에 다른 ID를 지정할 수 있습니다.

```py
<py-script>
    def display_hello():
        # this fails because we don't have any implicit target
        # from event handlers
        display('hello', target="helloDiv")
</py-script>
<div id="helloDiv"></div>
<button id="my-button" py-onClick="display_hello()">Click me</button>
```


- `append` - True이면 `<div>` 태그를 생성하고 False이면 임의의 ID를 가진 `<py-script>` 태그를 생성합니다. 
    - 현재 `<py-script>`태그 내부에서 `display`함수를 다수 사용한 뒤, `append`의 인수값을 `False`로 2개 이상 줄 경우, 1개만 노출 됩니다.
