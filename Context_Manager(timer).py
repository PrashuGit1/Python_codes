import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start:.2f} seconds")

with Timer():
    time.sleep(1.5)
