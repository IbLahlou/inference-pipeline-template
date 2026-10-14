import time
import threading


class Histogram:
    def __init__(self, name, buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0)):
        self.name = name
        self.buckets = sorted(buckets)
        self._lock = threading.Lock()
        self._counts = {b: 0 for b in self.buckets}
        self._counts[float("inf")] = 0
        self._sum = 0.0
        self._count = 0

    def observe(self, value):
        with self._lock:
            self._sum += value
            self._count += 1
            for b in self.buckets:
                if value <= b:
                    self._counts[b] += 1
            self._counts[float("inf")] += 1

    def collect(self):
        lines = []
        cumulative = 0
        with self._lock:
            for b in self.buckets:
                cumulative += self._counts[b]
                lines.append(f'{self.name}_bucket{{le="{b}"}} {cumulative}')
            lines.append(f'{self.name}_bucket{{le="+Inf"}} {self._count}')
            lines.append(f"{self.name}_sum {self._sum}")
            lines.append(f"{self.name}_count {self._count}")
        return "\n".join(lines)


class Counter:
    def __init__(self, name):
        self.name = name
        self._value = 0
        self._lock = threading.Lock()

    def inc(self, amount=1):
        with self._lock:
            self._value += amount

    def collect(self):
        with self._lock:
            return f"{self.name} {self._value}"


REQUEST_LATENCY = Histogram("request_latency_seconds")
PREDICTION_COUNT = Counter("prediction_count_total")
ERROR_COUNT = Counter("error_count_total")


def collect_metrics():
    parts = [
        "# HELP request_latency_seconds Histogram of request latency.",
        "# TYPE request_latency_seconds histogram",
        REQUEST_LATENCY.collect(),
        "# HELP prediction_count_total Total predictions served.",
        "# TYPE prediction_count_total counter",
        PREDICTION_COUNT.collect(),
        "# HELP error_count_total Total prediction errors.",
        "# TYPE error_count_total counter",
        ERROR_COUNT.collect(),
    ]
    return "\n".join(parts) + "\n"


class Timer:
    def __init__(self, histogram):
        self._histogram = histogram

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self._histogram.observe(time.perf_counter() - self._start)
