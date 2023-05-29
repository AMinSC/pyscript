# pyscript
Learning pyscript and writing books

## study
- CDN 방식
    - ```html
        <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>
        ```
- Python 모듈, 패키지 사용시
    - ```html
        <py-config>
        [[fetch]]
        files = ["./utils.py", "./todo.py"]
        </py-config>
        ```
- HTML 태그에 Python 함수 사용시
    - ```html
        <py-script src="./todo.py"></py-script>
        <!-- todo.py 안에 add_task() 함수가 있을 때 -->
        ```
    - ```html
        <button
            id="new-task-btn"
            class="py-button"
            type="submit"
            py-click="add_task()"  
        >
        <!-- py-click.. 그 외 PyScript 가능한 argument 찾아보기 -->
        ```