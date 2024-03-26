import tkinter as tk
from tkinter import messagebox, ttk
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
    创建并运行主应用程序，允许用户从检测到的摄像头中选择一个，并查看其视频流。
    """
    window = tk.Tk()
    window.title("摄像头检测器")
    window.geometry("300x150")

    # 检测摄像头并填充下拉菜单
    cameras = detect_cameras()  # 假设返回格式为 [(index, "Camera Name"), ...]
    camera_names = [name for index, name in cameras]

    # 创建标签
    label = tk.Label(window, text="请选择摄像头:")
    label.pack(pady=(20, 5))

    # 创建下拉菜单
    selected_camera_var = tk.StringVar()
    camera_dropdown = ttk.Combobox(window, textvariable=selected_camera_var, values=camera_names)
    camera_dropdown.pack()

    def on_show_camera():
        """
        当用户选择查看摄像头并点击“显示摄像头”按钮时调用。
        """
        camera_index = camera_names.index(selected_camera_var.get())
        camera_id = cameras[camera_index][0]  # 获取选中的摄像头索引
        open_camera(camera_id)  # 显示选定的摄像头视频流

    detect_button = tk.Button(window, text="显示摄像头", command=on_show_camera)
    detect_button.pack(pady=20)

    window.mainloop()


if __name__ == "__main__":
    create_app()
