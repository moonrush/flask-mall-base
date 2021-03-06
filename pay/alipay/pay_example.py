# -*- coding=utf-8 -*-
import logging
import traceback

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.domain.AlipayTradeAppPayModel import AlipayTradeAppPayModel
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayOfflineMaterialImageUploadRequest import AlipayOfflineMaterialImageUploadRequest
from alipay.aop.api.request.AlipayTradeAppPayRequest import AlipayTradeAppPayRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.response.AlipayOfflineMaterialImageUploadResponse import AlipayOfflineMaterialImageUploadResponse
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

if __name__ == '__main__':
    """
    设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
    """
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
    alipay_client_config.app_id = '2016102700771549'
    alipay_client_config.app_private_key = 'MIIEpAIBAAKCAQEAvuGtRvzpUrjGgmLinCq9uCSGMBPSjGtUMAYsi8/gfjznTmTK4zYHsX5nROSXZFep454bM8V0/WnZiXDCwR9Ce7WOjD2YN6pAnv1wyXHTqxg9aCc7sy/kQDidWG1Dj/cXxh948+S1EK9FxmxvGreEPPn2ORgsnE1gs2dnDeROhR2UXVQBJKTwnpmogMZHPcgXDE5BekfR1aZrbN7+IkL2H3dcPUO2+jimx9omcO1jTmsrpii3YF8becz5RqGerYcut0WXgQS0YQBxeCp48KkFjXSgYw+yBDKpu6U7ciaBWdcjj48wRfuPW1I08vOq6p+rm3oPEnPpyt3Bx4xkzActsQIDAQABAoIBAEO9n1rkAoHC5V/8a+N0H6QsAhspzbzbkiMA7eooOclTH9toVcBQumY5L7j5TujjW31V7N1wo9YTLIpkJBmZWGTCx/XpHg4TM5+43b//z1iW36QI2Fz9EAnijaSGEkYTMLK1FJ2pesCTEzYZ4Uwf+KQTKViVxa8qnrjMZ3w8m8kNWnxIgdsIQE7EwEEDqZ8WhZxfmJzC70VHDuA8g5MfzC5l2tsr4bB2trMVyPyQ0Ow0vdOyJwGPUsRj+AwlQxq2Ke4cusDTBW+mDspAbrFYIbJNfDCdYwQci6D9Aeg7yBAlIbxDPgkQPH7uDkJBnug9GnrFYexDzKu8UySjrwctq2ECgYEA9i6J4VeXfKvRXeKZfBVyzhtYwW7fMUqsNgqxuYwpQYCajbib9UJeg0nnSC4zQ08rCTqbtfp1L2hT1AwCifGEoPp0kxRKpv5iCDLDeZ5SDQGOIyxQmO3+44dkrDGhvaYisB57NuH20WqAX4iehoL/AfHEejcUPTKF160bVOua+DUCgYEAxn6I+8TtoMeOsRhlsU4QPdYcWAqTwIbbbm3qvm/6rG3hkecMqLqC6BnCCl9p0uSeC6ckiqh68kHfrnZrOXQ1ZhZiRxZ6igrxYHvwfGhBrAVywadwwSWHXS5HhzQKRpNab/K6tFRiuWo+ECUk5ZnA0TOKQBtv9EcOmTEE0rwGpw0CgYEA5WyxqoQK9XDaiXhoOa9zcokhygMdlb5Vh3en8Zehyx2i63ikP4k+s3PoSuhjddMN9GfePVXQaAH+PZuDsjKWu78tbPR4LfDcQ2+rpGfbZ6uPX1ApPJxv8nN3atJGPYvav+9oPNmRP9DVGjMkKY9jP9iklpFGF1JCUaFN23JG1hECgYAnFTMTn6rKRYCrDgq35o78HfRmwW5mMidyjuHxrUrGOLx5ZezwLAkqeifisva7N5iG4tonExViLeZFC7wBDAiXmUCwjpSCKbVtMfogBMcpf8kgqD9jSGhmyH38+Ros20arVDe+2f62U1z1ANtK+gMlLejCxqQ8jOEq+KPienM04QKBgQDKaQmThGEyS+v3aV9GlwBb9d3tO9UKabTsV2BmMB8v2PQlo5Ubk4PnLAjS0866Tdeh8r/YOSpoeFfKOpv56/ZS39nNImppoX+sc1STz87XO5IFZjHUTGkBaNzb1qTBBq3jLfwG0SJXpkLRk+8SZFoE6+ThF/Y6z0TbKdKl8nrPDw=='
    alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAokyVzV8XRmULA0rEpO2hz119QchMkqBXP/rSdOFTHNFvi0B/5I//AcRPT8SBhH+iQeNTl3/5U24H/FPdDMs7P4PEwnNfjpwUBB6kdGjO/+ehaBFQXTDG/0hixxTgO01S+zZD7zHyc55ie1SstrlqMxygXJQKhfKzGiVRV+hdCKi8KGznoDTueveJrcJydvug+AdzGftbpwX6gs84WjratZfEPt+4s57Y07g75e5nV67TABv9bkvWG39p5HJGh08X9TnU2bYegcDu7lkhJH4afuB0DT/cOtP+Qpu/zjQhcQ62PGEjSOOgnJ0B8l6epbybMj5AwL87d6gpN79g9P2oDQIDAQAB'

    """
    得到客户端对象。
    注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
    logger参数用于打印日志，不传则不打印，建议传递。
    """
    client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)

    """
    系统接口示例：alipay.trade.pay
    """
    # 对照接口文档，构造请求对象
    model = AlipayTradePayModel()

    #  支付授权码
    model.auth_code = "282877775259787048"
    
    # 订单描述 可选
    model.body = "Iphone6 16G"
    # goods_list 订单所含商品列表 可选
    goods_list = list()
    goods1 = GoodsDetail()
    goods1.goods_id = "apple-01"
    goods1.goods_name = "ipad"
    goods1.price = 10
    goods1.quantity = 1
    goods_list.append(goods1)
    model.goods_detail = goods_list

    # 商户操作员编号 可选
    model.operator_id = "yx_001"

    # 商户订单号 必填
    model.out_trade_no = "20180510AB014"

    # 产品码 可选
    model.product_code = "FACE_TO_FACE_PAYMENT"

    # 支付场景 条码支付 bar_code ,声波支付 wave_code
    model.scene = "bar_code"

    # 商户门店编号
    model.store_id = ""
    # 订单标题
    model.subject = "huabeitest"

    # 订单最晚支付时间 m、h、d, 整数值，当天1c，0点关闭
    model.timeout_express = "90m"

    # 订单总金额 ，精确到小数点后两位
    model.total_amount = 1

    request = AlipayTradePayRequest(biz_model=model)
    # 如果有auth_token、app_auth_token等其他公共参数，放在udf_params中
    # udf_params = dict()
    # from alipay.aop.api.constant.ParamConstants import *
    # udf_params[P_APP_AUTH_TOKEN] = "xxxxxxx"
    # request.udf_params = udf_params
    # 执行请求，执行过程中如果发生异常，会抛出，请打印异常栈
    response_content = None
    try:
        response_content = client.execute(request)
    except Exception as e:
        print(traceback.format_exc())
    if not response_content:
        print("failed execute")
    else:
        response = AlipayTradePayResponse()
        # 解析响应结果
        response.parse_response_content(response_content)
        if response.is_success():
            # 如果业务成功，则通过respnse属性获取需要的值
            print("get response trade_no:" + response.trade_no)
        else:
            # 如果业务失败，则从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
            print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)


    """
    带文件的系统接口示例：alipay.offline.material.image.upload
    """
    # 如果没有找到对应Model类，则直接使用Request类，属性在Request类中
    request = AlipayOfflineMaterialImageUploadRequest()
    request.image_name = "我的店"
    request.image_type = "jpg"
    # 设置文件参数
    f = open("/Users/foo/Downloads/IMG.jpg", "rb")
    request.image_content = FileItem(file_name="IMG.jpg", file_content=f.read())
    f.close()
    response_content = None
    try:
        response_content = client.execute(request)
    except Exception as e:
        print(traceback.format_exc())
    if not response_content:
        print("failed execute")
    else:
        response = AlipayOfflineMaterialImageUploadResponse()
        response.parse_response_content(response_content)
        if response.is_success():
            print("get response image_url:" + response.image_url)
        else:
            print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)


    """
    页面接口示例：alipay.trade.page.pay
    """
    # 对照接口文档，构造请求对象
    model = AlipayTradePagePayModel()
    model.out_trade_no = "pay201805020000226"
    model.total_amount = 50
    model.subject = "测试"
    model.body = "支付宝测试"
    model.product_code = "FAST_INSTANT_TRADE_PAY"
    settle_detail_info = SettleDetailInfo()
    settle_detail_info.amount = 50
    settle_detail_info.trans_in_type = "userId"
    settle_detail_info.trans_in = "2088302300165604"
    settle_detail_infos = list()
    settle_detail_infos.append(settle_detail_info)
    settle_info = SettleInfo()
    settle_info.settle_detail_infos = settle_detail_infos
    model.settle_info = settle_info
    sub_merchant = SubMerchant()
    sub_merchant.merchant_id = "2088301300153242"
    model.sub_merchant = sub_merchant
    request = AlipayTradePagePayRequest(biz_model=model)
    # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
    response = client.page_execute(request, http_method="GET")
    print("alipay.trade.page.pay response:" + response)


    """
    构造唤起支付宝客户端支付时传递的请求串示例：alipay.trade.app.pay
    """
    model = AlipayTradeAppPayModel()
    model.timeout_express = "90m"
    model.total_amount = "9.00"
    model.seller_id = "2088301194649043"
    model.product_code = "QUICK_MSECURITY_PAY"
    model.body = "Iphone6 16G"
    model.subject = "iphone"
    model.out_trade_no = "201800000001201"
    request = AlipayTradeAppPayRequest(biz_model=model)
    response = client.sdk_execute(request)
    print("alipay.trade.app.pay response:" + response)
