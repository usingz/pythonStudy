from typing import Optional
# coding = utf-8

'''
typing模块的作用:
1 类型检查，防止运行时出现参数和返回值类型不符合
2 作为开发文档附加说明，方便使用者调用时传入和返回参数类型
3 该模块加入后并不会影响程序的运行，不会报正式的错误，只有提醒
'''

#  1) Insertion, deletion, and random access of array
#  2) Assumes int for element type


class MyArray:
    def __init__(self, cacpcity: int):
        self._data = []
        self._count = 0
        self._cacpcity = cacpcity

    def __getitem__(self, position: int) -> int:
        return self._data[position]
    # 对于给定的键返回指定的值

    def find(self, index: int) -> Optional[int]:
        if index >= self._count or index <= -self._count: return None
        return self._data[index]

    def delete(self, index: int) -> bool:
        if index >= self._count or index <= -self._count: return False
        self._data[index: -1] = self[index+1:]
        self._count -= 1
    # -1表示从后往前第二个

    def insert(self, index: int, value: int) -> bool:
        if index >= self._count or index <= -self._count: return False
        if self._cacpcity == self._count: return False
        self._data.insert(index, value)
        self._count += 1
        return True

    def insert_to_tail(self, value: int) -> bool:
        if self._count == self._cacpcity: return False
        self._data.append(value)
        self._count += 1
        return True

    def __repr__(self):
        return " ".join(str(num) for num in self._data[:self._count])
    # 返回一个字符串对象， 表示每个数字的长度打印出来

    def print_all(self):
        for num in self._data[:self._count]:
            print(f"{num}", end=" ")
            # end表示在结尾加上指定字符串
        print("\n", flush=True)
        # flush表示是否立刻显示


if __name__ == "__main__":
    a = MyArray(6)
    for i in range(6):
        a.insert_to_tail(i)

    a.delete(2)
    a.print_all()
    a.__repr__()
    print(a)