from dataclasses import dataclass


@dataclass(frozen=True)
class Commands:
    info = "info"
    pnl = "pnl"
    open_pos = "open_pos"
