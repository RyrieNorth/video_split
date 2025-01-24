# video_split

一个简单的用于切割视频的 Python 工具 </br>

## 功能
- 获取视频总长度
- 切割视频
- 自定义输出路径

## 环境要求

- Python 3.6 或更高版本
- `pymediainfo`
- `FFmpeg` 工具（用于切分视频）（已集成在tools文件夹中且已经过裁剪）

## 安装方式

1. 克隆安装：
   ```bash
   git clone https://github.com/RyrieNorth/video_split.git
   cd video_split
   python setup.py install

2. 从release中下载安装(注意版本信息)：
   ```bash
   wget https://github.com/RyrieNorth/video_split/releases/download/v0.1/video_split-0.1-py3-none-any.whl
   pip install video_split-0.1-py3-none-any.whl

3. 如何卸载：
   ```bash
   pip list # 查找 `video_split` 相关字眼, 例如：`video_split`
   pip uninstall video_split
   无论是直接从 python setup.py install 还是在 pip 卸载方式都一样

## 使用方式

1. 在终端直接运行：
   ```bash
    usage: vl_split [-h] -i INPUT [-s SPLIT] [-o OUTPUT]
    
    视频工具
    
    options:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            输入视频文件路径
      -s SPLIT, --split SPLIT
                            分割的份数
      -o OUTPUT, --output OUTPUT
                            输出视频保存目录
2. 获取视频信息：</br></br>
![1](https://github.com/user-attachments/assets/d0583c5e-a177-45c4-b740-d99867c5e016)</br></br>
     ```bash
     vl_split -i 【历史合集】一口气回顾地狱空岛生存发展！

3. 切割视频：</br></br>
![2](https://github.com/user-attachments/assets/f24da11f-197c-40cf-acec-a7e977353c8c)</br></br>
     ```bash
     vl_split -i 【历史合集】一口气回顾地狱空岛生存发展！.mp4 -s 2 -o .
