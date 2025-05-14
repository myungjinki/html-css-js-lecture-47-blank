from itertools import combinations

"""
문제 설명
        주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
        숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중
        서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록
        solution 함수를 완성해주세요.

제한사항
        nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
        nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
"""


def solution(nums):
    def is_prime(n):
        # n이 2보다 작으면 소수가 아님
        if n < 2:
            return False
        # 2부터 √n까지 나누어 떨어지는지 확인
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        # 나누어 떨어지지 않으면 소수
        return True

    # nums에서 3개의 숫자를 뽑아 합이 소수인 경우의 수를 계산
    return sum(1 for comb in combinations(nums, 3) if is_prime(sum(comb)))
