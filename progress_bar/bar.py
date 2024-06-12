import time

class ProgressBar:
    def __init__(self, total, prefix='', suffix='', length=50, fill='█', print_end="\r"):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.iteration = 0

    def print_progress(self, iteration):
        self.iteration = iteration
        percent = ("{0:.1f}").format(100 * (self.iteration / float(self.total)))
        filled_length = int(self.length * self.iteration // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end=self.print_end)
        if self.iteration == self.total: 
            print()

    def iterate(self):
        for i in range(self.total):
            time.sleep(0.1)
            self.print_progress(i + 1)