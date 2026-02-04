from __future__ import annotations
import pathlib

def project_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]
