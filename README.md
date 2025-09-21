# MY-DOC-DEMO

整理一下近期的文档，使用本仓库主要是三个目的：

1. 近期频繁异地使用不同设备，同步成本较高，统一放到网页进行同步
2. 复习一下rst，马上要负责一个大项目文档的撰写
3. 学习一下github-action的自动部署



本地小部署 `.git/hooks/pre-commit`

```bash

#!/bin/bash

# 源目录 - 当前仓库中的html文件夹
SOURCE_DIR="docs/build"

# 目标目录 - 本地的web/html
DEST_DIR="D:/backups/nginx-1.28.0/html/sphinx-demo"  # 请根据实际路径修改

# 检查源目录是否存在
if [ ! -d "$SOURCE_DIR" ]; then
    echo "警告: 源目录 $SOURCE_DIR 不存在，跳过拷贝操作"
    exit 0
fi

# 创建目标目录（如果不存在）
mkdir -p "$DEST_DIR"

# 拷贝文件，强制覆盖已存在的文件
echo "正在将 $SOURCE_DIR 拷贝到 $DEST_DIR..."
cp -Rf "$SOURCE_DIR"/* "$DEST_DIR/"

# 检查拷贝是否成功
if [ $? -eq 0 ]; then
    echo "文件拷贝完成"
else
    echo "文件拷贝失败，终止提交"
    exit 1
fi

# 继续执行git commit
exit 0
    


```