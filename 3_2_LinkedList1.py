#!/usr/bin/python

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def init_list():
    global node_A # 왜 이런짓을? 
    # 원래 main에 포함된 global_variable 전역변수는 함수에서 접근이 가능하지만,
    # 함수 내에서 전역변수를 수정할 수는 없다! 
    # 즉, 여기 이 init_list()함수안에서 global_variable = 1 과 같이 수정을 가하는 행위는 
    # 금지된다. 
    # 하지만, 이 함수 내에서 global 키워드를 이용해서(예: global global_variable) 전역변수임을 명시적으로 선언해주면,
    # 함수 내에서 전역변수를 수정을 할 수 있다. (다만 권장하지 않는 방법이다. 함수의 매개변수와 return문을 활용해서 충분히 전역변수를 수정하여 구현할 수 있다.)
    
    node_A = Node("A") # noda_A객체의 data멤버변수에 "A"가 저장된다.
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")
    node_A.next = node_B # node_B 객체의 주소값이 node_A객체의 next멤버변수에 저장된다.
    node_B.next = node_C # 이번엔 node_C 객체의 주소값이 node_B객체의 next멤버변수에 저장된다.
    node_C.next = node_D 
    
def print_list():
    global node_A # 뭐하는 짓거리야
    node = node_A # head 부분인 node_A 객체의 주소값을 node라는 변수에 담는다. 
    while node:
        print(node.data) # node가 가리키는 주소의 객체가 가진 data멤버변수를 출력한다.
        node = node.next # 그리고 그 node의 next변수가 향하는 링크 (다음노드)의 노드주소를 node에 덮어 씌운다. 
                         # node.next가 None이 나올 때까지 계속 반복된다.
    print() # 띄어쓰기 (개행)
    
if __name__ == "__main__":
    global_variable = 0
    init_list()
    print_list()