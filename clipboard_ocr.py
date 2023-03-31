# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import ImageGrab
from pytesseract import pytesseract

# Tesseract OCRの実行ファイルへのパスを設定
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_clipboard_image():
    # クリップボードから画像を取得
    image = ImageGrab.grabclipboard()
    if image is None:
        print("[output]クリップボードに画像がありません。")
        return
    
    # 画像がRGBA形式の場合、RGB形式に変換
    if image.mode == "RGBA":
        image = image.convert("RGB")
    
    # PIL形式の画像をOpenCV形式に変換
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # 表形式データを認識するための設定を削除し、デフォルト設定に戻す
    custom_config = r"--psm 6"
    
    # 画像からテキストを抽出
    text = pytesseract.image_to_string(image, lang="jpn", config=custom_config)
    print("[output]:\n", text)
    print("-----------------------------")

    # 改行を削除する
    text = text.replace('\n', '')
    print("[output](改行削除):\n", text)

if __name__ == "__main__":
    print("[input]スクリーンショットを[Win+S]キーでクリップボードにコピーしてください。")
    
    while True:
        input("[input]画像がクリップボードにコピーされたら、Enterキーを押してください。終了する場合はCtrl+Cを押してください。")
        ocr_clipboard_image()
