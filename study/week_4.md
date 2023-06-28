# 3.4 시각화 (데이터 분석) + py-repl로 데이터 처리가능
이번 장에서는 `<py-config>`태그로 Python Package를 구성하여 간단하게 시각화를 해보겠습니다.

## 3.4.1 matplotlib
Python에서 시각화 패키지는 크게 matplotlib과 seaborn이 있습니다.
..
matplotlib, seaborn 으로 시각화, 심화로 pandas로 data까지 진행..

- 공식홈페이지 example
- pandas를 제외한 간단한 matplotlib으로 시각화
- 가능하면 seaborn 혹은 pandas

우선 plugin 관련 "AttributeError: 'NoneType' object has no attribute 'appendChild'" 에러 알아보기
plugin을 사용하지 않을 경우, ~~"plt.show()"가 None으로 나옴.. 위 에러와 비슷한 상황으로 판단됨~~ 해결 plt.show() -> display(plt)

## 3.4.2 pandas



<!-- package가 부담스러울 경우 테스트 용 -->
우선 공식 홈페이지에서 CDN(Content Delivery Network)방식을 활용해보겠습니다.
## 3.4.3 sklearn (보류) or 데이터를 읽어와서 사용