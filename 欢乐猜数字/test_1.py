import random


class GuessWhat_1:
    def guess1(self):
        count = random.randint(1, 100)
        set = input("请输入数字:\n")
        print(type(set))
        num = int(set)
        while count != num:
            if count > num:
                print('猜小了，请重新输入:/n')
            elif count < num:
                print('猜大了请重新输入:/n')
            set = input()
            num = int(set)
        print('猜对了，数字是：',num)




if __name__ == '__main__':
    game = GuessWhat_1()
    game.guess1()
