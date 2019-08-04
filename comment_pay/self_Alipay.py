# -*- coding: UTF-8 -*-
import base64
import collections
import copy
import json
from datetime import datetime
from urllib import request, parse
import rsa
from alipay import AliPay



class alipay:
    def __init__(self, notify_url=None, charset='gbk', sign_type='RSA2',
                 version='1.0', DEBUG=True):  # 需要注意，自己编码类型是否是RSA2
        self.app_id = '2016100100642916'
        self.requesturl = 'https://openapi.alipay.com/gateway.do' if DEBUG is False else "https://openapi.alipaydev.com/gateway.do"
        self.private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA3xvmGLdMdscuqiCdyp+xA4xJ0ohywqpETGelAIcoEa09y/pA533Erf7zRD5Kaf6xMl6suIEtq6i482En6aSf48ODAeT82YWrlj4kH/iA6R8cdufPU3D9od5li++6Ce0vFzEHWHLUwf7o6wbYgNQ23CPoE5ZiFpH7Fp+Nof+EfH/b9ODoW9ihy6bhA/RMYuycitDmD67O6++dR8iKAUSTAxUmSm5o8OILf6OcxWY1+cFKyfIm6m0RbONWFr6m8cbjvP+enibkB19EEUt91knWtyDk5NIbxERjatjH36yJhYjrFo4ovhT4vwdFb4pe9xrhgkBIu1qYnpvH42ZKOuFdowIDAQABAoIBAGig3sFMhJFXS20BKr5xMUQmsCAJWTgtPSZPnLOoroPLqKVV0MY+1tN6Mn8YbzFR/atPdtR30AEmeMW6FEufplPbxj5HMsSXySYGMk7D7UBmFKU2hKXu4SLd9uUvISGyl1ja50T1ZQ0tC/HcHgAchTWrqRQ2e/11rDipznPgLjNrqhpwHwAtxYT0tXxaqQ0mTThyWoSWD6lZCCjAjyW0uMdgihn/b/L/4QiZo4+jziPF97+kZdGG80Q2lq7mALM0j0keAvu1YCD3QCPcH/40T8FAsVv1sEyHT4vB/MYgwQw14erTeDCPloJhPj4G93MKBD0puo/0gJXdL1IXRSXZyIECgYEA/gvO+BFsz5X+j8GBEP6A/Gwrxv9CyW9AuD7fWRJFbUye7a14Sva1H3Q0aJ1bzyUMpz1aU9uNX4B5F5XrYhlt2KuHT5NgBxXvOStJADB1b+9bTieyDC1BXxIMcLjtbnNymMiT6KXJCa5iIrzWOtkY+8TCMDXAwKg3I0xEYRs85OECgYEA4NMtnTFXxCBqTwS120mjVJCHrT3Ua/qFImzgQ0Ggc/4vTsxtS+tZr0j3qCjYdak1N7ObfnKBXV522PyySYywP9jNOB8dUzP6q5DldIyWslU4ZefUk5PzI+griuj+yJmmp5fZVxnQf3MRpccZ2V4uv+oOTI0BYBBmXZhtTJ5xjwMCgYEA9WjY1cCXeWyvTZWjJZSFa9Le80ww60ACqDlsLrI8yRoESRuTIe9zBmCOJCUmxFNJBuF4uZtU1VXZJFSZ3tkryOviOZfnYtDomDRdP8aQG8KAVF56W9L33GwmAlpSWqlBoZ/ZahuEukpv2JjM5mpD/SqUYFf8zN9y7DFHuPrD92ECgYEA3j+kreojStyIewi7BcYr0eL2XMnsfbmvdrKOl63+gevatFjeCtjjVaYaPH/0S4wz8ZZ5tmxXegdyEVrsnEyZxuP5KuuHP8L4oDWivq5kInKgSAz/VcxB5VMUCEP/6ioKV06DKdl5BSSpY2oJIZo7OLiV3hLeMyrDJu8RzVYsCCUCgYEAkYlpixdd0EVMWdB817iJLcQKhCaFghYqA/dgUrFJkgL9BbGzN56lj+OebzC1bfcdqIuprHx+cb9i4ACTLc6WCCBDPrHgHV/fn1+mOZJgxyvhaHhe1J0ql72/qQ2MqIsyKOT9Rruz0cgjVE5N9WigTkn+wouUVzt9wYloX68e/OQ=
-----END RSA PRIVATE KEY-----
'''
        self.public_key = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmVpMxyqjAyYBbm0Yq4r5c9bjg5J546Ps9dlSVblVFtfIA7y+u14rwCT4BnDvOL4ukohy+2p2IchT/i7fo+T17MRDD8pThNZ6zyaH+PonsKPNtwBKsHtl+00aMK1GUlIi41nLgkP7kA3VunpAKzE1dOLx8nrhp58Ndzdpm85iDShZihHbhNysIzSPM5qh0cP+FOFfg7qSFCi8RDQbpyzYio0JnIlboF+GZdMMApczTiVOcejj+REZbOM37+Jlkg3N5VRMMiDc7pQyu/eNJ3/vDA9BnFHSlpirBbJfgO+NBVKE0zuiP/a65GeHQrPxV5Mn0ClnfqkfqVDoEEgk54ohOQIDAQAB
-----END PUBLIC KEY-----
'''
        self.params = dict(app_id=self.app_id, charset=charset, sign_type=sign_type, version=version,
                           biz_content={}, timestamp='', notify_url=notify_url)

    def _sort(self, params):
        # print(collections.OrderedDict(sorted(dict(params).items(), key=lambda x: x[0])))
        return collections.OrderedDict(sorted(dict(params).items(), key=lambda x: x[0]))

    @staticmethod
    def make_goods_etail(goods_detail=None, alipay_goods_id=None, goods_name=None, quantity=None, price=None,
                         goods_category=None, body=None, show_url=None):
        params = dict(goods_detail=goods_detail, alipay_goods_id=alipay_goods_id, goods_name=goods_name,
                      quantity=quantity, price=price, goods_category=goods_category, body=body, show_url=show_url)
        return dict(filter(lambda x: x[1] is not None, params.items()))

    def _make_sign(self, params, **kwargs):
        private_key = rsa.PrivateKey.load_pkcs1(kwargs.get('private_key', None) or self.private_key)
        sign = base64.b64encode(rsa.sign(params.encode(), private_key, "SHA-256")).decode('gbk')
        return sign

    def _check_sign(self, message, sign, **kwargs):
        message = self._sort(message)
        data = '{'
        for key, value in message.items():
            data += '"{}":"{}",'.format(key, value)
        data = data[:-1] + '}'
        sign = base64.b64decode(sign)
        public_key = rsa.PublicKey.load_pkcs1_openssl_pem(kwargs.get('public_key', None) or self.public_key)
        try:
            rsa.verify(data.encode(), sign, public_key)
            return True
        except Exception:
            return False

    def _make_request(self, params, biz_content, **kwargs):
        buf = ''
        params['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        params['biz_content'] = json.dumps(self._sort(biz_content))
        for key, value in kwargs.items():
            params[key] = value
        params = self._sort(params)
        for key in params:
            buf += '{}={}&'.format(key, params[key])
        params['sign'] = self._make_sign(buf[:-1], **kwargs)
        # print(params)
        # 发射http请求取回数据
        data = request.urlopen(self.requesturl, data=parse.urlencode(params).encode('gbk')).read().decode('gbk')
        # print(parse.urlencode(params).encode('gbk'))
        return data

    def parse_response(self, params, **kwargs):
        sign = params['sign']
        if self._check_sign(dict(filter(lambda x: 'sign' not in x[0], params.items())), sign, **kwargs):
            return True
        else:
            return False

    def trade_pre_create(self, out_trade_no, total_amount, subject, seller_id=None, discountable_amount=None,
                         undiscountable_amount=None, buyer_logon_id=None, body=None, goods_detail=None,
                         operator_id=None, store_id=None, terminal_id=None, timeout_express=None, alipay_store_id=None,
                         royalty_info=None, extend_params=None, **kwargs):
        """
        :param out_trade_no:    商户订单号,64个字符以内、只能包含字母、数字、下划线；需保证在商户端不重复.
        :param total_amount:    订单总金额，单位为元，精确到小数点后两位.
        :param subject:         订单标题.
        :param seller_id:       卖家支付宝用户ID。 如果该值为空，则默认为商户签约账号对应的支付宝用户ID.
        :param discountable_amount:可打折金额. 参与优惠计算的金额，单位为元，精确到小数点后两位，取值范围[0.01,100000000]
        :param undiscountable_amount:不可打折金额. 不参与优惠计算的金额，单位为元，精确到小数点后两位，取值范围[0.01,100000000]
        :param buyer_logon_id:      买家支付宝账号
        :param body:                对交易或商品的描述
        :param goods_detail:        订单包含的商品列表信息.使用make_goods_etail生成. 其它说明详见：“商品明细说明”
        :param operator_id:         商户操作员编号
        :param store_id:            商户门店编号
        :param terminal_id:         商户机具终端编号
        :param timeout_express:     该笔订单允许的最晚付款时间，逾期将关闭交易。取值范围：1m～15d。m-分钟，h-小时，d-天，1c-当天
        :param alipay_store_id:     支付宝店铺的门店ID
        :param royalty_info:        描述分账信息   暂时无效
        :param extend_params:       业务扩展参数	暂时无效
        :param kwargs:              公共参数可在此处暂时覆盖
        :return:
        """
        params = copy.deepcopy(self.params)
        params['method'] = 'alipay.trade.precreate'
        total_amount = round(int(total_amount), 2)
        if discountable_amount:
            discountable_amount = round(int(discountable_amount), 2)
        if undiscountable_amount:
            undiscountable_amount = round(int(undiscountable_amount), 2)
        if discountable_amount:
            if undiscountable_amount is not None:
                if discountable_amount + undiscountable_amount != total_amount:
                    return '传入打折金额错误'
        biz_content = dict(out_trade_no=out_trade_no[:64], total_amount=total_amount, seller_id=seller_id,
                           subject=subject,
                           discountable_amount=discountable_amount, undiscountable_amount=undiscountable_amount,
                           buyer_logon_id=buyer_logon_id, body=body, goods_detail=goods_detail, operator_id=operator_id,
                           store_id=store_id, terminal_id=terminal_id, timeout_express=timeout_express,
                           alipay_store_id=alipay_store_id, royalty_info=royalty_info, extend_params=extend_params)
        # print(biz_content)
        resp = self._make_request(params, dict(filter(lambda x: x[1] is not None, biz_content.items())), **kwargs)
        # print(resp)
        check = eval(resp)
        resp = json.loads(resp)['alipay_trade_precreate_response']
        if self._check_sign(check['alipay_trade_precreate_response'], check['sign']):
            return resp
        return False

    def trade_refund(self, refund_amount, out_trade_no=None, trade_no=None,
                     refund_reason=None, out_request_no=None, operator_id=None, store_id=None,
                     terminal_id=None, **kwargs):
        """
        :param refund_amount:   需要退款的金额，该金额不能大于订单金额,单位为元，支持两位小数
        :param out_trade_no:    商户订单号，不可与支付宝交易号同时为空
        :param trade_no:        支付宝交易号，和商户订单号不能同时为空
        :param refund_reason:   退款的原因说明
        :param out_request_no:  标识一次退款请求，同一笔交易多次退款需要保证唯一，如需部分退款，则此参数必传。
        :param operator_id:     商户的操作员编号
        :param store_id:        商户的门店编号
        :param terminal_id:     商户的终端编号
        :param kwargs:          公共参数可在此处临时覆盖
        :return:
        """
        params = copy.deepcopy(self.params)
        params['method'] = 'alipay.trade.refund'
        refund_amount = round(float(refund_amount), 2)

        biz_content = dict(refund_amount=refund_amount, out_trade_no=out_trade_no, trade_no=trade_no,
                           refund_reason=refund_reason, out_request_no=out_request_no, operator_id=operator_id,
                           store_id=store_id, terminal_id=terminal_id)
        resp = self._make_request(params, dict(filter(lambda x: x[1] is not None, biz_content.items())), **kwargs)
        check = eval(resp)
        resp = json.loads(resp)['alipay_trade_refund_response']
        if self._check_sign(check['alipay_trade_refund_response'], check['sign']):
            return int(resp['code']) == 10000
        return False

    def trade_query(self, out_trade_no, trade_no=None, **kwargs):
        params = copy.deepcopy(self.params)
        params['method'] = 'alipay.trade.query'

        biz_content = dict(out_trade_no=out_trade_no, trade_no=trade_no)
        resp = self._make_request(params, dict(filter(lambda x: x[1] is not None, biz_content.items())), **kwargs)
        check = eval(resp)
        resp = json.loads(resp)['alipay_trade_query_response']
        if self._check_sign(check['alipay_trade_query_response'], check['sign']) and resp['code'] == 10000:
            return resp
        return False

    def init_alipay_cfg(self):
        alipay = AliPay(
            appid=self.app_id,
            app_notify_url=None,  # 默认回调url
            app_private_key_string=self.private_key,
            alipay_public_key_string=self.public_key,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True  # 默认False ,若开启则使用沙盒环境的支付宝公钥
        )
        return alipay

