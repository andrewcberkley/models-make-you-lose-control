# Makes the lab folder importable for the tests (harness, solutions and labkit).
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
