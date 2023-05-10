from dataclasses import dataclass


@dataclass
class Stages:
    start = "start"
    search = "search"
    pos_open = "pos_open"
    pos_protected = "pos_protected"
    stats = "stats"
    stopped = "stopped"
    cold_down = "cold_down"
    cold_down_stats = "cold_down_stats"
