#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from pactverify.utils import generate_pact_json_by_response

if __name__ == '__main__':
  param={
"baseQuery": {
"adultsCount": 2,
"checkInDate": 1706150595,
"checkOutDate": 1706236995,
"mhotelId": "61805649",
"otaHotelId": "48637",
"otaId": 806,
"requestTrace": {
"prePagePriceInv": 0,
"reqSequence": 0,
"reqUuid": "core_prefetch_0A98223A00002A9F0000684968DCCB80",
"traceId": "core_prefetch_0A98223A00002A9F0000684968DCCB80"
},
"roomCount": 1,
"shotelId": "61805649",
"userInfo": {
"channel": 1024
}
},
"cityId": 110020580,
"countryId": 110019800
}
  response=requests.post(url="http://127.0.0.1:9202/pull/getDetail",json=param)

  response_json = response.text
  # 参数说明：响应json数据,契约关键字标识符(默认$)
  pact_json = generate_pact_json_by_response(response_json, separator='$')
  print(pact_json)
  '''
    # 模板生成只会包含$EachLike、$Like,可以根据具体校验需求更改,数组取第一个元素为模板来生成
    {
        '$Like': {
            'msg': 'success',
            'code': 0,
            'data': {
                '$EachLike': {
                    'type_id': 249,
                    'name': '王者荣耀',
                    'order_index': 1,
                    'status': 1,
                    'subtitle': ' ',
                    'game_name': '王者荣耀'
                }
            }
        }
    }
    '''
