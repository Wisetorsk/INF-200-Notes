
import nose.tools as nt

import palindrome as p

def test_empty():
    assert p.is_palindrome(''), 'Empty string false negative'
    
def test_lowercase_palindromes():
    nt.assert_true(p.is_palindrome('ana'), 'ana false negative')
    nt.assert_true(p.is_palindrome('anna'), 'anna false negative')

def test_lowercase_non_palindromes():
    nt.assert_false(p.is_palindrome('per'), 'per false positive')
    nt.assert_false(p.is_palindrome('kari'), 'kari false positive')
        
def test_uppercase_palindromes():
    nt.assert_true(p.is_palindrome('ANA'), 'ANA false negative')
    nt.assert_true(p.is_palindrome('ANNA'), 'ANNA false negative')

def test_uppercase_non_palindromes():
    nt.assert_false(p.is_palindrome('PER'), 'PER false positive')
    nt.assert_false(p.is_palindrome('KARI'), 'KARI false positive')