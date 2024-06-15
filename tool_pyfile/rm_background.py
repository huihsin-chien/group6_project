import cv2
import numpy as np

def remove_background(image_path, output_path):
    # 读取图片
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        print("Could not read the image.")
        return
    
    # 检查图像是否已经有Alpha通道
    if image.shape[2] == 3:
        # 如果图像没有 Alpha 通道，则添加一个
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 使用 Canny 边缘检测
    edges = cv2.Canny(gray, threshold1=50, threshold2=150)
    
    # 找到轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 创建一个掩码，初始化为全黑（全透明）
    mask = np.zeros_like(gray)
    
    # 绘制轮廓，将内部区域填充为白色
    cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)
    
    # 反转掩码
    mask_inv = cv2.bitwise_not(mask)
    
    # 将 mask 应用于图像的 Alpha 通道
    image[:, :, 3] = cv2.bitwise_and(image[:, :, 3], mask)
    
    # 将结果保存为 PNG 文件，以保留透明度
    cv2.imwrite(output_path, image)

# 使用示例
remove_background(r'C:\Users\jianh\OneDrive\git_repo\group6_project\Final_pj\Assets\img\waterbottle.jpg', r'C:\Users\jianh\OneDrive\git_repo\group6_project\Final_pj\Assets\img\waterbottle.png')
