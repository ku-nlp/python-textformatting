import typing

import re

PATTERNS = {
    'period': '。．？！♪…?!'
}


def ssplit(text, model='regex'):
    """Split text into sentences.

    Parameters
    ----------
    text : str
        A input text to be split.
    model : str
        A model name (default: regex).

    Returns
    -------
    typing.List[str]
    """
    if model == 'regex':
        return _ssplit_regex(text)
    else:
        raise NotImplementedError


def _ssplit_regex(text):
    """Split text into sentences by regular expressions.

    Parameters
    ----------
    text : str
        A input text to be split.

    Returns
    -------
    typing.List[str]
    """
    _base = r'[^%(period)s]*[%(period)s]' % PATTERNS
    _eol = r'[^%(period)s]*$' % PATTERNS
    _regex = re.compile(r'%(_base)s|%(_eol)s$' % locals())
    _sentence_candidates = []
    for line in text.split('\n'):
        _sentence_candidates += re.findall(_regex, line + '\n')
    _sentence_candidates = _merge_sentence_candidates(_sentence_candidates)
    return _clean_up_sentence_candidates(_sentence_candidates)


def _merge_sentence_candidates(sentence_candidates):
    """Merge sentence candidates.

    Parameters
    ----------
    sentence_candidates : typing.List[str]
        A list of sentence candidates.

    Returns
    -------
    typing.List[str]
    """
    sentence_candidates = _merge_single_periods(sentence_candidates)
    sentence_candidates = _merge_parenthesis(sentence_candidates)
    return sentence_candidates


def _merge_single_periods(sentence_candidates):
    """Merge sentence candidates that consist of a single period.

    Parameters
    ----------
    sentence_candidates : typing.List[str]
        A list of sentence candidates.

    Returns
    -------
    typing.List[str]
    """
    _regex = re.compile(r'^[%(period)s]$' % PATTERNS)

    merged_sentences = ['']
    for sentence_candidate in sentence_candidates:
        if re.match(_regex, sentence_candidate):
            merged_sentences[-1] += sentence_candidate
        else:
            merged_sentences.append(sentence_candidate)

    if merged_sentences[0] == '':
        merged_sentences.pop(0)  # remove the dummy sentence
    return merged_sentences


def _merge_parenthesis(sentence_candidates):
    """Merge sentence candidates so that they save strings in parentheses or brackets.

    Parameters
    ----------
    sentence_candidates : typing.List[str]
        A list of sentence candidates.

    Returns
    -------
    typing.List[str]
    """
    parenthesis_level = 0
    quotation_level = 0

    merged_sentences = []
    _sentence_candidate = ''
    while sentence_candidates:
        sentence_candidate = sentence_candidates.pop(0)

        parenthesis_level += sentence_candidate.count('（') + sentence_candidate.count('(')
        parenthesis_level -= sentence_candidate.count('）') + sentence_candidate.count(')')

        quotation_level += sentence_candidate.count('「') + sentence_candidate.count('“')
        quotation_level -= sentence_candidate.count('」') + sentence_candidate.count('”')

        if parenthesis_level == 0 and quotation_level == 0:
            sentence_candidate = _sentence_candidate + sentence_candidate
            merged_sentences.append(sentence_candidate)
            _sentence_candidate = ''
        else:
            if '\n' in sentence_candidate:
                sentence_candidate, rest = sentence_candidate.split('\n', maxsplit=1)
                sentence_candidate = _sentence_candidate + sentence_candidate
                merged_sentences.append(sentence_candidate)
                _sentence_candidate = ''
                sentence_candidates.insert(0, rest)
                parenthesis_level = 0
                quotation_level = 0
            else:
                _sentence_candidate += sentence_candidate

    if _sentence_candidate:
        merged_sentences.append(_sentence_candidate)
    return merged_sentences


def _clean_up_sentence_candidates(sentence_candidates):
    """Remove empty sentence candidates.

    Parameters
    ----------
    sentence_candidates : typing.List[str]
        A list of sentence candidates.

    Returns
    -------
    typing.List[str]
    """
    return [sentence_candidate.strip() for sentence_candidate in sentence_candidates if sentence_candidate.strip()]
