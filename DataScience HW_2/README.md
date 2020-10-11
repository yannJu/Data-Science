###DataScience HW
===

**__HW2__**

* _(Logistic Regression)_ Linear와 다르게 이진 분류 문제를 해결하는데 효과적이다.

* 이진분류문제 

Training Data = [1.2, 3.8, -1.4, ..., 4.1] -> 0
	         [3.2, -1.2, -0.2, ..., 2.1] -> 1

와 같이 결과 (Y)가 0 또는 1로 나오는 분류 문제

---

* Linear와 다르게 Y의 값이 0 아니면 1로 나오기 때문에 Linear 에서 사용했던 Hypothesis 함수를 사용하게 되면 오차가 커짐 (값이 이산적이기 때문에)

* 따라서 H(x)를 Logistic 함수를 사용하여 표현. `H(x) = ∂(x) = 1 / 1 + e^(-x)`

---

* 또한 Cost함수 역시 MSG를 사용하면 동작이 잘 되지 않음 ~> 왜냐하면 0 또는 1 로 결과값이 나오기 때문에 평야 혹은 협곡이 생기게 됨

* 따라서 `C(h, y) = { -log(1 - h) if y = 0 , -log(h) if y = 1`

* MSG였던 (H(x) - 1)^2의 그래프와 -log(h)의 그래프를 비교하여 보았을때, 전자는 값이 일정한 값에서 변화없이 유지되어 오차가 커지게 됨