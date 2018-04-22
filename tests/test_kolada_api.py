#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `kolada_api` package."""

import pytest

from kolada import Kpi, Municipality, Ou


def test_aslist():
    assert isinstance(Kpi().kpi().list_of_list, list)

    #rewrite for pytest
