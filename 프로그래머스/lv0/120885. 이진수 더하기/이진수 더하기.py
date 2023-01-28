def solution(bin1, bin2):
    return bin(int("0b{}".format(bin1), 2) + int("0b{}".format(bin2), 2))[2:]