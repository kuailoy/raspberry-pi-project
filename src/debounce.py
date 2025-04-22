# debounce.py
from time import time

class Debouncer:
    def __init__(self, delay, immediate=False):
        """
        delay: 防抖延迟时间(秒)
        immediate: 是否立即响应第一次触发
        """
        self.delay = delay
        self.last_call = 0
        self.last_value = None
        self.immediate = immediate
        self.pending = None

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            current_time = time()

            # 立即执行第一次调用
            if self.immediate and self.last_call == 0:
                self.last_call = current_time
                self.last_value = func(*args, **kwargs)
                return self.last_value

            # 取消前一个待执行调用
            if self.pending is not None:
                self.pending = None

            # 记录最新值并设置执行计划
            new_value = func(*args, **kwargs)
            elapsed = current_time - self.last_call

            if elapsed >= self.delay:
                self.last_call = current_time
                self.last_value = new_value
                return new_value
            else:
                # 设置延迟执行
                self.pending = new_value
                return self.last_value
        return wrapped

def debounce(delay, immediate=False):
    return Debouncer(delay, immediate)