# 동치관계 확인하기!

**동치관계 확인 코드**는 관계 R이 집합(set)관곌 주어질 때, 이 관계 R이 동치 관계인지 판단하는 파이썬 모듈이다.

동치관계를 확인할 때는 3가지 조건을 만족해야한다. 반사관계(check_reflexive), 대칭관계(check_symmetric), 추이관계(check_transitive)를 모두 성립해야 동치관계가 성립이 된다.


## 설치
[https://github.com/Jong-IN-Choi/2sansuhak] 에서 py 파일을 다운 받은 뒤에, COLAB을 통해서 설치한다. 

터미널을 통해, py확장자의 파일을 실행시에는 

R = {(1, 1), (1, 3), (2, 2), (3, 3),(3, 1), (3, 4), (4, 4), (4, 3)} 

R = { (1,1), (1,4), (2,2), (2,3), (3,2), (3,3), (4, 1), (4,4)}

이 기본으로 설정되어있으므로 '동치가 아닙니다', '동치입니다' 라고 뜬다.
    
```python
! python3 equiv.py
```



## 게임 하는 법
1. R을 집합의 형태로 적는다. 
  ex) R = {(1, 1), (1, 3), (2, 2), (3, 3), (3, 1), (3, 4), (4, 4), (4, 3)}
2. check_equivalance(R)을 입력하여, 동치관게인지 확인한다.
3. 반사관계, 대칭관계, 추이관계를 확인하고 싶다면 각각 check_reflexive(R), check_symmetric(R), check_transitive(R)을 통해서 확인한다.
