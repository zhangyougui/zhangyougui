#!/bin/bash

# 显示当前用户
echo "当前用户: $(whoami)"

# 显示当前系统时间
echo "当前时间: $(date)"

# 显示CPU负载情况
echo "CPU负载情况: $(uptime)"

# 显示磁盘使用情况
echo "磁盘使用情况:"
df -h

# 显示当前内存使用情况
echo "内存使用情况:"
free -m
