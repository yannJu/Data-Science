###DataScience HW
===

**__HW1__**

* 1. [약 10000줄정도의 문장에서 가장 빈도수가 높은 단어 1000개와 그 갯수를 stdout으로 출력](https://github.com/yannJu/Python/blob/master/%EB%8D%B0%EC%9D%B4%ED%84%B0%EA%B3%BC%ED%95%99/h01_%EC%9D%B4%EC%97%B0%EC%A3%BC_20191644_wc.py)
* 2. [1)에서 출력한 stdout을 stdin으로 받아, 지프의 법칙이 성립하는지 확인, c와 s를 구함](https://github.com/yannJu/Python/blob/master/%EB%8D%B0%EC%9D%B4%ED%84%B0%EA%B3%BC%ED%95%99/h01_%EC%9D%B4%EC%97%B0%EC%A3%BC_20191644_plot.py)

_지프의 법칙은 n(단어의 출현횟수) = ck(단어의 출현순위)^-s_
* 3. [2)에서 받은 stdin을 이용하여 pyplot으로 그래프를 그리고 저장](https://github.com/yannJu/Python/blob/master/%EB%8D%B0%EC%9D%B4%ED%84%B0%EA%B3%BC%ED%95%99/h01_%EC%9D%B4%EC%97%B0%EC%A3%BC_20191644_plot.png)

---

* redirection 사용으로 stdin과 stdout에 대한 정리
* `import re`를 통하여 re.split사용 
	_ re.split외에도 re.sub, re.compile, re.findall사용 _
* `Counter`을 통하여 빠르고 쉽게 횟수 체크
