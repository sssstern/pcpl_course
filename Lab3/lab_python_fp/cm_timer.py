import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        exc_time = time.time() - self.start
        print(f"time: {exc_time}")

@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    exc_time = time.time() - start
    print(f"time: {exc_time}")


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
         time.sleep(5.5)