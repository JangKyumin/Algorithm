def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        eaten = coupon//10 
        answer += eaten 
        coupon = coupon%10 + eaten 
    return answer 