#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
import time, random

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    sku_ids = '100011540165'  # 商品id
    area = '3_51043_2907'  # 区域id
    # asst = Assistant()  # 初始化
    # asst.login_by_QRcode()  # 扫码登陆
    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=10)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒

    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    # asst.clear_cart()  # 清空购物车（可选）

    # print(asst.get_single_item_stock(sku_ids,1, area))
    # print(asst.if_item_can_be_ordered(sku_ids, area))

    while 1:

        if asst.get_single_item_stock(sku_ids, 1, area):
            print("到货", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            asst.add_item_to_cart(sku_ids)  # 根据商品id添加购物车（可选）
            asst.submit_order()  # 直接提交订单
            print("抢货成功")
            break
        else:
            print("无货", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        tt = random.randint(60, 70)
        time.sleep(tt)

    # print(asst.get_single_item_stock(sku_ids,1, area))
