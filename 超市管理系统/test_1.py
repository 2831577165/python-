# class shopping_1:
#     def shop1(self):
#         money = 5000
#         shangs = [('candy',1500),('sunny',2000),('airpot',10000)]
#         che = []
#         while money > 0 :
#             wanna = input('请输入购买商品名称(按q退出）：')
#             print(wanna)
#             if wanna == 'q':
#                 break
#             f1 = False
#             for shang,qian in shangs:
#                 if wanna == shang:
#                     if money > qian:
#                         che.append(shang)
#                         money = money - qian
#                         shangs.remove((shang,qian))
#                         f1 = True
#                     else:
#                         print('穷鬼，钱不够！请到其他超市购买！')
#                         return che
#             if not f1:
#                 print('没有这个商品，别瞎弄！')
#                 return che
#         return che
#
# if __name__ == '__main__':
#     shopping_1().shop1()


class shopping_1:
    def shop1(self):
        money,pay,counts = 5000,0,0
        shangs = [('candy',1500),('sunny',2000),('airpot',10000)]
        che = []
        while money > 0 :
            wanna = input('请输入购买商品名称(按q退出)：')
            if wanna == 'q':
                break
            f1 = False
            for shang,qian in shangs:
                if wanna == shang:
                    if money > qian:
                        che.append(shang)
                        money = money - qian
                        pay += qian
                        shangs.remove((shang,qian))
                        counts += 1
                        f1 = True
                    else:
                        print('穷鬼，钱不够!请到其他超市购买！')
                        f1 = True
                    break
            if not f1:
                print('没有这个商品，别瞎弄！')

        print('购物清单：',che,'\n剩余金额:',money,'\n总共花费:',pay,'\n购买数量:',counts)
        return che,money,pay,counts

if __name__ == '__main__':
     shopping_1().shop1()
