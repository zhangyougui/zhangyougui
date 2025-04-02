# 雷雨典 324080203104 24机械1班  https://github.com/lyd960/lyd

##bash任务1：系统信息收集
touch sys-info.sh   #生成脚本
nano sys-info.sh    #编辑脚本内容
#!/bin/bash
echo "===current user===: $(whoami)"
echo "===current time===: $(date)"
echo "====CPU load===: $(uptime)"
echo "===disk usage===:"
df -h
echo "===memory usage===:"
free -m
chmod +x sys-info.sh   #赋予施行权限
./sys-info.sh > system-report.txt    #运行脚本并保存输出
cat system-report.txt  #查看输出文件


###bash任务2：批量创建用户

nano user-list.txt  #创建文件

Bob
Alice
Caveil
Davide

#!/bin/bash
touch create-users.sh   #创建一个新的脚本文件

nano create-users.sh   #编辑脚本文件

#!/bin/bash   # 编写脚本内容从 user-list.txt 中读取用户名
while read -r username; do     # 检查用户是否已经存在
    
    if id "$username" &>/dev/null; then
        echo "user $username already exists，skip creation"
    else
        useradd "$username"
        echo "user $username successfully created"    # 创建用户
    fi
done < user-list.txt
chmod +x create-users.sh   #给予执行权限
sudo ./create-users.sh   #运行脚本
cat /etc/passwd | grep -E 'Bob|Alice|Caveil|Davide'  # 检查用户是否创建成功

###python 任务
def factorial(n):
    """
    计算n的阶乘
    
    参数:
        n (int): 非负整数
        
    返回:
        int: n的阶乘
    """
    if n < 0:
        return "输入必须是非负整数"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    """
    判断一个数是否为素数
    
    参数:
        n (int): 要判断的数字
        
    返回:
        bool: 如果是素数返回True，否则返回False
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """
    生成斐波那契数列
    
    参数:
        n (int): 数列的长度
        
    返回:
        list: 包含n个斐波那契数的列表
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence[:n]

def main():
    """
    主函数，提供用户交互菜单
    """
    print("欢迎使用多功能计算程序")
    
    while True:
        print("\n请选择要执行的功能：")
        print("1. 计算阶乘")
        print("2. 判断素数")
        print("3. 打印斐波那契数列")
        print("4. 退出程序")
        
        choice = input("请输入选项(1-4): ")
        
        if choice == '1':
            try:
                num = int(input("请输入要计算阶乘的非负整数: "))
                print(f"{num}的阶乘是: {factorial(num)}")
            except ValueError:
                print("输入无效，请输入一个整数。")
                
        elif choice == '2':
            try:
                num = int(input("请输入要判断的数字: "))
                if is_prime(num):
                    print(f"{num}是素数")
                else:
                    print(f"{num}不是素数")
            except ValueError:
                print("输入无效，请输入一个整数。")
                
        elif choice == '3':
            try:
                length = int(input("请输入斐波那契数列的长度: "))
                if length < 0:
                    print("长度必须是非负整数")
                else:
                    print(f"长度为{length}的斐波那契数列是: {fibonacci(length)}")
            except ValueError:
                print("输入无效，请输入一个整数。")
                
        elif choice == '4':
            print("感谢使用，程序即将退出。")
            break
            
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()


