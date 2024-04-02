
import copy
import json
from pactverify.core import Like, EachLike


def  generate_pact_json_by_response(target_data, pactverify_json=None, is_list=False, separator='$'):
    """
    根据接口返回数据自动生成json格式断言数据
    :param target_data:  返回数据
    :param pactverify_json: 自动生成的断言数据
    :param is_list:
    :return:
    """

    base_types = (float, str, int, bool)

    like_key = separator + Like.__name__
    eachlike_key = separator + EachLike.__name__

    values_key = separator + 'values'
    params_key = separator + 'params'

    if pactverify_json is None:

        if not isinstance(target_data, (list, dict)):
            try:
                tmp = json.loads(target_data)
                if isinstance(tmp, (list, dict)):
                    target_data = tmp
            except Exception as e:
                print('【pactverify生成json断言数据异常】：{}'.format(str(e)))
                return None

        pactverify_json = {}

    if type(target_data) == dict:
        if (is_list):
            pass
        else:
            pactverify_json = {like_key: copy.deepcopy(target_data)}

        for k, v in target_data.items():
            if (is_list):
                target_data[k] = {}
            else:
                pactverify_json[like_key][k] = {}
            if type(v) in base_types:
                if (like_key in pactverify_json.keys()):

                    pactverify_json[like_key][k] = v
                else:

                    pactverify_json[k] = v
            else:
                if (is_list):
                    pactverify_json[k] = generate_pact_json_by_response(v, pactverify_json[k], False, separator)
                else:
                    pactverify_json[like_key][k] = generate_pact_json_by_response(v,
                                                                                  pactverify_json[like_key][
                                                                                      k],
                                                                                  False, separator)

    elif type(target_data) == list:
        if len(target_data) == 0:
            pactverify_json = {
                eachlike_key: {
                    values_key: "空数组占位",
                    params_key: {
                        "minimum": 0
                    }
                }
            }
        else:
            example_data = target_data[0]
            pactverify_json = {
                eachlike_key: example_data
            }
            pactverify_json[eachlike_key] = generate_pact_json_by_response(example_data,
                                                                           pactverify_json[eachlike_key],
                                                                           True, separator)


    elif type(target_data) == type(None):
        pactverify_json = {
            like_key: {
                values_key: "null占位",
                params_key: {
                    "nullable": True
                }
            }
        }

    elif type(target_data) in base_types:
        if is_list:
            pactverify_json = copy.deepcopy(target_data)
        else:
            pactverify_json = {
                like_key: copy.deepcopy(target_data)
            }
    return pactverify_json


if __name__ == '__main__':
    # resposne_data = {
    #     'k1': 'v1',
    #     'k2': None
    # }
    resposne_data={
  "response": {
    "detailOtaList": [
      {
        "cityId": "110020100",
        "countryId": "110019800",
        "crawlTime": 1700112608,
        "hotelStatus": "SUCCESS_STOCK",
        "otaHotelId": "2304547",
        "otaId": 807,
        "roomList": [
          {
            "allotment": 11,
            "personHold": {
              "maxPersonNum": 2
            },
            "productList": [
              {
                "attachment": "",
                  "bookingPrice": {
                  "totalPriceOri": {
                    "amount": 3118,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "costPrice": {
                  "averagePrice": {
                    "amount": 10826,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 9115,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 9116,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 9116,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "34.21",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 3421,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 3421,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 471,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 21652,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 2977,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 18231,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "elongPid": "-2919326087709973557",
                "hasLimitedPrice": True,
                "originPrice": {
                  "averagePrice": {
                    "amount": 11338.842409,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 9547,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 9548,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 9548,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "34.21",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 3421,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 3583,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 493,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 22678,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 3118,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 19095,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "otaOriginPrice": {
                  "totalPrice": {
                    "amount": 22678,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 3118,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "otaPid": "N2Y3OWM5ZjAtZDllZS1lY2Q1LTZlMTgtYjAwMGY0ODg1NzMxOjMzMg==",
                "productDesc": {
                  "bedSimpleDesc": "单人床",
                  "boardInfoList": [
                    {
                      "description": "不含早餐",
                      "included": True
                    }
                  ],
                  "cancellationDescCn": "预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。",
                  "cancellationDescEn": "Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).",
                  "productBedGroup": [
                    {
                      "bedFilters": [
                        201
                      ],
                      "bedTypeList": [
                        {
                          "bedNameCn": "单人床",
                          "id": "4000409782008688296",
                          "num": 1,
                          "type": "单人床"
                        }
                      ],
                      "description": "1张单人床"
                    }
                  ],
                  "rateComment": ""
                },
                "productFeature": "1582208588449584356",
                "productFilter": {
                  "filterBeds": [
                    201
                  ],
                  "filterBoards": 101,
                  "filterInternet": 301
                },
                "productNameCn": "标准房(双人床)",
                "productNameEn": "Standard Double Room",
                "rateplan": {
                  "cancellationInfoList": [
                    {
                      "customerPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-19 23:59:59",
                      "refundable": "1",
                      "startDate": "2023-11-16 13:30:08",
                      "supplierPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "customerPrice": {
                        "amount": 22678,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-20 23:59:59",
                      "refundable": "0",
                      "startDate": "2023-11-19 23:59:59",
                      "supplierPrice": {
                        "amount": 22678,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ]
                },
                "roomNum": 1
              }
            ],
            "roomDesc": {
              "bedDesc": "1张单人床",
              "facilityList": [
                "停车服务",
                "免费WiFi",
                "饮用水"
              ],
              "hasWindow": 2,
              "internet": "",
              "roomBedGroup": [
                {
                  "bedFilters": [
                    201
                  ],
                  "bedTypeList": [
                    {
                      "bedNameCn": "单人床",
                      "id": "4000409782008688296",
                      "num": 1,
                      "type": "单人床"
                    }
                  ],
                  "description": "1张单人床"
                }
              ],
              "roomSize": "面积24平方米",
              "sharedBathroom": 2
            },
            "roomId": "13275788",
            "roomNameCn": "标准房(双人床)",
            "roomNameEn": "Standard Double Room",
            "roomStatus": 1
          },
          {
            "allotment": 1,
            "personHold": {
              "maxPersonNum": 2
            },
            "productList": [
              {
                "attachment": "{\"adultNumForBook\":2,\"blockid\":\"N2Y5MDIwNTYtZTUyNC01MjkxLWRmN2ItNTI2ODFiNTA2ODAyOjMzMg==\",\"children_num\":0,\"commisionPercent\":\"0.0350\",\"currency\":\"USD\",\"eCrawlTime\":1700112607,\"eSearchId\":\"f3c2d8c5-71ff-4611-b838-dc9278b7b5e8\",\"elongPid\":-4914971693533669972,\"exclusive\":\"42.93\",\"fees\":\"4.02\",\"hotelId\":2304547,\"hotelroomnum\":1,\"inclusive\":\"50.53\",\"language\":\"zh-cn\",\"marketing_fee\":\"4.59\",\"model\":\"Merchant\",\"rateInfo\":{\"currency_rate\":7.27315100000000000000,\"currency_type\":\"USD\",\"rate_id\":\"2490362\"},\"roomId\":462099131,\"roomInfo\":{\"benefits\":[{\"benefitName\":\"Parking\",\"id\":\"6\",\"translatedBenefitName\":\"停车服务\"},{\"benefitName\":\"Free WiFi\",\"id\":\"95\",\"translatedBenefitName\":\"免费WiFi\"}],\"blockId\":\"N2Y5MDIwNTYtZTUyNC01MjkxLWRmN2ItNTI2ODFiNTA2ODAyOjMzMg==\",\"blockIdBackup\":\"7f902056-e524-5291-df7b-52681b506802\",\"cancellationPolicy\":{\"cancellationText\":\"Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).\",\"code\":\"0D100P_100P\",\"date\":[{\"before\":\"2023-11-21T00:00:00\",\"rate\":{\"exclusive\":0.00,\"fees\":0.00,\"inclusive\":0.00,\"tax\":0.00}},{\"before\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":85.86,\"fees\":8.04,\"inclusive\":101.06,\"tax\":7.16}},{\"onward\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":85.86,\"fees\":8.04,\"inclusive\":101.06,\"tax\":7.16}}],\"parameter\":[{\"charge\":\"P\",\"days\":1,\"value\":0},{\"charge\":\"P\",\"days\":0,\"value\":100},{\"charge\":\"P\",\"days\":0,\"value\":100}],\"translatedCancellationText\":\"预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。\"},\"dailyRate\":[{\"date\":\"2023-11-21\",\"exclusive\":\"42.93\",\"fees\":\"4.02\",\"inclusive\":\"50.53\",\"tax\":\"3.58\"},{\"date\":\"2023-11-22\",\"exclusive\":\"42.93\",\"fees\":\"4.02\",\"inclusive\":\"50.53\",\"tax\":\"3.58\"}],\"extraBeds\":0,\"normalBedding\":2,\"parentRoomId\":\"462099131\",\"parentRoomName\":\"Suite King\",\"paymentModel\":\"Merchant\",\"promotionDetail\":{\"codeEligible\":False,\"description\":\"期间限订 - 优惠27%！\",\"promotionId\":191032337,\"savingAmount\":20.34},\"rate\":{\"currency\":\"USD\",\"exclusive\":42.93,\"fees\":4.02,\"inclusive\":50.53,\"method\":\"PRPN\",\"tax\":3.58},\"remainingRooms\":1,\"roomId\":\"462099131\",\"roomName\":\"Suite King\",\"surcharges\":[],\"taxBreakdown\":[{\"amount\":3.58,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"1\",\"method\":\"PRPN\",\"percent\":7.0,\"taxDescription\":\"Sales tax\",\"taxable\":\"N\",\"translatedTaxDescription\":\"营业税\",\"typeValue\":\"Tax\"},{\"amount\":4.02,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"2\",\"method\":\"PRPN\",\"percent\":10.0,\"taxDescription\":\"Service charge (taxable)\",\"taxable\":\"Y\",\"translatedTaxDescription\":\"服务费 (应课税)\",\"typeValue\":\"Fee\"}],\"totalPayment\":{\"estimatedCommission\":\"4.59\",\"exclusive\":\"85.86\",\"fees\":\"8.04\",\"inclusive\":\"101.06\",\"tax\":\"7.16\"},\"translatedRoomName\":\"大床套房\"},\"roomName\":\"Suite King\",\"searchid\":630123207643920000,\"surcharges\":[],\"tax\":\"3.58\"}",
                "bookingPrice": {
                  "totalPriceOri": {
                    "amount": 10106,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "costPrice": {
                  "averagePrice": {
                    "amount": 35082,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 29540,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 29540,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 29540,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "110.86",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 11086,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 11086,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 1524,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 70164,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 9647,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 59078,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "elongPid": "-4914971693533669972",
                "hasLimitedPrice": False,
                "originPrice": {
                  "averagePrice": {
                    "amount": 36751.232003,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 30945,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 30945,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 30945,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "110.86",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 11086,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 11613,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 1597,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 73502,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 10106,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 61889,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "otaOriginPrice": {
                  "totalPrice": {
                    "amount": 73502,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 10106,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "otaPid": "N2Y5MDIwNTYtZTUyNC01MjkxLWRmN2ItNTI2ODFiNTA2ODAyOjMzMg==",
                "productDesc": {
                  "bedSimpleDesc": "大床",
                  "boardInfoList": [
                    {
                      "description": "不含早餐",
                      "included": True
                    }
                  ],
                  "cancellationDescCn": "预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。",
                  "cancellationDescEn": "Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).",
                  "productBedGroup": [
                    {
                      "bedFilters": [
                        202
                      ],
                      "bedTypeList": [
                        {
                          "bedNameCn": "特大床",
                          "id": "-2405204229768249819",
                          "num": 1,
                          "type": "大床"
                        }
                      ],
                      "description": "1张特大床"
                    }
                  ],
                  "rateComment": ""
                },
                "productFeature": "-7616188020487911822",
                "productFilter": {
                  "filterBeds": [
                    202
                  ],
                  "filterBoards": 101,
                  "filterInternet": 301
                },
                "productNameCn": "大床套房",
                "productNameEn": "Suite King",
                "rateplan": {
                  "cancellationInfoList": [
                    {
                      "customerPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-19 23:59:59",
                      "refundable": "1",
                      "startDate": "2023-11-16 13:30:08",
                      "supplierPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "customerPrice": {
                        "amount": 73502,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-20 23:59:59",
                      "refundable": "0",
                      "startDate": "2023-11-19 23:59:59",
                      "supplierPrice": {
                        "amount": 73502,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ]
                },
                "roomNum": 1
              }
            ],
            "roomDesc": {
              "bedDesc": "1张特大床",
              "facilityList": [
                "停车服务",
                "免费WiFi"
              ],
              "hasWindow": 2,
              "internet": "",
              "roomBedGroup": [
                {
                  "bedFilters": [
                    202
                  ],
                  "bedTypeList": [
                    {
                      "bedNameCn": "特大床",
                      "id": "-2405204229768249819",
                      "num": 1,
                      "type": "大床"
                    }
                  ],
                  "description": "1张特大床"
                }
              ],
              "roomSize": "面积40平方米",
              "sharedBathroom": 2
            },
            "roomId": "462099131",
            "roomNameCn": "大床套房",
            "roomNameEn": "Suite King",
            "roomStatus": 1
          },
          {
            "allotment": 10,
            "personHold": {
              "maxPersonNum": 2
            },
            "productList": [
              {
                "attachment": "{\"adultNumForBook\":2,\"blockid\":\"YjRmYTNlODgtZjNiNC1iMzc2LTRiYjktYmVmMjdhMmNmMzUzOjMzMg==\",\"children_num\":0,\"commisionPercent\":\"0.0350\",\"currency\":\"USD\",\"eCrawlTime\":1700112607,\"eSearchId\":\"f3c2d8c5-71ff-4611-b838-dc9278b7b5e8\",\"elongPid\":-8861868828510195386,\"exclusive\":\"13.25\",\"fees\":\"1.24\",\"hotelId\":2304547,\"hotelroomnum\":1,\"inclusive\":\"15.59\",\"language\":\"zh-cn\",\"marketing_fee\":\"1.41\",\"model\":\"Merchant\",\"rateInfo\":{\"currency_rate\":7.27315100000000000000,\"currency_type\":\"USD\",\"rate_id\":\"2490362\"},\"roomId\":13275766,\"roomInfo\":{\"benefits\":[{\"benefitName\":\"Parking\",\"id\":\"6\",\"translatedBenefitName\":\"停车服务\"},{\"benefitName\":\"Free WiFi\",\"id\":\"95\",\"translatedBenefitName\":\"免费WiFi\"},{\"benefitName\":\"Drinking water\",\"id\":\"230\",\"translatedBenefitName\":\"饮用水\"}],\"blockId\":\"YjRmYTNlODgtZjNiNC1iMzc2LTRiYjktYmVmMjdhMmNmMzUzOjMzMg==\",\"blockIdBackup\":\"b4fa3e88-f3b4-b376-4bb9-bef27a2cf353\",\"cancellationPolicy\":{\"cancellationText\":\"Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).\",\"code\":\"0D100P_100P\",\"date\":[{\"before\":\"2023-11-21T00:00:00\",\"rate\":{\"exclusive\":0.00,\"fees\":0.00,\"inclusive\":0.00,\"tax\":0.00}},{\"before\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":26.50,\"fees\":2.48,\"inclusive\":31.18,\"tax\":2.20}},{\"onward\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":26.50,\"fees\":2.48,\"inclusive\":31.18,\"tax\":2.20}}],\"parameter\":[{\"charge\":\"P\",\"days\":1,\"value\":0},{\"charge\":\"P\",\"days\":0,\"value\":100},{\"charge\":\"P\",\"days\":0,\"value\":100}],\"translatedCancellationText\":\"预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。\"},\"dailyRate\":[{\"date\":\"2023-11-21\",\"exclusive\":\"13.25\",\"fees\":\"1.24\",\"inclusive\":\"15.59\",\"tax\":\"1.10\"},{\"date\":\"2023-11-22\",\"exclusive\":\"13.25\",\"fees\":\"1.24\",\"inclusive\":\"15.59\",\"tax\":\"1.10\"}],\"extraBeds\":0,\"normalBedding\":2,\"parentRoomId\":\"13275766\",\"parentRoomName\":\"Standard Twin Room\",\"paymentModel\":\"Merchant\",\"promotionDetail\":{\"codeEligible\":False,\"description\":\"期间限订 - 优惠27%！\",\"promotionId\":191032337,\"savingAmount\":6.28},\"rate\":{\"currency\":\"USD\",\"exclusive\":13.25,\"fees\":1.24,\"inclusive\":15.59,\"method\":\"PRPN\",\"tax\":1.10},\"remainingRooms\":10,\"roomId\":\"13275766\",\"roomName\":\"Standard Twin Room\",\"surcharges\":[],\"taxBreakdown\":[{\"amount\":1.10,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"1\",\"method\":\"PRPN\",\"percent\":7.0,\"taxDescription\":\"Sales tax\",\"taxable\":\"N\",\"translatedTaxDescription\":\"营业税\",\"typeValue\":\"Tax\"},{\"amount\":1.24,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"2\",\"method\":\"PRPN\",\"percent\":10.0,\"taxDescription\":\"Service charge (taxable)\",\"taxable\":\"Y\",\"translatedTaxDescription\":\"服务费 (应课税)\",\"typeValue\":\"Fee\"}],\"totalPayment\":{\"estimatedCommission\":\"1.41\",\"exclusive\":\"26.5\",\"fees\":\"2.48\",\"inclusive\":\"31.18\",\"tax\":\"2.20\"},\"translatedRoomName\":\"标准房(双床)\"},\"roomName\":\"Standard Twin Room\",\"searchid\":630123207643920000,\"surcharges\":[],\"tax\":\"1.10\"}",
                "bookingPrice": {
                  "totalPriceOri": {
                    "amount": 3118,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "costPrice": {
                  "averagePrice": {
                    "amount": 10826,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 9115,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 9116,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 9116,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "34.21",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 3421,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 3421,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 471,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 21652,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 2977,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 18231,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "elongPid": "-8861868828510195386",
                "hasLimitedPrice": False,
                "originPrice": {
                  "averagePrice": {
                    "amount": 11338.842409,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 9547,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 9548,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 9548,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "34.21",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 3421,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 3583,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 493,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 22678,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 3118,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 19095,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "otaOriginPrice": {
                  "totalPrice": {
                    "amount": 22678,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 3118,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "otaPid": "YjRmYTNlODgtZjNiNC1iMzc2LTRiYjktYmVmMjdhMmNmMzUzOjMzMg==",
                "productDesc": {
                  "bedSimpleDesc": "单人床",
                  "boardInfoList": [
                    {
                      "description": "不含早餐",
                      "included": True
                    }
                  ],
                  "cancellationDescCn": "预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。",
                  "cancellationDescEn": "Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).",
                  "productBedGroup": [
                    {
                      "bedFilters": [
                        201
                      ],
                      "bedTypeList": [
                        {
                          "bedNameCn": "单人床",
                          "id": "4000409782008688296",
                          "num": 1,
                          "type": "单人床"
                        }
                      ],
                      "description": "1张单人床"
                    }
                  ],
                  "rateComment": ""
                },
                "productFeature": "126171078983649804",
                "productFilter": {
                  "filterBeds": [
                    201
                  ],
                  "filterBoards": 101,
                  "filterInternet": 301
                },
                "productNameCn": "标准房(双床)",
                "productNameEn": "Standard Twin Room",
                "rateplan": {
                  "cancellationInfoList": [
                    {
                      "customerPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-19 23:59:59",
                      "refundable": "1",
                      "startDate": "2023-11-16 13:30:08",
                      "supplierPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "customerPrice": {
                        "amount": 22678,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-20 23:59:59",
                      "refundable": "0",
                      "startDate": "2023-11-19 23:59:59",
                      "supplierPrice": {
                        "amount": 22678,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ]
                },
                "roomNum": 1
              }
            ],
            "roomDesc": {
              "bedDesc": "1张单人床",
              "facilityList": [
                "停车服务",
                "免费WiFi",
                "饮用水"
              ],
              "hasWindow": 2,
              "internet": "",
              "roomBedGroup": [
                {
                  "bedFilters": [
                    201
                  ],
                  "bedTypeList": [
                    {
                      "bedNameCn": "单人床",
                      "id": "4000409782008688296",
                      "num": 1,
                      "type": "单人床"
                    }
                  ],
                  "description": "1张单人床"
                }
              ],
              "roomSize": "面积24平方米",
              "sharedBathroom": 2
            },
            "roomId": "13275766",
            "roomNameCn": "标准房(双床)",
            "roomNameEn": "Standard Twin Room",
            "roomStatus": 1
          },
          {
            "allotment": 2,
            "personHold": {
              "maxPersonNum": 2
            },
            "productList": [
              {
                "attachment": "{\"adultNumForBook\":2,\"blockid\":\"Yjg5ZTVmNjItNzZiMi1kN2M0LWQ0MDItZDlkOWY3Nzc5YjJmOjMzMg==\",\"children_num\":0,\"commisionPercent\":\"0.0350\",\"currency\":\"USD\",\"eCrawlTime\":1700112607,\"eSearchId\":\"f3c2d8c5-71ff-4611-b838-dc9278b7b5e8\",\"elongPid\":2242624979833976095,\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"hotelId\":2304547,\"hotelroomnum\":1,\"inclusive\":\"25.03\",\"language\":\"zh-cn\",\"marketing_fee\":\"2.28\",\"model\":\"Merchant\",\"rateInfo\":{\"currency_rate\":7.27315100000000000000,\"currency_type\":\"USD\",\"rate_id\":\"2490362\"},\"roomId\":294430651,\"roomInfo\":{\"benefits\":[{\"benefitName\":\"Parking\",\"id\":\"6\",\"translatedBenefitName\":\"停车服务\"},{\"benefitName\":\"Free WiFi\",\"id\":\"95\",\"translatedBenefitName\":\"免费WiFi\"},{\"benefitName\":\"Drinking water\",\"id\":\"230\",\"translatedBenefitName\":\"饮用水\"}],\"blockId\":\"Yjg5ZTVmNjItNzZiMi1kN2M0LWQ0MDItZDlkOWY3Nzc5YjJmOjMzMg==\",\"blockIdBackup\":\"b89e5f62-76b2-d7c4-d402-d9d9f7779b2f\",\"cancellationPolicy\":{\"cancellationText\":\"Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).\",\"code\":\"0D100P_100P\",\"date\":[{\"before\":\"2023-11-21T00:00:00\",\"rate\":{\"exclusive\":0.00,\"fees\":0.00,\"inclusive\":0.00,\"tax\":0.00}},{\"before\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":42.52,\"fees\":3.98,\"inclusive\":50.06,\"tax\":3.56}},{\"onward\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":42.52,\"fees\":3.98,\"inclusive\":50.06,\"tax\":3.56}}],\"parameter\":[{\"charge\":\"P\",\"days\":1,\"value\":0},{\"charge\":\"P\",\"days\":0,\"value\":100},{\"charge\":\"P\",\"days\":0,\"value\":100}],\"translatedCancellationText\":\"预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。\"},\"dailyRate\":[{\"date\":\"2023-11-21\",\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"inclusive\":\"25.03\",\"tax\":\"1.78\"},{\"date\":\"2023-11-22\",\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"inclusive\":\"25.03\",\"tax\":\"1.78\"}],\"extraBeds\":0,\"normalBedding\":2,\"parentRoomId\":\"294430651\",\"parentRoomName\":\"Superior Twin\",\"paymentModel\":\"Merchant\",\"promotionDetail\":{\"codeEligible\":False,\"description\":\"期间限订 - 优惠27%！\",\"promotionId\":191032337,\"savingAmount\":10.07},\"rate\":{\"currency\":\"USD\",\"exclusive\":21.26,\"fees\":1.99,\"inclusive\":25.03,\"method\":\"PRPN\",\"tax\":1.78},\"remainingRooms\":2,\"roomId\":\"294430651\",\"roomName\":\"Superior Twin\",\"surcharges\":[],\"taxBreakdown\":[{\"amount\":1.78,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"1\",\"method\":\"PRPN\",\"percent\":7.0,\"taxDescription\":\"Sales tax\",\"taxable\":\"N\",\"translatedTaxDescription\":\"营业税\",\"typeValue\":\"Tax\"},{\"amount\":1.99,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"2\",\"method\":\"PRPN\",\"percent\":10.0,\"taxDescription\":\"Service charge (taxable)\",\"taxable\":\"Y\",\"translatedTaxDescription\":\"服务费 (应课税)\",\"typeValue\":\"Fee\"}],\"totalPayment\":{\"estimatedCommission\":\"2.28\",\"exclusive\":\"42.52\",\"fees\":\"3.98\",\"inclusive\":\"50.06\",\"tax\":\"3.56\"},\"translatedRoomName\":\"高级房(双床)\"},\"roomName\":\"Superior Twin\",\"searchid\":630123207643920000,\"surcharges\":[],\"tax\":\"1.78\"}",
                "bookingPrice": {
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "costPrice": {
                  "averagePrice": {
                    "amount": 17376,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 14630,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 14630,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 14630,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "54.91",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 5491,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 5491,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 755,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 34751,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 4778,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 29260,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "elongPid": "2242624979833976095",
                "hasLimitedPrice": False,
                "originPrice": {
                  "averagePrice": {
                    "amount": 18204.696953,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 15328,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 15328,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 15328,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "54.91",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 5491,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 5753,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 791,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 36409,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 30656,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "otaOriginPrice": {
                  "totalPrice": {
                    "amount": 36409,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "otaPid": "Yjg5ZTVmNjItNzZiMi1kN2M0LWQ0MDItZDlkOWY3Nzc5YjJmOjMzMg==",
                "productDesc": {
                  "bedSimpleDesc": "大床",
                  "boardInfoList": [
                    {
                      "description": "不含早餐",
                      "included": True
                    }
                  ],
                  "cancellationDescCn": "预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。",
                  "cancellationDescEn": "Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).",
                  "productBedGroup": [
                    {
                      "bedFilters": [
                        202
                      ],
                      "bedTypeList": [
                        {
                          "bedNameCn": "双人床",
                          "id": "-6026449967890959129",
                          "num": 1,
                          "type": "大床"
                        }
                      ],
                      "description": "1张双人床"
                    }
                  ],
                  "rateComment": ""
                },
                "productFeature": "4469078496816041269",
                "productFilter": {
                  "filterBeds": [
                    202
                  ],
                  "filterBoards": 101,
                  "filterInternet": 301
                },
                "productNameCn": "高级房(双床)",
                "productNameEn": "Superior Twin",
                "rateplan": {
                  "cancellationInfoList": [
                    {
                      "customerPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-19 23:59:59",
                      "refundable": "1",
                      "startDate": "2023-11-16 13:30:08",
                      "supplierPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "customerPrice": {
                        "amount": 36409,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-20 23:59:59",
                      "refundable": "0",
                      "startDate": "2023-11-19 23:59:59",
                      "supplierPrice": {
                        "amount": 36409,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ]
                },
                "roomNum": 1
              }
            ],
            "roomDesc": {
              "bedDesc": "1张双人床",
              "facilityList": [
                "停车服务",
                "免费WiFi",
                "饮用水"
              ],
              "hasWindow": 2,
              "internet": "",
              "roomBedGroup": [
                {
                  "bedFilters": [
                    202
                  ],
                  "bedTypeList": [
                    {
                      "bedNameCn": "双人床",
                      "id": "-6026449967890959129",
                      "num": 1,
                      "type": "大床"
                    }
                  ],
                  "description": "1张双人床"
                }
              ],
              "roomSize": "面积24平方米",
              "sharedBathroom": 2
            },
            "roomId": "294430651",
            "roomNameCn": "高级房(双床)",
            "roomNameEn": "Superior Twin",
            "roomStatus": 1
          },
          {
            "allotment": 1,
            "personHold": {
              "maxPersonNum": 2
            },
            "productList": [
              {
                "attachment": "{\"adultNumForBook\":2,\"blockid\":\"YmNhZjY2MjMtZDkzZS0yZTlkLTA1NjUtYjkyOWFlMzQ2MDkzOjMzMg==\",\"children_num\":0,\"commisionPercent\":\"0.0350\",\"currency\":\"USD\",\"eCrawlTime\":1700112607,\"eSearchId\":\"f3c2d8c5-71ff-4611-b838-dc9278b7b5e8\",\"elongPid\":424664125745006846,\"exclusive\":\"42.93\",\"fees\":\"4.02\",\"hotelId\":2304547,\"hotelroomnum\":1,\"inclusive\":\"50.53\",\"language\":\"zh-cn\",\"marketing_fee\":\"4.59\",\"model\":\"Merchant\",\"rateInfo\":{\"currency_rate\":7.27315100000000000000,\"currency_type\":\"USD\",\"rate_id\":\"2490362\"},\"roomId\":613479091,\"roomInfo\":{\"benefits\":[{\"benefitName\":\"Parking\",\"id\":\"6\",\"translatedBenefitName\":\"停车服务\"},{\"benefitName\":\"Free WiFi\",\"id\":\"95\",\"translatedBenefitName\":\"免费WiFi\"}],\"blockId\":\"YmNhZjY2MjMtZDkzZS0yZTlkLTA1NjUtYjkyOWFlMzQ2MDkzOjMzMg==\",\"blockIdBackup\":\"bcaf6623-d93e-2e9d-0565-b929ae346093\",\"cancellationPolicy\":{\"cancellationText\":\"Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).\",\"code\":\"0D100P_100P\",\"date\":[{\"before\":\"2023-11-21T00:00:00\",\"rate\":{\"exclusive\":0.00,\"fees\":0.00,\"inclusive\":0.00,\"tax\":0.00}},{\"before\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":85.86,\"fees\":8.04,\"inclusive\":101.06,\"tax\":7.16}},{\"onward\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":85.86,\"fees\":8.04,\"inclusive\":101.06,\"tax\":7.16}}],\"parameter\":[{\"charge\":\"P\",\"days\":1,\"value\":0},{\"charge\":\"P\",\"days\":0,\"value\":100},{\"charge\":\"P\",\"days\":0,\"value\":100}],\"translatedCancellationText\":\"预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。\"},\"dailyRate\":[{\"date\":\"2023-11-21\",\"exclusive\":\"42.93\",\"fees\":\"4.02\",\"inclusive\":\"50.53\",\"tax\":\"3.58\"},{\"date\":\"2023-11-22\",\"exclusive\":\"42.93\",\"fees\":\"4.02\",\"inclusive\":\"50.53\",\"tax\":\"3.58\"}],\"extraBeds\":0,\"normalBedding\":2,\"parentRoomId\":\"613479091\",\"parentRoomName\":\"Suite Double\",\"paymentModel\":\"Merchant\",\"promotionDetail\":{\"codeEligible\":False,\"description\":\"期间限订 - 优惠27%！\",\"promotionId\":191032337,\"savingAmount\":20.34},\"rate\":{\"currency\":\"USD\",\"exclusive\":42.93,\"fees\":4.02,\"inclusive\":50.53,\"method\":\"PRPN\",\"tax\":3.58},\"remainingRooms\":1,\"roomId\":\"613479091\",\"roomName\":\"Suite Double\",\"surcharges\":[],\"taxBreakdown\":[{\"amount\":3.58,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"1\",\"method\":\"PRPN\",\"percent\":7.0,\"taxDescription\":\"Sales tax\",\"taxable\":\"N\",\"translatedTaxDescription\":\"营业税\",\"typeValue\":\"Tax\"},{\"amount\":4.02,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"2\",\"method\":\"PRPN\",\"percent\":10.0,\"taxDescription\":\"Service charge (taxable)\",\"taxable\":\"Y\",\"translatedTaxDescription\":\"服务费 (应课税)\",\"typeValue\":\"Fee\"}],\"totalPayment\":{\"estimatedCommission\":\"4.59\",\"exclusive\":\"85.86\",\"fees\":\"8.04\",\"inclusive\":\"101.06\",\"tax\":\"7.16\"},\"translatedRoomName\":\"双人床套房\"},\"roomName\":\"Suite Double\",\"searchid\":630123207643920000,\"surcharges\":[],\"tax\":\"3.58\"}",
                "bookingPrice": {
                  "totalPriceOri": {
                    "amount": 10106,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "costPrice": {
                  "averagePrice": {
                    "amount": 35082,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 29540,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 29540,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 29540,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "110.86",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 11086,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 11086,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 1524,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 70164,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 9647,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 59078,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "elongPid": "424664125745006846",
                "hasLimitedPrice": False,
                "originPrice": {
                  "averagePrice": {
                    "amount": 36751.232003,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 30945,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 30945,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 30945,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "110.86",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 11086,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 11613,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 1597,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 73502,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 10106,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 61889,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "otaOriginPrice": {
                  "totalPrice": {
                    "amount": 73502,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 10106,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "otaPid": "YmNhZjY2MjMtZDkzZS0yZTlkLTA1NjUtYjkyOWFlMzQ2MDkzOjMzMg==",
                "productDesc": {
                  "bedSimpleDesc": "大床",
                  "boardInfoList": [
                    {
                      "description": "不含早餐",
                      "included": True
                    }
                  ],
                  "cancellationDescCn": "预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。",
                  "cancellationDescEn": "Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).",
                  "productBedGroup": [
                    {
                      "bedFilters": [
                        202
                      ],
                      "bedTypeList": [
                        {
                          "bedNameCn": "特大床",
                          "id": "-2405204229768249819",
                          "num": 1,
                          "type": "大床"
                        }
                      ],
                      "description": "1张特大床"
                    }
                  ],
                  "rateComment": ""
                },
                "productFeature": "-602068621273647667",
                "productFilter": {
                  "filterBeds": [
                    202
                  ],
                  "filterBoards": 101,
                  "filterInternet": 301
                },
                "productNameCn": "双人床套房",
                "productNameEn": "Suite Double",
                "rateplan": {
                  "cancellationInfoList": [
                    {
                      "customerPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-19 23:59:59",
                      "refundable": "1",
                      "startDate": "2023-11-16 13:30:08",
                      "supplierPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "customerPrice": {
                        "amount": 73502,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-20 23:59:59",
                      "refundable": "0",
                      "startDate": "2023-11-19 23:59:59",
                      "supplierPrice": {
                        "amount": 73502,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ]
                },
                "roomNum": 1
              }
            ],
            "roomDesc": {
              "bedDesc": "1张特大床",
              "facilityList": [
                "停车服务",
                "免费WiFi"
              ],
              "hasWindow": 2,
              "internet": "",
              "roomBedGroup": [
                {
                  "bedFilters": [
                    202
                  ],
                  "bedTypeList": [
                    {
                      "bedNameCn": "特大床",
                      "id": "-2405204229768249819",
                      "num": 1,
                      "type": "大床"
                    }
                  ],
                  "description": "1张特大床"
                }
              ],
              "roomSize": "面积40平方米",
              "sharedBathroom": 2
            },
            "roomId": "613479091",
            "roomNameCn": "双人床套房",
            "roomNameEn": "Suite Double",
            "roomStatus": 1
          },
          {
            "allotment": 1,
            "personHold": {
              "maxPersonNum": 2
            },
            "productList": [
              {
                "attachment": "{\"adultNumForBook\":2,\"blockid\":\"Yzc3ZGMwOWEtZmRkYi0zMmIzLTZhOTYtMGZhZWE0ZThiZTFiOjMzMg==\",\"children_num\":0,\"commisionPercent\":\"0.0350\",\"currency\":\"USD\",\"eCrawlTime\":1700112607,\"eSearchId\":\"f3c2d8c5-71ff-4611-b838-dc9278b7b5e8\",\"elongPid\":6963636896630662797,\"exclusive\":\"35.49\",\"fees\":\"3.31\",\"hotelId\":2304547,\"hotelroomnum\":1,\"inclusive\":\"41.77\",\"language\":\"zh-cn\",\"marketing_fee\":\"3.79\",\"model\":\"Merchant\",\"rateInfo\":{\"currency_rate\":7.27315100000000000000,\"currency_type\":\"USD\",\"rate_id\":\"2490362\"},\"roomId\":462100008,\"roomInfo\":{\"benefits\":[{\"benefitName\":\"Parking\",\"id\":\"6\",\"translatedBenefitName\":\"停车服务\"},{\"benefitName\":\"Free WiFi\",\"id\":\"95\",\"translatedBenefitName\":\"免费WiFi\"}],\"blockId\":\"Yzc3ZGMwOWEtZmRkYi0zMmIzLTZhOTYtMGZhZWE0ZThiZTFiOjMzMg==\",\"blockIdBackup\":\"c77dc09a-fddb-32b3-6a96-0faea4e8be1b\",\"cancellationPolicy\":{\"cancellationText\":\"Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).\",\"code\":\"0D100P_100P\",\"date\":[{\"before\":\"2023-11-21T00:00:00\",\"rate\":{\"exclusive\":0.00,\"fees\":0.00,\"inclusive\":0.00,\"tax\":0.00}},{\"before\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":70.98,\"fees\":6.62,\"inclusive\":83.54,\"tax\":5.94}},{\"onward\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":70.98,\"fees\":6.62,\"inclusive\":83.54,\"tax\":5.94}}],\"parameter\":[{\"charge\":\"P\",\"days\":1,\"value\":0},{\"charge\":\"P\",\"days\":0,\"value\":100},{\"charge\":\"P\",\"days\":0,\"value\":100}],\"translatedCancellationText\":\"预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。\"},\"dailyRate\":[{\"date\":\"2023-11-21\",\"exclusive\":\"35.49\",\"fees\":\"3.31\",\"inclusive\":\"41.77\",\"tax\":\"2.97\"},{\"date\":\"2023-11-22\",\"exclusive\":\"35.49\",\"fees\":\"3.31\",\"inclusive\":\"41.77\",\"tax\":\"2.97\"}],\"extraBeds\":0,\"normalBedding\":2,\"parentRoomId\":\"462100008\",\"parentRoomName\":\"Deluxe King Bed Room\",\"paymentModel\":\"Merchant\",\"promotionDetail\":{\"codeEligible\":False,\"description\":\"期间限订 - 优惠27%！\",\"promotionId\":191032337,\"savingAmount\":16.81},\"rate\":{\"currency\":\"USD\",\"exclusive\":35.49,\"fees\":3.31,\"inclusive\":41.77,\"method\":\"PRPN\",\"tax\":2.97},\"remainingRooms\":1,\"roomId\":\"462100008\",\"roomName\":\"Deluxe King Bed Room\",\"surcharges\":[],\"taxBreakdown\":[{\"amount\":2.97,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"1\",\"method\":\"PRPN\",\"percent\":7.0,\"taxDescription\":\"Sales tax\",\"taxable\":\"N\",\"translatedTaxDescription\":\"营业税\",\"typeValue\":\"Tax\"},{\"amount\":3.31,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"2\",\"method\":\"PRPN\",\"percent\":10.0,\"taxDescription\":\"Service charge (taxable)\",\"taxable\":\"Y\",\"translatedTaxDescription\":\"服务费 (应课税)\",\"typeValue\":\"Fee\"}],\"totalPayment\":{\"estimatedCommission\":\"3.79\",\"exclusive\":\"70.98\",\"fees\":\"6.62\",\"inclusive\":\"83.54\",\"tax\":\"5.94\"},\"translatedRoomName\":\"豪华房(大床)\"},\"roomName\":\"Deluxe King Bed Room\",\"searchid\":630123207643920000,\"surcharges\":[],\"tax\":\"2.97\"}",
                "bookingPrice": {
                  "totalPriceOri": {
                    "amount": 8354,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "costPrice": {
                  "averagePrice": {
                    "amount": 29001,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 24419,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 24419,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 24419,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "91.64",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 9164,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 9164,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 1260,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 58003,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 7975,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 48839,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "elongPid": "6963636896630662797",
                "hasLimitedPrice": False,
                "originPrice": {
                  "averagePrice": {
                    "amount": 30379.951727,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 25580,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 25580,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 25580,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "91.64",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 9164,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 9600,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 1320,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 60760,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 8354,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 51160,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "otaOriginPrice": {
                  "totalPrice": {
                    "amount": 60760,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 8354,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "otaPid": "Yzc3ZGMwOWEtZmRkYi0zMmIzLTZhOTYtMGZhZWE0ZThiZTFiOjMzMg==",
                "productDesc": {
                  "bedSimpleDesc": "大床",
                  "boardInfoList": [
                    {
                      "description": "不含早餐",
                      "included": True
                    }
                  ],
                  "cancellationDescCn": "预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。",
                  "cancellationDescEn": "Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).",
                  "productBedGroup": [
                    {
                      "bedFilters": [
                        202
                      ],
                      "bedTypeList": [
                        {
                          "bedNameCn": "特大床",
                          "id": "-2405204229768249819",
                          "num": 1,
                          "type": "大床"
                        }
                      ],
                      "description": "1张特大床"
                    }
                  ],
                  "rateComment": ""
                },
                "productFeature": "-5982678051259250618",
                "productFilter": {
                  "filterBeds": [
                    202
                  ],
                  "filterBoards": 101,
                  "filterInternet": 301
                },
                "productNameCn": "豪华房(大床)",
                "productNameEn": "Deluxe King Bed Room",
                "rateplan": {
                  "cancellationInfoList": [
                    {
                      "customerPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-19 23:59:59",
                      "refundable": "1",
                      "startDate": "2023-11-16 13:30:08",
                      "supplierPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "customerPrice": {
                        "amount": 60760,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-20 23:59:59",
                      "refundable": "0",
                      "startDate": "2023-11-19 23:59:59",
                      "supplierPrice": {
                        "amount": 60760,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ]
                },
                "roomNum": 1
              }
            ],
            "roomDesc": {
              "bedDesc": "1张特大床",
              "facilityList": [
                "停车服务",
                "免费WiFi"
              ],
              "hasWindow": 2,
              "internet": "",
              "roomBedGroup": [
                {
                  "bedFilters": [
                    202
                  ],
                  "bedTypeList": [
                    {
                      "bedNameCn": "特大床",
                      "id": "-2405204229768249819",
                      "num": 1,
                      "type": "大床"
                    }
                  ],
                  "description": "1张特大床"
                }
              ],
              "roomSize": "面积30平方米",
              "sharedBathroom": 2
            },
            "roomId": "462100008",
            "roomNameCn": "豪华房(大床)",
            "roomNameEn": "Deluxe King Bed Room",
            "roomStatus": 1
          },
          {
            "allotment": 4,
            "personHold": {
              "maxPersonNum": 2
            },
            "productList": [
              {
                "attachment": "{\"adultNumForBook\":2,\"blockid\":\"ZDU3NzYwMzctYjY0Mi0xOTQwLWZmMmItZTAwNjNiMmIzYzk2OjMzMg==\",\"children_num\":0,\"commisionPercent\":\"0.0350\",\"currency\":\"USD\",\"eCrawlTime\":1700112607,\"eSearchId\":\"f3c2d8c5-71ff-4611-b838-dc9278b7b5e8\",\"elongPid\":-5976020275049473214,\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"hotelId\":2304547,\"hotelroomnum\":1,\"inclusive\":\"25.03\",\"language\":\"zh-cn\",\"marketing_fee\":\"2.28\",\"model\":\"Merchant\",\"rateInfo\":{\"currency_rate\":7.27315100000000000000,\"currency_type\":\"USD\",\"rate_id\":\"2490362\"},\"roomId\":294438839,\"roomInfo\":{\"benefits\":[{\"benefitName\":\"Parking\",\"id\":\"6\",\"translatedBenefitName\":\"停车服务\"},{\"benefitName\":\"Free WiFi\",\"id\":\"95\",\"translatedBenefitName\":\"免费WiFi\"},{\"benefitName\":\"Drinking water\",\"id\":\"230\",\"translatedBenefitName\":\"饮用水\"}],\"blockId\":\"ZDU3NzYwMzctYjY0Mi0xOTQwLWZmMmItZTAwNjNiMmIzYzk2OjMzMg==\",\"blockIdBackup\":\"d5776037-b642-1940-ff2b-e0063b2b3c96\",\"cancellationPolicy\":{\"cancellationText\":\"Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).\",\"code\":\"0D100P_100P\",\"date\":[{\"before\":\"2023-11-21T00:00:00\",\"rate\":{\"exclusive\":0.00,\"fees\":0.00,\"inclusive\":0.00,\"tax\":0.00}},{\"before\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":42.52,\"fees\":3.98,\"inclusive\":50.06,\"tax\":3.56}},{\"onward\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":42.52,\"fees\":3.98,\"inclusive\":50.06,\"tax\":3.56}}],\"parameter\":[{\"charge\":\"P\",\"days\":1,\"value\":0},{\"charge\":\"P\",\"days\":0,\"value\":100},{\"charge\":\"P\",\"days\":0,\"value\":100}],\"translatedCancellationText\":\"预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。\"},\"dailyRate\":[{\"date\":\"2023-11-21\",\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"inclusive\":\"25.03\",\"tax\":\"1.78\"},{\"date\":\"2023-11-22\",\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"inclusive\":\"25.03\",\"tax\":\"1.78\"}],\"extraBeds\":0,\"normalBedding\":2,\"parentRoomId\":\"294438839\",\"parentRoomName\":\"Superior Double\",\"paymentModel\":\"Merchant\",\"promotionDetail\":{\"codeEligible\":False,\"description\":\"期间限订 - 优惠27%！\",\"promotionId\":191032337,\"savingAmount\":10.07},\"rate\":{\"currency\":\"USD\",\"exclusive\":21.26,\"fees\":1.99,\"inclusive\":25.03,\"method\":\"PRPN\",\"tax\":1.78},\"remainingRooms\":4,\"roomId\":\"294438839\",\"roomName\":\"Superior Double\",\"surcharges\":[],\"taxBreakdown\":[{\"amount\":1.78,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"1\",\"method\":\"PRPN\",\"percent\":7.0,\"taxDescription\":\"Sales tax\",\"taxable\":\"N\",\"translatedTaxDescription\":\"营业税\",\"typeValue\":\"Tax\"},{\"amount\":1.99,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"2\",\"method\":\"PRPN\",\"percent\":10.0,\"taxDescription\":\"Service charge (taxable)\",\"taxable\":\"Y\",\"translatedTaxDescription\":\"服务费 (应课税)\",\"typeValue\":\"Fee\"}],\"totalPayment\":{\"estimatedCommission\":\"2.28\",\"exclusive\":\"42.52\",\"fees\":\"3.98\",\"inclusive\":\"50.06\",\"tax\":\"3.56\"},\"translatedRoomName\":\"高级双人床房\"},\"roomName\":\"Superior Double\",\"searchid\":630123207643920000,\"surcharges\":[],\"tax\":\"1.78\"}",
                "bookingPrice": {
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "costPrice": {
                  "averagePrice": {
                    "amount": 17376,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 14630,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 14630,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 14630,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "54.91",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 5491,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 5491,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 755,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 34751,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 4778,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 29260,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "elongPid": "-5976020275049473214",
                "hasLimitedPrice": False,
                "originPrice": {
                  "averagePrice": {
                    "amount": 18204.696953,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 15328,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 15328,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 15328,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "54.91",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 5491,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 5753,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 791,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 36409,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 30656,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "otaOriginPrice": {
                  "totalPrice": {
                    "amount": 36409,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "otaPid": "ZDU3NzYwMzctYjY0Mi0xOTQwLWZmMmItZTAwNjNiMmIzYzk2OjMzMg==",
                "productDesc": {
                  "bedSimpleDesc": "大床",
                  "boardInfoList": [
                    {
                      "description": "不含早餐",
                      "included": True
                    }
                  ],
                  "cancellationDescCn": "预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。",
                  "cancellationDescEn": "Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).",
                  "productBedGroup": [
                    {
                      "bedFilters": [
                        202
                      ],
                      "bedTypeList": [
                        {
                          "bedNameCn": "双人床",
                          "id": "-6026449967890959129",
                          "num": 1,
                          "type": "大床"
                        }
                      ],
                      "description": "1张双人床"
                    }
                  ],
                  "rateComment": ""
                },
                "productFeature": "1621167317627012419",
                "productFilter": {
                  "filterBeds": [
                    202
                  ],
                  "filterBoards": 101,
                  "filterInternet": 301
                },
                "productNameCn": "高级双人床房",
                "productNameEn": "Superior Double",
                "rateplan": {
                  "cancellationInfoList": [
                    {
                      "customerPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-19 23:59:59",
                      "refundable": "1",
                      "startDate": "2023-11-16 13:30:08",
                      "supplierPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "customerPrice": {
                        "amount": 36409,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-20 23:59:59",
                      "refundable": "0",
                      "startDate": "2023-11-19 23:59:59",
                      "supplierPrice": {
                        "amount": 36409,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ]
                },
                "roomNum": 1
              }
            ],
            "roomDesc": {
              "bedDesc": "1张双人床",
              "facilityList": [
                "停车服务",
                "免费WiFi",
                "饮用水"
              ],
              "hasWindow": 2,
              "internet": "",
              "roomBedGroup": [
                {
                  "bedFilters": [
                    202
                  ],
                  "bedTypeList": [
                    {
                      "bedNameCn": "双人床",
                      "id": "-6026449967890959129",
                      "num": 1,
                      "type": "大床"
                    }
                  ],
                  "description": "1张双人床"
                }
              ],
              "roomSize": "面积24平方米",
              "sharedBathroom": 2
            },
            "roomId": "294438839",
            "roomNameCn": "高级双人床房",
            "roomNameEn": "Superior Double",
            "roomStatus": 1
          },
          {
            "allotment": 8,
            "personHold": {
              "maxPersonNum": 2
            },
            "productList": [
              {
                "attachment": "{\"adultNumForBook\":2,\"blockid\":\"ZWIzOTdjYTgtNmIwMS04NWJjLTczMmYtZjIwNmVjYzlhNjE1OjMzMg==\",\"children_num\":0,\"commisionPercent\":\"0.0350\",\"currency\":\"USD\",\"eCrawlTime\":1700112607,\"eSearchId\":\"f3c2d8c5-71ff-4611-b838-dc9278b7b5e8\",\"elongPid\":-1874319175347129605,\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"hotelId\":2304547,\"hotelroomnum\":1,\"inclusive\":\"25.03\",\"language\":\"zh-cn\",\"marketing_fee\":\"2.28\",\"model\":\"Merchant\",\"rateInfo\":{\"currency_rate\":7.27315100000000000000,\"currency_type\":\"USD\",\"rate_id\":\"2490362\"},\"roomId\":447480041,\"roomInfo\":{\"benefits\":[{\"benefitName\":\"Parking\",\"id\":\"6\",\"translatedBenefitName\":\"停车服务\"},{\"benefitName\":\"Free WiFi\",\"id\":\"95\",\"translatedBenefitName\":\"免费WiFi\"},{\"benefitName\":\"Drinking water\",\"id\":\"230\",\"translatedBenefitName\":\"饮用水\"}],\"blockId\":\"ZWIzOTdjYTgtNmIwMS04NWJjLTczMmYtZjIwNmVjYzlhNjE1OjMzMg==\",\"blockIdBackup\":\"eb397ca8-6b01-85bc-732f-f206ecc9a615\",\"cancellationPolicy\":{\"cancellationText\":\"Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).\",\"code\":\"0D100P_100P\",\"date\":[{\"before\":\"2023-11-21T00:00:00\",\"rate\":{\"exclusive\":0.00,\"fees\":0.00,\"inclusive\":0.00,\"tax\":0.00}},{\"before\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":42.52,\"fees\":3.98,\"inclusive\":50.06,\"tax\":3.56}},{\"onward\":\"2023-11-22T00:00:00\",\"rate\":{\"exclusive\":42.52,\"fees\":3.98,\"inclusive\":50.06,\"tax\":3.56}}],\"parameter\":[{\"charge\":\"P\",\"days\":1,\"value\":0},{\"charge\":\"P\",\"days\":0,\"value\":100},{\"charge\":\"P\",\"days\":0,\"value\":100}],\"translatedCancellationText\":\"预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。\"},\"dailyRate\":[{\"date\":\"2023-11-21\",\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"inclusive\":\"25.03\",\"tax\":\"1.78\"},{\"date\":\"2023-11-22\",\"exclusive\":\"21.26\",\"fees\":\"1.99\",\"inclusive\":\"25.03\",\"tax\":\"1.78\"}],\"extraBeds\":0,\"normalBedding\":2,\"parentRoomId\":\"447480041\",\"parentRoomName\":\"Cozy Studio\",\"paymentModel\":\"Merchant\",\"promotionDetail\":{\"codeEligible\":False,\"description\":\"期间限订 - 优惠27%！\",\"promotionId\":191032337,\"savingAmount\":10.07},\"rate\":{\"currency\":\"USD\",\"exclusive\":21.26,\"fees\":1.99,\"inclusive\":25.03,\"method\":\"PRPN\",\"tax\":1.78},\"remainingRooms\":8,\"roomId\":\"447480041\",\"roomName\":\"Cozy Studio\",\"surcharges\":[],\"taxBreakdown\":[{\"amount\":1.78,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"1\",\"method\":\"PRPN\",\"percent\":7.0,\"taxDescription\":\"Sales tax\",\"taxable\":\"N\",\"translatedTaxDescription\":\"营业税\",\"typeValue\":\"Tax\"},{\"amount\":1.99,\"base\":\"N\",\"currency\":\"USD\",\"id\":\"2\",\"method\":\"PRPN\",\"percent\":10.0,\"taxDescription\":\"Service charge (taxable)\",\"taxable\":\"Y\",\"translatedTaxDescription\":\"服务费 (应课税)\",\"typeValue\":\"Fee\"}],\"totalPayment\":{\"estimatedCommission\":\"2.28\",\"exclusive\":\"42.52\",\"fees\":\"3.98\",\"inclusive\":\"50.06\",\"tax\":\"3.56\"},\"translatedRoomName\":\"舒适单间\"},\"roomName\":\"Cozy Studio\",\"searchid\":630123207643920000,\"surcharges\":[],\"tax\":\"1.78\"}",
                "bookingPrice": {
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "costPrice": {
                  "averagePrice": {
                    "amount": 17376,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 14630,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 14630,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 14630,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "54.91",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 5491,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 5491,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 755,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 34751,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 4778,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 29260,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "elongPid": "-1874319175347129605",
                "hasLimitedPrice": False,
                "originPrice": {
                  "averagePrice": {
                    "amount": 18204.696953,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "averageRoomPrice": {
                    "amount": 15328,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "dailyPriceList": [
                    {
                      "date": "2023-11-21",
                      "price": {
                        "amount": 15328,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "date": "2023-11-22",
                      "price": {
                        "amount": 15328,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ],
                  "extraCharge": {
                    "chargePriceList": [
                      {
                        "chargeAmount": "54.91",
                        "chargeAmountCurrency": "CNY",
                        "chargePriceMode": "CHARGE_IS_PER_STAY",
                        "description": "税和服务费",
                        "included": True,
                        "price": {
                          "amount": 5491,
                          "currency": "CNY",
                          "currencyRate": 1
                        },
                        "type": "TAXANDSERVICEFEE"
                      }
                    ],
                    "total": {
                      "amount": 5753,
                      "currency": "CNY",
                      "currencyRate": 1
                    },
                    "totalOri": {
                      "amount": 791,
                      "currency": "USD",
                      "currencyRate": 7.273151
                    }
                  },
                  "totalPrice": {
                    "amount": 36409,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  },
                  "totalRoomPrice": {
                    "amount": 30656,
                    "currency": "CNY",
                    "currencyRate": 1
                  }
                },
                "otaOriginPrice": {
                  "totalPrice": {
                    "amount": 36409,
                    "currency": "CNY",
                    "currencyRate": 1
                  },
                  "totalPriceOri": {
                    "amount": 5006,
                    "currency": "USD",
                    "currencyRate": 7.273151
                  }
                },
                "otaPid": "ZWIzOTdjYTgtNmIwMS04NWJjLTczMmYtZjIwNmVjYzlhNjE1OjMzMg==",
                "productDesc": {
                  "bedSimpleDesc": "大床",
                  "boardInfoList": [
                    {
                      "description": "不含早餐",
                      "included": True
                    }
                  ],
                  "cancellationDescCn": "预订零风险！2023-11-21之前可随时取消预订，无需支付取消费用！ 如果您在入住当日取消预订，您将被收取订单全额作为取消费。 不能按时抵达酒店住宿办理入住将被视为 No-Show（客人未按照预订日期入住），将被收取预订总额的 100% 作为取消费（酒店政策）。",
                  "cancellationDescEn": "Risk-free booking! Cancel before 2023-11-21 and you'll pay nothing! Any cancellation received on your check-in date will incur a charge of 100% of the booking value. Failure to arrive at your hotel or property will be treated as a No-Show and will incur a charge of 100% of the booking value (Hotel policy).",
                  "productBedGroup": [
                    {
                      "bedFilters": [
                        202
                      ],
                      "bedTypeList": [
                        {
                          "bedNameCn": "双人床",
                          "id": "-6026449967890959129",
                          "num": 1,
                          "type": "大床"
                        }
                      ],
                      "description": "1张双人床"
                    }
                  ],
                  "rateComment": ""
                },
                "productFeature": "2084650065304300200",
                "productFilter": {
                  "filterBeds": [
                    202
                  ],
                  "filterBoards": 101,
                  "filterInternet": 301
                },
                "productNameCn": "舒适单间",
                "productNameEn": "Cozy Studio",
                "rateplan": {
                  "cancellationInfoList": [
                    {
                      "customerPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-19 23:59:59",
                      "refundable": "1",
                      "startDate": "2023-11-16 13:30:08",
                      "supplierPrice": {
                        "amount": 0,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    },
                    {
                      "customerPrice": {
                        "amount": 36409,
                        "currency": "CNY",
                        "currencyRate": 1
                      },
                      "endDate": "2023-11-20 23:59:59",
                      "refundable": "0",
                      "startDate": "2023-11-19 23:59:59",
                      "supplierPrice": {
                        "amount": 36409,
                        "currency": "CNY",
                        "currencyRate": 1
                      }
                    }
                  ]
                },
                "roomNum": 1
              }
            ],
            "roomDesc": {
              "bedDesc": "1张双人床",
              "facilityList": [
                "停车服务",
                "免费WiFi",
                "饮用水"
              ],
              "hasWindow": 2,
              "internet": "",
              "roomBedGroup": [
                {
                  "bedFilters": [
                    202
                  ],
                  "bedTypeList": [
                    {
                      "bedNameCn": "双人床",
                      "id": "-6026449967890959129",
                      "num": 1,
                      "type": "大床"
                    }
                  ],
                  "description": "1张双人床"
                }
              ],
              "roomSize": "面积24平方米",
              "sharedBathroom": 2
            },
            "roomId": "447480041",
            "roomNameCn": "舒适单间",
            "roomNameEn": "Cozy Studio",
            "roomStatus": 1
          }
        ],
        "shotelId": "61556723"
      }
    ],
    "otaCategory": 7,
    "otaId": 807,
    "queryInfo": {
      "checkInDate": 1700496000,
      "checkOutDate": 1700668800,
      "cityId": 110020100,
      "countryId": 110019800,
      "groupId": "e875a98a-a49e-4eff-965a-06592904b094",
      "hotelRankFilter": {
        "hotelRankType": "SALE_RANK"
      },
      "otaCityId": "110020100",
      "otaHotelId": "2304547",
      "otaList": [
        807
      ],
      "prePagePrice": 0,
      "querySeq": 0,
      "regionId": 110020100,
      "roomPerson": [
        {
          "adultNum": 2
        }
      ],
      "shotelId": "61556723"
    },
    "searchId": "f3c2d8c5-71ff-4611-b838-dc9278b7b5e8",
    "serviceStatus": {
      "code": 0,
      "subCode": 0
    },
    "userInfo": {
      "bookingChannel": 8,
      "customerLevel": 1,
      "deviceId": "CEACD181-62B6-46FA-A599-33A3F6CE94E8",
      "memberLevel": 3,
      "orderFrom": -999,
      "requestType": "NORMAL",
      "userId": "33323030",
      "userIp": "49.237.47.45"
    }
  }
}
    pactverify_json = generate_pact_json_by_response(resposne_data, separator='@')
    print(pactverify_json)
    string = json.dumps(pactverify_json)
    print(string)
    with open("test.txt","w") as txt_file:
      txt_file.write(string)
    print(pactverify_json)
    with open("test.txt","r") as f:
      txt=f.read()
    print(txt)
    print(json.loads(txt))
