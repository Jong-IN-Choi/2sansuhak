# -*- coding: utf-8 -*-
"""코드과제4_equiv_relation_check_student_임선민, 여재영, 최종인

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FM2kvK5lGQlQZHib9gaX-vLYhcckgaw0

# 관계 R 이 set 으로 주어질 때, 이 관계 R 이 동치 관계인지를 판단하는 파이썬 모듈을 만들라. 이 모듈에는 check_transitive(R), check_symmetric(R), check_reflexive(R) 을 포함하며, 이 함수들은 True, False 를 반환한다. 이 결과를 종합하여, 동치관계인지 판단하는 check_equivalance(R) 도 들어있는데, 이 함수에서 위의 세 함수 (즉, check_transitive(R), check_symmetric(R), check_reflexive(R)) 을 호출하여 해당 결과들을 종합하여 동치 관계 여부를 판단하고, True 혹은 False 를 최종적으로 반환해준다. 이 모듈이 팀원들의 깃페이지에 read.md 와 함께 기록되어 다운 받으면 설치 후 각 함수를 실행될 수 있도록 한다. 

## 결과는 모든 집합 형태의 관계에 대해 작동해야하지만, 특히 아래의 예로 주어지는 집합에 대해 작동하도록 한다. 

```
A = {1,2,3,4} # 관계가 정의된 집합 
R = {(1, 1), (1, 3), (2, 2), (3, 3),(3, 1), (3, 4), (4, 4), (4, 3)} # 정의된 관계 
```
"""

# 반사
def check_reflexive(R) :
    for element in R:
        x, y = element
        if x == y :
            return True
        else : 
            return False
# 대칭
def check_symmetric(R) :# xRy == yRx
    for element in R: # R에 대한 모든 요소를 추출해서
        x, y = element #x 과 y에 할당해준다
        element1 = (y, x) # y 과 x에 할당해준다
        if element1 not in R: # R에 (y,x)가 없다면
            return False # 대칭조건에 성립하지 않으므로, False를 반환해준다. 
    return True # 대칭조건에 성립하므로, True를 반환해준다. 
# 추이
def check_transitive(R): # xRy and yRz —> xRz
    for element in R: # R에 대한 모든 요소를 추출해서
        x_1,y_1 = element # x_1 과 y_1에 할당해준다
        for element_2 in R: # 이번에도 R에 대한 모든 요소를 추출해서
            y_2,z_1 = element_2 # y_2 와 z_1에 할당해준다
            if y_1 == y_2 and (x_1,z_1) not in R: # y_1과 y_2가 같은데 (x_1,z_1)이 R에 속해 있지 않다면 xRy가 있고 yRz가 있으면 xRz가 존재하는 추이적 조건을 성립 하지 못하므로 False를 리턴해주고
                return False
    return True # 조건문에 걸리지 않으면 추이적 조건을 성립하는 것 이므로 True를 반환해준다

# (1)  여기에 전체 코드 
def check_equivalance(CJI) :
    if check_transitive(CJI) and check_symmetric(CJI)and check_reflexive(CJI): # 동치조건의 세가지 (반사조건, 대칭조건, 추이조건)을 모두 만족한다면,
        print('동치입니다.') #True를 반환한다.
    else :
        print('동치가 아닙니다.')  #False를 반환한다.

#진짜 문제
R = {(1, 1), (1, 3), (2, 2), (3, 3),(3, 1), (3, 4), (4, 4), (4, 3)} # 정의된 관계 
check_equivalance(R)

#동치인 문제
R = { (1,1), (1,4), (2,2), (2,3), (3,2), (3,3), (4, 1), (4,4)}
check_equivalance(R)

# (2) 모듈이 설명과 함께 올라온 깃허브 링크 추가: