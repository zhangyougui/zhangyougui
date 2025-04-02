#!/bin/bash

# 从 user-list.txt 中读取用户名
while read -r username; do
    # 检查用户是否已经存在
    if id "$username" &>/dev/null; then
        echo "用户 $username 已存在，跳过创建。"
    else
        # 创建用户
        useradd "$username"
        echo "用户 $username 创建成功。"
    fi
done < user-list.txt
