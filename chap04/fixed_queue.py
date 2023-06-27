# 고정 길이 큐 클래스 FixedQueue 구현하기

from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int) -> None:
        """큐 초기화"""
        self.no = 0 
        self.front = 0 