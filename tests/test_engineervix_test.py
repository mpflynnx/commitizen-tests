#!/usr/bin/env python3

"""Tests for `engineervix_test`"""

import pytest

from engineervix_test import engineervix_test


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/engineervix/cookiecutter-pyproject')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
def test_command_line_interface(capsys):
    """Test the CLI."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli()
    captured = capsys.readouterr()
    result = captured.out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 42
    assert 'engineervix_test.cli.main' in result

    with pytest.raises(SystemExit) as pytest_wrapped_f:
        cli(["-h"])
    captured_02 = capsys.readouterr()
    help_result = captured_02.out
    assert pytest_wrapped_f.type == SystemExit
    assert pytest_wrapped_f.value.code == 42
    assert '-h, --help            show this help message and exit' in help_result


class TestEngineervix_test():
    """Tests the engineervix_test module"""

    @staticmethod
    def test_addition():
        """tests for addition"""
        assert engineervix_test.add(2, 2) == 4  # nosec

    @staticmethod
    def test_subtraction():
        """tests for subtraction"""
        assert engineervix_test.subtract(4, 2) == 2  # nosec
