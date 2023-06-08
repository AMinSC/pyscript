# Using Async/Await and Asyncio `Deprecated` Implicit Coroutine Scheduling / Top-Level Await
## Async/Await 및 Asyncio 사용 
`더 이상 사용되지 않음` 암시적 코루틴 스케줄링/최상위 대기

## 2022.09.01 기준 버전 업데이트
PyScript 2022.09.01 이전 버전에서는 <py-sciprt> 태그는 암시적으로 *코루틴 스케줄링이 가능했습니다.

```
*코루틴(coroutine)은 서로 협력하는 루틴(cooperative routine)을 의미합니다.

여기서는 코루틴을 자세히 다루기 보다는 간략하게 말씀드리겠습니다.

예를 들어 일반 계산기와 특수한 계산기를 함수화 시킨다고 가정하고 설명하겠습니다.

일반 계산기 기능을 하는 일반 함수의 경우, `calculator`함수 안에 내부 함수인 `add`함수를 사용한다면, 더하기 기능을 사용할 때, `calculator`함수인 메인 루틴은 대기 상태가 되고, `add`함수인 서브 루틴이 계산을 완료한 뒤 함수가 종료되고(함수가 종료되기 때문에 안에 내용은 모두 사라집니다.) 다시 메인 루틴인 `calculator`함수가 기능을 완료하고 종료할 것입니다.

하지만, 코루틴을 사용한 특수한 계산기의 경우, `special_cal`함수 안에 yeild로 값을 ..... 더 간략하게 설명하는 방향으로 수정...
```