# 目录
# 1.脚本的不足
# 2.命令行工具的选型
#
# Python脚本的问题
#
# 1.用户需要手动安装依赖
# 2.涉及到多个脚本，需要手动分发多个脚本
# 3.脚本对于环境的一致性要求比较高,分发时需要确保环境一致
# 4.脚本不放置在系统路径中。需要使用完整路径调用
# 5.脚本无法配置子命令,使用起来比较麻烦
# 6.脚本需要自行维护参数args
# 7.脚本没有提供原生的帮助信息,长期维护成本高
#
# 常用的Python命令行编写工具
#
# 1. cement
# 2. Click
# 3. cliff
# 4. docopt
# 5. python-fire
# 6. python-prompt-toolkit