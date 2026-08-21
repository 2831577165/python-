class ArrayRank:
    def array_rank(self):
        nums = [30,51,41,35,12,6,48,73]
        rank = {v: i for i,v in enumerate(sorted(set(nums)),1)}
        return [rank[v] for v in nums]

if __name__ == '__main__':
    print(ArrayRank().array_rank())