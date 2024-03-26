import tkinter as tk
from tkinter import messagebox
from camera_detector import detect_cameras
from camera_display import open_camera


def show_cameras():
    """
    显示已检测到的摄像头，并询问用户是否打开第一个摄像头。
    """
    cameras = detect_cameras()
    if cameras:
        camera_list = ', '.join(str(cam) for cam in cameras)
        result = messagebox.askyesno("摄像头检测结果", f"检测到摄像头在以下索引：{camera_list}。是否打开第一个摄像头？")
        if result:
            open_camera(cameras[0])
    else:
        messagebox.showinfo("摄像头检测结果", "未检测到摄像头。")


def create_app():
    """
    创建并运行主应用程序。
    """
    window = tk.Tk()
    window.title("摄像头检测器")
    window.geometry("300x100")

    detect_button = tk.Button(window, text="检测摄像头", command=show_cameras)
    detect_button.pack(pady=20)

    window.mainloop()


if __name__ == "__main__":
    create_app()
