import cv2
from PIL import Image, ImageTk
import tkinter as tk


def open_camera(camera_index):
    """
    打开指定索引的摄像头，并在新窗口中显示实时视频流。
    """
    # cap = cv2.VideoCapture(camera_index)
    # cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)  # 创建视频捕获对象
    cap = cv2.VideoCapture(camera_index, cv2.CAP_MSMF)

    camera_window = tk.Toplevel()  # 创建新的顶级窗口
    camera_window.title(f"摄像头 {camera_index}")  # 设置窗口标题

    camera_label = tk.Label(camera_window)  # 创建用于显示视频帧的标签
    camera_label.pack()

    desired_width = 480
    desired_height = 270

    def show_frame():
        """
        捕获摄像头的当前帧，并在标签上显示。
        """
        ret, frame = cap.read()  # 读取一帧视频
        if ret:
            resized_frame = cv2.resize(frame, (desired_width, desired_height))
            frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)  # 将BGR颜色转换为RGB
            img = Image.fromarray(frame)  # 将帧转换为Image对象
            imgtk = ImageTk.PhotoImage(image=img)  # 将Image对象转换为PhotoImage对象
            camera_label.imgtk = imgtk  # 避免垃圾回收
            camera_label.configure(image=imgtk)  # 更新标签的图像
            camera_label.after(10, show_frame)  # 10ms后再次调用此函数

    show_frame()  # 开始显示视频流
