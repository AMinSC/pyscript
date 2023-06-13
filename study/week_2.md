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


---
# display(*values, target=None, append=True)

