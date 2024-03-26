import cv2  # 导入opencv库，用于访问摄像头
import platform  # 导入platform库，用于获取操作系统信息


def detect_cameras():
    """
    检测并返回所有已连接的摄像头及其名称（如果可用）。

    :return: 一个列表，包含元组(index, camera_name)，其中index是摄像头的索引，camera_name是摄像头的名称。
    """
    camera_list = []  # 初始化一个空列表，用于存储检测到的摄像头信息
    index = 0  # 从索引0开始检测摄像头

    while True:  # 无限循环，直到没有更多的摄像头可以检测
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # 尝试打开当前索引的摄像头
        if not cap.isOpened():  # 如果当前索引的摄像头无法打开
            break  # 退出循环
        else:  # 如果摄像头成功打开
            if platform.system() == "Windows":  # 如果当前操作系统是Windows
                # 尝试获取摄像头的名称
                camera_name = f"摄像头 {index}"  # 默认名称，包含索引
                from win32com.client import Dispatch
                wmi = Dispatch("WbemScripting.SWbemLocator")  # 使用WMI接口
                wbem_service = wmi.ConnectServer(".", r"root\cimv2")  # 连接到WMI服务
                # 查询所有PnP设备中包含“Camera”字样的设备
                for item in wbem_service.ExecQuery(
                        f"SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%Camera%' OR Description LIKE '%Camera%'"):
                    if item.Description:  # 如果查询到的设备有描述
                        camera_name = item.Description  # 使用设备的描述作为摄像头名称
                        break  # 找到后退出循环
            else:  # 如果不是Windows系统
                camera_name = f"摄像头 {index}"  # 直接使用索引作为摄像头名称
            camera_list.append((index, camera_name))  # 将摄像头索引和名称添加到列表中
            cap.release()  # 释放摄像头资源
        index += 1  # 索引递增，准备检测下一个摄像头

    return camera_list  # 返回检测到的所有摄像头的列表
