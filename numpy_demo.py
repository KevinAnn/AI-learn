import numpy as np

# 使用np.array()创建矩阵
na = np.array([[1, 2, 3], [4, 5, 6]])
print("========== array() ==========")
print(na)
print(
    """
    对象类型：{}\n
    矩阵形状：{}\n
    维度（秩）：{}\n
    元素个数：{}\n
    元素类型：{}\n
    """
    .format(type(na), na.shape, na.ndim, na.size, na.dtype)
)


# 使用np.zeros()创建矩阵，矩阵中所有元素为0
na1 = np.zeros((2, 3))
print("========== zeros() ==========")
print(na1)
print(
    """
    对象类型：{}\n
    矩阵形状：{}\n
    维度（秩）：{}\n
    元素个数：{}\n
    元素类型：{}\n
    """
    .format(type(na1), na1.shape, na1.ndim, na1.size, na1.dtype)
)


# 使用np.ones()创建矩阵，矩阵中所有元素为1
na2 = np.ones((2, 3))
print("========== ones() ==========")
print(na2)
print(
    """
    对象类型：{}\n
    矩阵形状：{}\n
    维度（秩）：{}\n
    元素个数：{}\n
    元素类型：{}\n
    """
    .format(type(na2), na2.shape, na2.ndim, na2.size, na2.dtype)
)

# np.arange() arg1:start, arg2:end(not included)， arg3:step
na3 = np.arange(2, 13, 2)
print("========== arange() ==========")
print(na3)

# 使用reshape()可以将一维数组转化为矩阵，不会改变原数组
# 使用resize()效果与reshape()相同，但是会改变原数组
na4 = na3.reshape(2, 3)
print("========== arange().reshape() ==========")
print(na4)

# linspace(), same like arrange(), arg1:start, arg2:end(includ), arg3:element sum
na5 = np.linspace(2, 10, 5)
print("========== linspace() ==========")
