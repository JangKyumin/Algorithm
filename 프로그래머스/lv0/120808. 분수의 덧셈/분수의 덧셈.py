from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    ans = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [ans.numerator, ans.denominator]