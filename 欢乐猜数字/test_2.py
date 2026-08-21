import random


class GuessWhat_2:
    def guess2(self):
        count = random.randint(1, 100)
        coud = 5000
        set = input("请输入数字:\n")
        print(type(set))
        num = int(set)
        while count != num and coud != 0:
            if count > num:
                coud -= 500
                print('猜小了剩余金币是：\n',coud)
            elif count < num:
                coud -= 500
                print('猜大了剩余金币是：\n',coud)
            set = input()
            num = int(set)
        print('猜对了，数字是：',num)




if __name__ == '__main__':
    game = GuessWhat_2()
    game.guess2()