import pytest
from stuff.accum import Accumulator

# --------------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------------
@pytest.fixture
def accum():
  yield Accumulator()
  print("DONE Testing Accumulator!")
