#!/usr/bin/env python
import os
import argparse
import json
import platform
from pathlib import Path
import stat
from pymediainfo import MediaInfo


# 给文件添加执行权限
def add_execute_permission(file_path):
    """给文件添加执行权限（Linux系统）"""
    if platform.system() == "Linux":
        # 获取当前文件的权限，并添加执行权限
        st = os.stat(file_path)
        os.chmod(file_path, st.st_mode | stat.S_IEXEC)
    else:
        pass


# 获取当前脚本的目录路径
current_dir = Path(__file__).resolve().parent

# 根据操作系统设置 ffmpeg 的路径
ffmpeg_path = current_dir.joinpath(
    "tools", "ffmpeg.exe" if os.name == "nt" else "ffmpeg"
)


# 获取视频总时长
def get_video_duration(file_path):
    media_info = MediaInfo.parse(file_path)
    data = json.loads(media_info.to_json())
    duration_str = data["tracks"][0]["other_duration"][3]  # 格式如 00:02:24.080
    return duration_str


# 将时长字符串转换为总秒数
def duration_to_seconds(duration):
    hours, minutes, seconds = map(float, duration.split(":"))
    return int(hours * 3600 + minutes * 60 + seconds)


# 将总秒数转换为时长字符串
def seconds_to_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{seconds:06.3f}"


# 获取 ffmpeg 命令路径
def get_ffmpeg_command():
    if not os.path.isfile(ffmpeg_path):
        raise FileNotFoundError(
            f"指定工具文件 {ffmpeg_path} 不存在, 请检查路径或该工具是否存在。"
        )
    return ffmpeg_path


# 分割视频函数
def split_video(input_file, num_parts, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 获取视频时长
    duration_str = get_video_duration(input_file)
    total_seconds = duration_to_seconds(duration_str)
    print(f"当前视频总时长为: {duration_str} ({total_seconds} 秒)")

    # 计算每段的时长
    segment_seconds = total_seconds // num_parts
    print(f"每段视频时长为: {seconds_to_duration(segment_seconds)}")

    # 生成切分命令并执行
    for i in range(num_parts):
        start_time = segment_seconds * i
        output_file = os.path.join(
            output_dir,
            f"{os.path.splitext(os.path.basename(input_file))[0]}_split_{i + 1}.mp4",
        )
        ffmpeg = get_ffmpeg_command()
        command = (
            f"{ffmpeg} -y -ss {seconds_to_duration(start_time)} -t {seconds_to_duration(segment_seconds)} "
            f'-i "{input_file}" -vcodec copy -acodec copy "{output_file}"'
        )
        if i == num_parts - 1:  # 最后一段处理剩余时间
            command = (
                f"{ffmpeg} -y -ss {seconds_to_duration(start_time)} "
                f'-i "{input_file}" -vcodec copy -acodec copy "{output_file}"'
            )
        print(f"执行命令: {command}")
        os.system(command)


# 主函数
def run():
    parser = argparse.ArgumentParser(description="视频工具")
    parser.add_argument("-i", "--input", required=True, help="输入视频文件路径")
    parser.add_argument("-s", "--split", type=int, help="分割的份数")
    parser.add_argument("-o", "--output", help="输出视频保存目录")
    args = parser.parse_args()

    if args.split and args.output:
        # 如果提供了 -s 和 -o 参数，则执行分割逻辑
        split_video(args.input, args.split, args.output)
    else:
        # 如果没有提供 -s 和 -o 参数，则仅输出视频时长
        duration_str = get_video_duration(args.input)
        print(f"当前视频总时长为: {duration_str}")


if __name__ == "__main__":
    run()
