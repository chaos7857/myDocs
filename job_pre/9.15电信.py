import sys

def solu1():
    T = int(sys.stdin.readline())
    for t in range(T):
        # 零食种类数 与 价格倍率
        n, m = [int(x) for x in sys.stdin.readline().strip().split()]
        # 这玩意是一个m为首相，m为公比的等比数列
        # [m^1, m^2, m^3 ... m^n]
        # 题目可以转化为将这个等比数列分成俩个最为接近的数，
        # 其中小的那个数取了什么索引


############################################################################
if __name__ == "__main__":
    solu1()