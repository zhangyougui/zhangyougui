# 导入之前定义的函数
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("输入必须是非负整数")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("输入必须是非负整数")
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence[:n]


# 主菜单程序
def main():
    print("多功能数学工具")
    print("===============")

    while True:
        print("\n请选择要执行的功能:")
        print("1. 计算阶乘")
        print("2. 判断素数")
        print("3. 打印斐波那契数列")
        print("4. 退出程序")

        choice = input("请输入选项(1-4): ")

        if choice == '1':
            # 计算阶乘
            try:
                num = int(input("请输入要计算阶乘的非负整数: "))
                print(f"{num}的阶乘是: {factorial(num)}")
            except ValueError as e:
                print(f"错误: {str(e)}")

        elif choice == '2':
            # 判断素数
            try:
                num = int(input("请输入要判断的整数: "))
                if is_prime(num):
                    print(f"{num}是素数")
                else:
                    print(f"{num}不是素数")
            except ValueError as e:
                print(f"错误: {str(e)}")

        elif choice == '3':
            # 打印斐波那契数列
            try:
                length = int(input("请输入要生成的斐波那契数列长度: "))
                fib_seq = fibonacci(length)
                print(f"前{length}个斐波那契数列是: {fib_seq}")
            except ValueError as e:
                print(f"错误: {str(e)}")

        elif choice == '4':
            # 退出程序
            print("感谢使用，程序退出!")
            break

        else:
            print("无效的选项，请重新输入!")


# 运行主程序
if __name__ == "__main__":
    main()