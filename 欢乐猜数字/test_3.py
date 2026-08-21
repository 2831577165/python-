import random


class GuessWhat_3:
    def guess3(self):
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
        mankind = input('是否开始下一轮，回答Y/N:')
        print(mankind)
        if mankind == 'Y':
            return self.guess3()
        else:
            return '欢迎下次'




if __name__ == '__main__':
    game = GuessWhat_3()
    game.guess3()