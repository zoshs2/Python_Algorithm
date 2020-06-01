#!/usr/bin/python

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E
    
def insert_node(data): # 매개변수 data값을 가지는 새로운 노드를 추가하는 함수
    global node_A
    new_node = Node(data) # 새로운 노드(객체)가 선언된다.
    node_P = node_A # head노드 부분인 node_A객체의 주소값을 node_P에 담는다.
    node_T = node_A # head노드 부분인 node_A객체의 주소값을 node_T에 담는다. 왜 이런짓을?
    while node_T.data <= data: # 새로 추가할 노드의 값이 머리부분의 값보다 크거나 같다면, 반복문 시행(즉, 여기선 사전적알파벳 순으로 나중에 나오는 것이라면)
        node_P = node_T # ?? 왜 똑같은 걸 대입하고 난리지
        node_T = node_T.next # 맨처음 반복때, node_T에는 head노드 부분의 다음 노드의 주소값이 담긴다.
                             # 이런 식으로 계속 다음으로 넘어간 노드가 새로 추가하는 data값보다 작거나 같을 때까지 계속 반복한다. 커지는 순간 반복문은 종료
    
    new_node.next = node_T # 새로 추가하는 노드의 next멤버변수에는 이제 본인보다 큰 값을 가지는 노드를 가리키게 된다.
    node_P.next = new_node # 바로 그 직전의 노드의 next멤버변수에는 새로 추가하는 노드를 가리키게 한다.
    # 그러니까 순서가 새로 추가하는 노드의 next를 먼저 지정해주고,
    # 그리고나서 그 직전 노드의 next는 새로 추가하는 노드를 가리키도록 한다.
    # 이 때 링크를 걸어주는 순서가 중요하다! 

def delete_note(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next
    if pre_node.data == del_data:
        node_A = next_node
        del pre_node
        return
    
    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next
        
    
def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()
    
if __name__ == "__main__":
    print("연결리스트 초기화 후")
    init_list()
    print_list()
    print("노드 C를 추가한 후")
    insert_node("C")
    print_list()
    
    
