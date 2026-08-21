class YHSJ1:
    def yhsj_1(self):
        res = []
        num = 5
        for i in range(num):
            row = []
            for j in range(0,i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i-1][j] + res[i-1][j-1])
            res.append(row)
        return res

if __name__ == '__main__':
    print(YHSJ1().yhsj_1())