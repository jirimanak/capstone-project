import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = time.time()

    def elapsed_seconds(self):
        return time.time() - self.start_time

    def elapsed_time(self):
        seconds = self.elapsed_seconds()
        hours = seconds // (60 * 60)
        seconds %= (60 * 60)
        minutes = seconds // 60
        seconds %= 60
        return "%02i:%02i:%02i" % (hours, minutes, seconds)

    def print_elapsed_time(self):
        print ("\nElapsed time: {}\n".format(self.elapsed_time()))