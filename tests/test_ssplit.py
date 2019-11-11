import glob
import json
import typing

import os
import pytest

from textformatting import ssplit


def read_test_file(path):
    """Read a test file.

    Parameters
    ----------
    path : str
        The path to a test file.

    Returns
    -------
    typing.Tuple[str, typing.List[str]]
    """
    with open(path) as f:
        dct = json.load(f)
        return dct['text'], dct['sentences']


test_file_path_pattern = os.path.join(os.path.dirname(__file__), 'test_ssplit', '*.json')
test_cases = [read_test_file(path) for path in sorted(glob.glob(test_file_path_pattern))]


@pytest.mark.parametrize('test_case', test_cases)
def test_ssplit(test_case):
    text, sentences = test_case
    assert ssplit(text) == sentences
