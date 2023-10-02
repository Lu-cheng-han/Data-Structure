
class Solution:

    def findRelativeRanks(self, source: list):
        sorted_source = sorted(source,reverse=True)
        rank_dictionary = {}
        ans = []
        for i in range(len(sorted_source)):
            if i == 0:
                rank_dictionary[sorted_source[i]] = "Gold Medal" 
            elif i == 1:
                rank_dictionary[sorted_source[i]] = "Silver Medal"
            elif i == 2:
                rank_dictionary[sorted_source[i]] = "Bronze Medal"
            else:
                rank_dictionary[sorted_source[i]] = str(i+1)
        for i in source:
            ans.append(rank_dictionary.get(i))
        return ans


if __name__ == "__main__":
    source = [11, 15, 16, 17, 55,1,3]
    ans = Solution().findRelativeRanks(source)
    print(ans)