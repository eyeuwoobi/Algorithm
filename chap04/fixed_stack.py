# 고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""
    
    class Empty(Exception):
        """비어 있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외처리"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """스택 초기화"""
        self.capacity = capacity            #스택의 크기
        self.stk = [None] * self.capacity   #스택 본체
        self.pointer = 0                    #스택 포인터

    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return self.pointer

    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return self.pointer <= 0

    def is_full(self) -> bool:
        """스택이 가득 차 있는지 판단"""
        return self.pointer >= self.capacity

    def push(self, value: Any) -> None:
        """스택에 value를 푸시"""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.pointer] = value
        self.pointer += 1

    def pop(self) -> Any:
        """스택에서 데이터를 팝"""
        if self.is_empty():
            raise FixedStack.Empty
        self.pointer -= 1
        return self.stk[self.pointer]

    def peek(self) -> Any:
        """스택에서 데이터를 피크"""
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.pointer - 1]
    
    def clear(self) -> None:
        """스택을 비움"""
        self.pointer = 0
    
    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 인덱스를 반환"""
        for i in range(self.pointer - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value: Any) -> int:
        """스택에서 value의 개수를 반환"""
        idx = 0
        for i in range(self.pointer - 1, -1, -1):
            if self.stk[i] == value:
                idx += 1
        return idx
    
    def __contains__(self, value: Any) -> bool:
        """스택에 value가 있는지 판단"""
        return self.count(value) > 0
    
    def dump(self) -> None:
        """덤프"""
        if self.is_empty():
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.pointer])