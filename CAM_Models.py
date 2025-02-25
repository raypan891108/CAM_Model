from colormath.color_appearance_models import Nayatani95, ATD95, CIECAM02
from colormath.color_objects import XYZColor
from colour import Lab_to_XYZ
import numpy as np

def Nayatani95_Model():
    
    #測試樣本顏色 
    #測試 Kaleido 量測紅
    LAB_color = np.array([26.9, 10.9, 3])
    XYZ_color = Lab_to_XYZ(LAB_color)
    

    # 轉換為 XYZColor 物件
    color = XYZColor(XYZ_color[0], XYZ_color[1], XYZ_color[2])

    # 參考白點（使用 D65 標準光源）
    illuminant_d65 = XYZColor(95.05, 100, 108.88)

    # 無彩色背景亮度（Y_ob）- 需大於 0.18
    y_ob = 10 

    # 觀察場景的照度 E_o（單位：lux）
    e_o = 318.31  # 例如標準日光環境

    # 正規化照度 E_or（通常設定與 E_o 相同）
    e_or = 318.31

    # 噪聲參數 n（一般設為 1）
    n = 1

    # 建立 Nayatani95 模型
    model = Nayatani95(
        x=color.xyz_x, y=color.xyz_y, z=color.xyz_z, 
        x_n=illuminant_d65.xyz_x, y_n=illuminant_d65.xyz_y, z_n=illuminant_d65.xyz_z,
        y_ob=y_ob, e_o=e_o, e_or=e_or, n=n
    )
    print(f"XYZ 值: {XYZ_color}")
    # 輸出 Nayatani95 模型計算結果
    print("== Nayatani95 Color Appearance Model ==")
    print(f"Predicted Brightness (B_r): {model.brightness:.2f}")
    print(f"Predicted Chroma (C): {model.chroma:.2f}")
    print(f"Predicted Colorfulness (M): {model.colorfulness:.2f}")
    print(f"Predicted Hue Angle (h): {model.hue_angle:.2f}°")
    print(f"Predicted Saturation (S): {model.saturation:.2f}")
    
    
def ATD95_Model():
    
    #測試樣本顏色 
    #測試 Kaleido 量測紅
    LAB_color = np.array([26.9, 10.9, 3])
    XYZ_color = Lab_to_XYZ(LAB_color)
    
    
    # 轉換為 XYZColor 物件
    color = XYZColor(XYZ_color[0], XYZ_color[1], XYZ_color[2])
    
    # 參考白點（使用 D65 標準光源）
    illuminant_d65 = XYZColor(95.05, 100, 108.88)
    
    
    # 設定模型參數
    y_0_abs = 318.31  # 絕對適應亮度 (cd/m²)
    
    k_1 = 0.05        # 色彩對比參數
    k_2 = 0.15        # 色彩適應參數
    sigma = 300       # 色彩調節參數 (預設 300)
    
    print(f"XYZ 值: {XYZ_color}")
    
    # 建立 ATD95 模型
    model = ATD95(
        x=color.xyz_x, y=color.xyz_y, z=color.xyz_z,
        x_0=illuminant_d65.xyz_x, y_0=illuminant_d65.xyz_y, z_0=illuminant_d65.xyz_z,
        y_0_abs=y_0_abs, k_1=k_1, k_2=k_2, sigma=sigma)
    
    # 輸出結果
    print("== ATD95 Color Appearance Model ==")
    print(f"brightness (A channel): {model.brightness:.2f}")
    print(f"Hue (T & D channels): {model.hue:.2f}°")
    print(f"saturation (K1 & K2 adjusted): {model.saturation:.2f}")
    

def CIECAM02_Model():
    
    #測試樣本顏色 
    #測試 Kaleido 量測紅
    LAB_color = np.array([26.9, 10.9, 3])
    XYZ_color = Lab_to_XYZ(LAB_color)
    
    # 轉換為 XYZColor 物件
    color = XYZColor(XYZ_color[0], XYZ_color[1], XYZ_color[2])

    # 參考白點（D65）
    illuminant_d65 = XYZColor(95.05, 100, 108.88)

    # 設定 CIECAM02 參數
    y_b = 20.0     # 背景亮度
    l_a = 318.31   # 絕對適應亮度（典型照明）
    c = 0.69       # 環境影響指數（標準照明）  （平均/暗淡/黑暗）（0.69/0.59/0.525）
    n_c = 1.0      # 色彩適應係數（標準視覺）  （平均/暗淡/黑暗）（1.0,0.9,0.8）
    f = 1.0        # 環境因子                （平均/暗淡/黑暗）（1.0/0.9/0.8​​）
    d = False       # 抑制適應因子，讓模型自動計算

    print(color)
    # 建立 CIECAM02 模型
    model = CIECAM02(
        x=color.xyz_x, y=color.xyz_y, z=color.xyz_z,
        x_w=illuminant_d65.xyz_x, y_w=illuminant_d65.xyz_y, z_w=illuminant_d65.xyz_z,
        y_b=y_b, l_a=l_a, c=c, n_c=n_c, f=f, d=d
    )

    # 輸出結果
    print("== CIECAM02 Color Appearance Model ==")
    print(f"red-green chromatic response (a): {model.a:.2f}")
    print(f"yellow-blue chromatic response (b): {model.b:.2f}")
    print(f"Brightness (Q): {model.brightness:.2f}")
    print(f"Chroma (C): {model.chroma:.2f}")
    print(f"Colorfulness (M): {model.colorfulness:.2f}")
    print(f"Hue Angle (h): {model.hue_angle:.2f}°")
    print(f"Lightness (J): {model.lightness:.2f}")
    print(f"Saturation (S): {model.saturation:.2f}")


# def CAM02_m1_model():
#     #測試樣本顏色 
#     #測試 Kaleido 量測紅
#     LAB_color = np.array([26.9, 10.9, 3])
#     XYZ_color = Lab_to_XYZ(LAB_color)
    
#     # 轉換為 XYZColor 物件
#     color = XYZColor(XYZ_color[0], XYZ_color[1], XYZ_color[2])

#     # 參考白點（D65）
#     illuminant_d65 = XYZColor(95.05, 100, 108.88)

#     # 設定 CIECAM02 參數
#     l_a = 318.31   # 絕對適應亮度（典型照明）
#     c = 0.69       # 環境影響指數（標準照明）  （平均/暗淡/黑暗）（0.69/0.59/0.525）
#     n_c = 1.0      # 色彩適應係數（標準視覺）  （平均/暗淡/黑暗）（1.0,0.9,0.8）
#     f = 1.0        # 環境因子                （平均/暗淡/黑暗）（1.0/0.9/0.8​​）
#     d = False       # 抑制適應因子，讓模型自動計算

#     print(color)
#     # 建立 CIECAM02 模型
#     model = CIECAM02(
#         x=color.xyz_x, y=color.xyz_y, z=color.xyz_z,
#         x_w=illuminant_d65.xyz_x, y_w=illuminant_d65.xyz_y, z_w=illuminant_d65.xyz_z,
#         x_b = ,y_b = ,z_b= ,
#         l_a=l_a, c=c, n_c=n_c, f=f,p = , d=d
#     )

#     # 輸出結果
#     print("== CIECAM02 Color Appearance Model ==")
#     print(f"red-green chromatic response (a): {model.a:.2f}")
#     print(f"yellow-blue chromatic response (b): {model.b:.2f}")
#     print(f"Brightness (Q): {model.brightness:.2f}")
#     print(f"Chroma (C): {model.chroma:.2f}")
#     print(f"Colorfulness (M): {model.colorfulness:.2f}")
#     print(f"Hue Angle (h): {model.hue_angle:.2f}°")
#     print(f"Lightness (J): {model.lightness:.2f}")
#     print(f"Saturation (S): {model.saturation:.2f}")
