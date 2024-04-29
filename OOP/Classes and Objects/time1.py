class Time:
    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def to_seconds(self):
        seconds = self.hh * 60 * 60 + self.mm * 60 + self.ss
        return seconds

    def is_after(self, other):
        return self.to_seconds() > other.to_seconds()

    def is_valid(self):
        if self.hh < 0 or self.mm < 0 or self.ss < 0:
            return False

        if self.hh > 23 or self.mm >= 60 or self.ss >= 60:
            return False

        return True

    def increment(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24

        self.ss += seconds
        self.mm += minutes
        self.hh += hours

    def __add__(self, other):
        if not self.is_valid() or not other.is_valid():
            raise ValueError("Invalid time was entered")

        seconds = self.to_seconds() + other.to_seconds()

        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24

        t = Time(hours, minutes, seconds)
        return t

    def __str__(self):
        return f"{self.hh:02}:{self.mm:02}:{self.ss:02}"


def main():
    t = Time(1, 2)
    print(t)
    print()

    t.increment(100)
    print(t)
    print()

    start = Time(9, 45)
    end = Time(10, 7, 17)
    print(t.is_valid())
    print(end.is_after(start))
    print()

    b = start + end
    print(b)


main()
