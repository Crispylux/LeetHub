#배열 nums에서 두 수를 더하면 target이 나온다.
#몇 번째, 몇 번째 요소인지 리턴하라
#시간복잡도 : O(n)

class Solution(object):
    def twoSum(self, nums, target):  #(배열, 결과)

        dic = {}

        for i, num in enumerate(nums):          #i=인덱스, num=그 위치의 값
            want = target - num                 #지금 값(num)와 더해서 target이 되려면 필요한 값

            if want in dic:                     #해시 테이블이므로 O(1)로 바로 찾을 수 있어 성능적으로 좋은 선택!
                return [dic[want], i]

            dic[num] = i    #해시에 저장(num:i 형식으로)