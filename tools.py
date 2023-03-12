import os

import cv2
import operator
import time
from io import BytesIO

import numpy as np
import pyautogui
from PIL import ImageGrab, Image


def is_match(baseline, sample, threshold=None):
    """
    图片是否相似
    :param baseline: 基准图片
    :param sample: 样本图片
    :param threshold: 阈值比率
    :return:
    """
    # 缩小至指定尺寸进行对比
    COMPARE_SIZE = baseline.size if baseline.size[0] <= 100 else (100, int(baseline.size[1] * (100 / baseline.size[0])))
    COMPARE_UNITS = COMPARE_SIZE[0] * COMPARE_SIZE[1]  # 对比像素数量
    MATCH_THRESHOLD = int(COMPARE_UNITS * ((1 - threshold) if threshold else (1 / 10)))  # 匹配阈值
    # 缩小图片尺寸 转灰度 减少判断开销
    baseline_image = baseline.resize(COMPARE_SIZE).convert("L")
    sample_image = sample.resize(COMPARE_SIZE).convert("L")

    baseline_image.save('baseline.png')
    sample_image.save('sample.png')
    # 将灰度图标转成列表
    baseline_pixels = list(baseline_image.getdata())
    sample_pixels = list(sample_image.getdata())

    baseline_avg = sum(baseline_pixels) / len(baseline_pixels)
    sample_avg = sum(sample_pixels) / len(sample_pixels)

    baseline_image.point([0 if i < baseline_avg else 1 for i in range(256)], '1').save('baseline_L.png')
    sample_image.point([0 if i < sample_avg else 1 for i in range(256)], '1').save('sample_L.png')

    baseline_hash = [int(pix > baseline_avg) for pix in baseline_pixels]
    sample_hash = [int(pix > sample_avg) for pix in sample_pixels]
    # 统计两个01串不同数字的个数
    match = sum(map(operator.ne, baseline_hash, sample_hash))

    print('tools.is_match | {} | {}'.format(match <= MATCH_THRESHOLD, round((COMPARE_UNITS - match) * 100 / COMPARE_UNITS, 2)))

    return match <= MATCH_THRESHOLD


def loading(position, expation_name, duration=None, once=None, threshold=None, path='./locations'):
    """
    指定位置图标匹配
    :param position:
    :param expation_name:
    :param duration:
    :param once:
    :param threshold:
    :return:
    """
    while 1:
        print('tools.loading | {}'.format(expation_name))
        match = is_match(
            Image.open(os.path.join(path, "{}.jpg".format(expation_name))),
            ImageGrab.grab(position),
            threshold
        )
        if once:
            return match
        if match:
            return match
        time.sleep(duration or 0.5)


def grab(position, name, duration=None):
    """
    区域截屏
    :param position:
    :param name:
    :param duration:
    :return:
    """
    while 1:
        ImageGrab.grab(position).save('{}_{}.jpg'.format(name, int(time.time())))
        time.sleep(duration or 0.5)


def grab_from_file(position, name, filename):
    """
    区域截取图片文件
    :param position:
    :param name:
    :param filename:
    :return:
    """
    Image.open(filename).crop(box=position).convert('RGB').save('{}_{}.jpg'.format(name, int(time.time())))


def template_match(temple_img='test.jpg', base_img=None, threshold=0.90):
    """
    模版匹配图标位置
    :param temple_img:
    :param base_img:
    :param threshold:
    :return:
    """
    if isinstance(base_img, BytesIO):
        base_img.seek(0)
        img_buffer_numpy = np.frombuffer(base_img.read(), dtype=np.uint8)  # 将 图片字节码bytes  转换成一维的numpy数组 到缓存中
        base = cv2.imdecode(img_buffer_numpy, 0)
    else:
        base = cv2.imread(base_img, 0)
    # 读取模板图像
    temple = cv2.imread(temple_img, 0)
    # 获取模板图像的高和宽
    temple_width, temple_height = temple.shape
    # 使用标准相关系数匹配,1表示完美匹配,-1表示糟糕的匹配,0表示没有任何相关性
    result = cv2.matchTemplate(base, temple, cv2.TM_CCOEFF_NORMED)
    # 使用函数 minMaxLoc, 确定匹配结果矩阵的最大值和最小值(val)，以及它们的位置(loc)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print('tools.template_match | {} | {}'.format(temple_img, round(max_val * 100, 2)))
    if max_val < threshold:
        return None

    # 中心位置参数
    return max_loc[0] + int(temple_height / 2), max_loc[1] + int(temple_width / 2)


def locate(temple_img, threshold=0.90, once=True, box=None, path='./locations'):
    """
    定位图标屏幕位置
    :param temple_img:
    :param threshold:
    :param once:
    :param box:
    :return:
    """
    while 1:
        img_bytes = BytesIO()
        ImageGrab.grab(bbox=box).save(img_bytes, format='JPEG')
        result = template_match(temple_img=os.path.join(path, temple_img), base_img=img_bytes, threshold=threshold)
        if once:
            return result
        if result:
            return result


if __name__ == '__main__':
    grab((1470, 300, 1800, 800), 'sdf')
    exit()

    t1 = time.time()
    position = pyautogui.locateOnScreen('1.png')
    if position is not None:
        x, y = pyautogui.center(position)
        print(x, y)
        pyautogui.moveTo(x, y)
    print(time.time() - t1)

    t1 = time.time()
    img_bytes = BytesIO()
    ImageGrab.grab().save(img_bytes, format='JPEG')
    result = template_match(temple_img='1.png', base_img=img_bytes)
    print(result)
    print(time.time() - t1)
