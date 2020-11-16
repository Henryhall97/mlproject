# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import dist
import pytest


def test_dist():

    assert dist(48.865070, 2.380009, 48.235070, 2.393409) == 70.00789153218594
