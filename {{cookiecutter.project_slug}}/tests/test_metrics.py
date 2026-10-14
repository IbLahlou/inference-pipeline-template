import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from metrics import Counter, Histogram, Timer, collect_metrics


def test_counter_increment():
    c = Counter("test_counter")
    c.inc()
    c.inc(5)
    assert "test_counter 6" in c.collect()


def test_histogram_observe():
    h = Histogram("test_hist", buckets=(0.1, 0.5, 1.0))
    h.observe(0.05)
    h.observe(0.3)
    h.observe(0.8)
    output = h.collect()
    assert "test_hist_count 3" in output
    assert "test_hist_sum" in output


def test_timer():
    h = Histogram("timer_test")
    with Timer(h):
        pass
    assert h._count == 1


def test_collect_metrics_format():
    output = collect_metrics()
    assert "# HELP" in output
    assert "# TYPE" in output
    assert "request_latency_seconds" in output
    assert "prediction_count_total" in output
    assert "error_count_total" in output
