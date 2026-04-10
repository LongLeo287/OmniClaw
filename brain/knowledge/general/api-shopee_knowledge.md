# Knowledge Dump for api-shopee

## File: adspend_response.json
```
{
  "code": 0,
  "message": "OK",
  "request_id": "20251114114917D53FA4AF5A7FD040100D",
  "data": {
    "list": [
      {
        "dimensions": {
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "38984663",
          "reach": "2207000",
          "impressions": "9329192"
        }
      }
    ],
    "page_info": {
      "page_size": 1,
      "total_number": 1,
      "page": 1,
      "total_page": 1
    }
  }
}
```

## File: curl.txt
```
### PRODUCT GMV MAX

# GET PRODUCT GMV MAX METRICS BY STORE ID
curl -G --location 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'advertiser_id=7271210972684451842' \
--data-urlencode 'store_ids=["7495827950440450460"]' \
--data-urlencode 'start_date=2025-11-01' \
--data-urlencode 'end_date=2025-11-18' \
--data-urlencode 'dimensions=["advertiser_id", "stat_time_day"]' \
--data-urlencode 'metrics=["cost", "orders", "cost_per_order", "gross_revenue", "roi", "net_cost"]' \
--data-urlencode 'gmv_max_promotion_types=["PRODUCT"]' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=1000'


### LIVE GMV MAX

# TESTING PLAYGROUND

- Eileen Grace
curl --location --get 'https://business-api.tiktok.com/open_api/v1.3/campaign/get/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'advertiser_id=6899326735087566850'

- Mamaway, NB, chess
curl --location --get 'https://business-api.tiktok.com/open_api/v1.3/campaign/get/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'advertiser_id=7306800699382251521'


### REGULAR Ads

## For single advertiser account
EILEEN GRACE
curl --location --get 'https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'advertiser_id=6899326735087566850' \
--data-urlencode 'service_type=AUCTION' \
--data-urlencode 'report_type=BASIC' \
--data-urlencode 'data_level=AUCTION_ADVERTISER' \
--data-urlencode 'dimensions=["advertiser_id", "stat_time_day"]' \
--data-urlencode 'metrics=["spend", "impressions", "reach"]' \
--data-urlencode 'start_date=2025-11-01' \
--data-urlencode 'end_date=2025-11-18' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=200'

## For grouped advertiser account

1. Get all stores under an ad account: GET /store/list/. Response: store_id
Look for: get ad spending by store_id

TEST - MAMAWAY, NB, CHESS
curl --location --get 'https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'advertiser_id=7306800699382251521' \
--data-urlencode 'service_type=AUCTION' \
--data-urlencode 'report_type=BASIC' \
--data-urlencode 'data_level=AUCTION_CAMPAIGN' \
--data-urlencode 'dimensions=["campaign_id", "stat_time_day"]' \
--data-urlencode 'metrics=["spend", "impressions", "reach"]' \
--data-urlencode 'start_date=2025-11-01' \
--data-urlencode 'end_date=2025-11-17' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=200'

### GMV MAX

## For single advertiser account

# Per advertiser_id
curl --location --get 'https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'advertiser_id=6899326735087566850' \
--data-urlencode 'service_type=AUCTION' \
--data-urlencode 'report_type=TT_SHOP' \
--data-urlencode 'data_level=AUCTION_ADVERTISER' \
--data-urlencode 'dimensions=["advertiser_id", "country_code", "stat_time_day"]' \
--data-urlencode 'metrics=["spend","billed_cost"]' \
--data-urlencode 'start_date=2025-11-13' \
--data-urlencode 'end_date=2025-11-16' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=100'

## For grouped advertiser account

# GET STORE LIST BY ADVERTISER ID
curl --location --get 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/store/list/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'advertiser_id=7579206207240765448'

# Get GMV Max cost by advertiser_id & store_id
curl --location --get 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'advertiser_id=7306800699382251521' \
--data-urlencode 'store_ids=["7494499456018189063"]' \
--data-urlencode 'start_date=2025-11-14' \
--data-urlencode 'end_date=2025-11-16' \
--data-urlencode 'dimensions=["advertiser_id", "stat_time_day"]' \
--data-urlencode 'metrics=["cost", "orders", "cost_per_order", "gross_revenue", "roi", "net_cost"]' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=1000'

curl -g -G "https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/" \
  -H 'Content-Type: application/json' \
  -H 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
  --data-urlencode 'advertiser_id=7377330420947632145' \
  --data-urlencode 'store_ids=["7494060372131481134"]' \
  --data-urlencode 'metrics=["product_name","item_group_id","cost","gross_revenue"]' \
  --data-urlencode 'dimensions=["campaign_id", "item_group_id","stat_time_day"]' \
  --data-urlencode 'filtering={"campaign_ids":["1840491011045426"]}' \
  --data-urlencode 'start_date=2025-11-07' \
  --data-urlencode 'end_date=2025-11-07' \
  --data-urlencode 'page=1' \
  --data-urlencode 'page_size=1000'

curl -g -G "https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/" \
  -H 'Content-Type: application/json' \
  -H 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
  -d 'advertiser_id=7377330420947632145' \
  --data-urlencode 'store_ids=["7494060372131481134"]' \
  --data-urlencode 'metrics=["product_name", "product_status", "item_group_id","cost","gross_revenue"]' \
  --data-urlencode 'dimensions=["item_group_id","stat_time_day"]' \
  --data-urlencode 'filtering={"campaign_ids":["1840491011045426"]}' \
  -d 'start_date=2025-11-07' \
  -d 'end_date=2025-11-07' \
  -d 'page=1' \
  -d 'page_size=1000'


## BC something something
curl --location --get 'https://business-api.tiktok.com/open_api/v1.3/bc/asset/get/' \
--header 'Access-Token: 93d9e78ba3938f3fd77aac5a97de8b76f74e3c89' \
--data-urlencode 'bc_id=7251865807498559489' \
--data-urlencode 'asset_type=TIKTOK_SHOP'
```

## File: docker-compose.yml
```
version: '3.8'

services:
  redis: 
    image: redis:latest
    container_name: eileen-grace-redis
    ports:
      - "6739:6379"
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

## File: escrow-detail.json
```
{
    "escrow_detail": {
      "buyer_payment_info": {
        "bulky_handling_fee": 0,
        "buyer_paid_extended_warranty": 0,
        "buyer_paid_installation_fee": 0,
        "buyer_payment_method": "SPayLater",
        "buyer_service_fee": 2000,
        "buyer_tax_amount": 0,
        "buyer_total_amount": 307100,
        "credit_card_promotion": 0,
        "footwear_tax": 0,
        "icms_tax_amount": 0,
        "import_processing_charge": 0,
        "import_tax_amount": 0,
        "initial_buyer_txn_fee": 0,
        "insurance_premium": 0,
        "iof_tax_amount": 0,
        "is_paid_by_credit_card": false,
        "merchant_subtotal": 349000,
        "seller_voucher": -10000,
        "shipping_fee": 0,
        "shipping_fee_sst_amount": 0,
        "shopee_coins_redeemed": 0,
        "shopee_voucher": -33900,
        "total_tax_and_fees_amount": 0,
        "trade_in_bonus": 0,
        "trade_in_discount": 0
      },
      "buyer_user_name": "tri0900beutyshop",
      "order_income": {
        "actual_installation_fee": 0,
        "actual_shipping_fee": 3500,
        "buyer_paid_extended_warranty": 0,
        "buyer_paid_shipping_fee": 0,
        "buyer_payment_method": "SPayLater",
        "buyer_total_amount": 307100,
        "buyer_transaction_fee": 1000,
        "campaign_fee": 0,
        "coins": 0,
        "commission_fee": 32883,
        "cost_of_goods_sold": 349000,
        "credit_card_promotion": 0,
        "credit_card_transaction_fee": 1000,
        "cross_border_tax": 0,
        "delivery_seller_protection_fee_premium_amount": 0,
        "drc_adjustable_refund": 0,
        "escrow_amount": 285205,
        "escrow_import_tax": 0,
        "escrow_tax": 0,
        "estimated_shipping_fee": 3500,
        "final_escrow_product_gst": 0,
        "final_escrow_shipping_gst": 0,
        "final_product_protection": 0,
        "final_product_vat_tax": 0,
        "final_return_to_seller_shipping_fee": 0,
        "final_shipping_fee": 0,
        "final_shipping_vat_tax": 0,
        "fsf_seller_protection_fee_claim_amount": 0,
        "installation_fee_paid_by_buyer": 0,
        "instalment_plan": "1x",
        "items": [
          {
            "activity_id": 379949064402867,
            "activity_type": "add_on_deal",
            "ams_commission_fee": 0,
            "buyer_paid_extended_warranty": 0,
            "discount_from_coin": 0,
            "discount_from_voucher_seller": 10000,
            "discount_from_voucher_shopee": 33900,
            "discounted_price": 349000,
            "installation_fee_paid_by_buyer": 0,
            "is_b2c_shop_item": false,
            "is_main_item": true,
            "item_id": 460504215,
            "item_name": "EILEEN GRACE - Moisturize Rose Jelly Mask 300 ml | Masker Wajah | Jerawat | Bruntus | Bopeng | Bekas Jerawat | Kemerahan | Skin Barrier | Mencerahkan | Melembapkan",
            "item_sku": "",
            "model_id": 290663617998,
            "model_name": "Rose Jelly Mask",
            "model_sku": "EIGR0007",
            "original_price": 499000,
            "quantity_purchased": 1,
            "seller_discount": 150000,
            "seller_order_processing_fee": 1250,
            "selling_price": 349000,
            "shopee_discount": 0
          },
          {
            "activity_id": 379949064402867,
            "activity_type": "add_on_deal",
            "ams_commission_fee": 0,
            "buyer_paid_extended_warranty": 0,
            "discount_from_coin": 0,
            "discount_from_voucher_seller": 0,
            "discount_from_voucher_shopee": 0,
            "discounted_price": 0,
            "installation_fee_paid_by_buyer": 0,
            "is_b2c_shop_item": false,
            "is_main_item": false,
            "item_id": 42773159444,
            "item_name": "Black Jelly Mask 35ml",
            "item_sku": "EIGR9992",
            "model_id": 0,
            "model_name": "",
            "model_sku": "",
            "original_price": 499999,
            "quantity_purchased": 1,
            "seller_discount": 499999,
            "seller_order_processing_fee": 0,
            "selling_price": 0,
            "shopee_discount": 0
          }
        ],
        "order_ams_commission_fee": 0,
        "order_chargeable_weight": 0,
        "order_discounted_price": 349000,
        "order_original_price": 998999,
        "order_seller_discount": 649999,
        "order_selling_price": 349000,
        "original_cost_of_goods_sold": 349000,
        "original_price": 499000,
        "original_shopee_discount": 0,
        "overseas_return_service_fee": 0,
        "payment_promotion": 0,
        "prorated_coins_value_offset_return_items": 0,
        "prorated_payment_channel_promo_bank_offset_return_items": 0,
        "prorated_payment_channel_promo_shopee_offset_return_items": 0,
        "prorated_seller_voucher_offset_return_items": 0,
        "prorated_shopee_voucher_offset_return_items": 0,
        "reverse_shipping_fee": 0,
        "reverse_shipping_fee_sst": 0,
        "rsf_seller_protection_fee_claim_amount": 0,
        "sales_tax_on_lvg": 0,
        "seller_coin_cash_back": 0,
        "seller_discount": 150000,
        "seller_lost_compensation": 0,
        "seller_order_processing_fee": 1250,
        "seller_return_refund": 0,
        "seller_shipping_discount": 0,
        "seller_transaction_fee": 0,
        "seller_voucher_code": [
          "EILEOKTT"
        ],
        "service_fee": 19662,
        "shipping_fee_discount_from_3pl": 0,
        "shipping_fee_sst": 0,
        "shipping_seller_protection_fee_amount": 0,
        "shopee_discount": 0,
        "shopee_shipping_rebate": 3500,
        "tenure_info_list": [
          {
            "instalment_plan": "1x"
          }
        ],
        "trade_in_bonus_by_seller": 0,
        "vat_on_imported_goods": 0,
        "voucher_from_seller": 10000,
        "voucher_from_shopee": 33900,
        "withholding_pit_tax": 0,
        "withholding_tax": 0,
        "withholding_vat_tax": 0
      },
      "order_sn": "25101424NYKBHG",
      "return_order_sn_list": []
    }
  }
```

## File: gmvmax-response.json
```
{
  "code": 0,
  "message": "OK",
  "request_id": "20251114113337267C3017B572313C5F0A",
  "data": {
    "page_info": {
      "page_size": 26,
      "page": 1,
      "total_number": 26,
      "total_page": 1
    },
    "list": [
      {
        "dimensions": {
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "6865538",
          "billed_cost": "6865538"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-07 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "11358015",
          "billed_cost": "11358015"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-02 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "5582123",
          "billed_cost": "5582123"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-07 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-02 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-10 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "12936042",
          "billed_cost": "12915271"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-05 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "9941071",
          "billed_cost": "9714060"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-08 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-03 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "5763834",
          "billed_cost": "4990692"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-08 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "6249525",
          "billed_cost": "6249525"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-10 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-05 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-03 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "11832322",
          "billed_cost": "11832322"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-01 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-11 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-06 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-06 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "7003382",
          "billed_cost": "7003382"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-01 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "7291475",
          "billed_cost": "7291475"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-11 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "34697710",
          "billed_cost": "34631273"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-09 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "9663607",
          "billed_cost": "9663607"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-04 00:00:00",
          "country_code": "ID",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "10465411",
          "billed_cost": "10465411"
        }
      },
      {
        "dimensions": {
          "stat_time_day": "2025-11-09 00:00:00",
          "country_code": "None",
          "advertiser_id": "6899326735087566850"
        },
        "metrics": {
          "spend": "0",
          "billed_cost": "0"
        }
      }
    ]
  }
}
```

## File: index.js
```
import express from 'express';
import { Queue } from 'bullmq';
import 'dotenv/config';
import Redis from 'ioredis';

const app = express();
// const port = 3000;
const port = process.env.PORT || 8080;

const redisConnection = {
    connection: {
        url: process.env.REDIS_URL,
        connectTimeout: 30000,
    }
}

const orderQueue = new Queue("order-processing", redisConnection);
const orderQueueMD = new Queue("fetch-orders-md", redisConnection);
const orderQueueSHRD = new Queue("fetch-orders-shrd", redisConnection);
const orderQueueCLEV = new Queue("fetch-orders-clev", redisConnection);
const orderQueueDRJOU = new Queue("fetch-orders-drjou", redisConnection);
const orderQueueMOSS = new Queue("fetch-orders-moss", redisConnection);
const orderQueueGB = new Queue("fetch-orders-gb", redisConnection);
const orderQueueIL = new Queue("fetch-orders-il", redisConnection);
const orderQueueEV = new Queue("fetch-orders-evoke", redisConnection);
const orderQueueMMW = new Queue("fetch-orders-mmw", redisConnection);
const orderQueueCHESS = new Queue("fetch-orders-chess", redisConnection);
const orderQueueSV = new Queue("fetch-orders-sv", redisConnection);
const orderQueuePN = new Queue("fetch-orders-pn", redisConnection);
const orderQueueNB = new Queue("fetch-orders-nb", redisConnection);
const orderQueueMIRAE = new Queue("fetch-orders-mirae", redisConnection);
const orderQueuePOLY = new Queue("fetch-orders-poly", redisConnection);

app.get('/trigger-daily-sync', async (req, res) => {

    if(req.header('X-Cloud-Scheduler-Job') !== 'true') {
        console.warn("Unauthorized attempt to trigger daily sync");
        return res.status(403).send('Forbidden');
    }

    try {
        const timestamp = new Date().toISOString();
        
        // Base options to keep code clean
        const baseOptions = {
            attempts: 5,
            backoff: { type: 'exponential', delay: 60000 }
        };

        // --- GROUP 1: Shared Account Risk (Evoke, DrJou, Swissvita) ---
        // These MUST NOT run together. We force a 3-minute gap.

        // 1. Evoke: Starts Immediately
        await orderQueueEV.add('fetch-orders-evoke', {}, { 
            ...baseOptions, 
            jobId: `evoke-daily-sync-${timestamp}`,
            delay: 0 
        });

        // 2. Dr. Jou: Starts +3 minutes later
        await orderQueueDRJOU.add('fetch-orders-drjou', {}, { 
            ...baseOptions, 
            jobId: `drjou-daily-sync-${timestamp}`,
            delay: 180000 
        });

        // 3. Swissvita: Starts +6 minutes later
        await orderQueueSV.add('fetch-orders-sv', {}, { 
            ...baseOptions, 
            jobId: `sv-daily-sync-${timestamp}`,
            delay: 360000 
        });

        // --- GROUP 2: Independent Brands ---
        // Stagger these by 45 seconds so they don't hit the API all at once.
        
        let stagger = 30000; // Start the first one 30 seconds in
        const interval = 45000; // Add 45 seconds for each subsequent brand

        // Eileen Grace
        await orderQueue.add('fetch-daily-orders', {}, { 
            ...baseOptions, 
            jobId: `daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Miss Daisy
        await orderQueueMD.add('fetch-orders-md', {}, { 
            ...baseOptions, 
            jobId: `md-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // SH-RD
        await orderQueueSHRD.add('fetch-orders-shrd', {}, { 
            ...baseOptions, 
            jobId: `shrd-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Cleviant
        await orderQueueCLEV.add('fetch-orders-clev', {}, { 
            ...baseOptions, 
            jobId: `clev-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Mosseru
        await orderQueueMOSS.add('fetch-orders-moss', {}, { 
            ...baseOptions, 
            jobId: `moss-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // G-Belle
        await orderQueueGB.add('fetch-orders-gb', {}, { 
            ...baseOptions, 
            jobId: `gb-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Ivy & Lily
        await orderQueueIL.add('fetch-orders-il', {}, { 
            ...baseOptions, 
            jobId: `il-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Mamaway
        await orderQueueMMW.add('fetch-orders-mmw', {}, { 
            ...baseOptions, 
            jobId: `mmw-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Chess
        await orderQueueCHESS.add('fetch-orders-chess', {}, { 
            ...baseOptions, 
            jobId: `chess-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Past Nine
        await orderQueuePN.add('fetch-orders-pn', {}, { 
            ...baseOptions, 
            jobId: `pn-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Nutri Beyond
        await orderQueueNB.add('fetch-orders-nb', {}, { 
            ...baseOptions, 
            jobId: `nb-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Mirae
        await orderQueueMIRAE.add('fetch-orders-mirae', {}, { 
            ...baseOptions, 
            jobId: `mirae-daily-sync-${timestamp}`, 
            delay: stagger 
        });
        stagger += interval;

        // Polynia
        await orderQueuePOLY.add('fetch-orders-poly', {}, { 
            ...baseOptions, 
            jobId: `poly-daily-sync-${timestamp}`, 
            delay: stagger 
        });

        console.log("Daily sync job enqueued by Cloud Scheduler with Staggered Delays");
        res.status(200).send("Successfully enqueued daily sync job");
    } catch (e) {
        console.error("Failed to enqueue daily job: ", e);
        res.status(500).send("Failed to enqueue job");
    }
});

app.get("/orders", async (req, res) => {
    try {
        await orderQueue.add('manual-fetch', {}).catch(err => {
            throw new Error("Failed to enqueue job: " + err.message);
        });
        console.log("Manual fetch enqueued.");
        res.json({
            message: "Job to fetch and process orders has been enqueued." 
        });
    } catch (e) {
        res.status(500).json({ error: "Failed to enqueue job", details: e.message });
    }
});


// 1. ENDPOINT TO PAUSE THE QUEUE
app.get('/admin/pause-queue', async (req, res) => {
    try {
        await orderQueue.pause();
        await orderQueueMD.pause();
        await orderQueueSHRD.pause();
        await orderQueueCLEV.pause();

        console.log("ADMIN: all queues have been paused.");
        res.status(200).send("All queues have been PAUSED.");
    } catch (e) {
        console.error("ADMIN: Error pausing queue:", e);
        res.status(500).send("Error pausing queue");
    }
});

// 2. ENDPOINT TO REMOVE A SPECIFIC JOB
app.get('/admin/remove-job', async (req, res) => {
    const { jobId } = req.query; // Get jobId from query: ?jobId=...

    if (!jobId) {
        return res.status(400).send("Missing 'jobId' query parameter.");
    }

    try {
        const job = await orderQueue.getJob(jobId);
        if (job) {
            await job.remove();
            console.log(`ADMIN: Successfully removed job ${jobId}.`);
            res.status(200).send(`Successfully removed job ${jobId}.`);
        } else {
            console.log(`ADMIN: Job ${jobId} not found.`);
            res.status(404).send(`Job ${jobId} not found.`);
        }
    } catch (e) {
        console.error(`ADMIN: Error removing job ${jobId}:`, e);
        res.status(500).send(`Error removing job ${jobId}`);
    }
});

// 3. ENDPOINT TO RESUME THE QUEUE
app.get('/admin/resume-queue', async (req, res) => {
    try {
        await orderQueue.resume();
        await orderQueueMD.resume();
        await orderQueueSHRD.resume();
        await orderQueueCLEV.resume();
        await orderQueueDRJOU.resume();
        await orderQueueMOSS.resume();
        await orderQueueGB.resume();
        await orderQueueIL.resume();
        await orderQueueEV.resume();
        await orderQueueMMW.resume();
        await orderQueueCHESS.resume();
        await orderQueueSV.resume();
        await orderQueuePN.resume();
        await orderQueueNB.resume();
        await orderQueueMIRAE.resume();
        await orderQueuePOLY.resume();
        
        console.log("ADMIN: all queues have been resumed");
        res.status(200).send("All queues have been RESUMED.");
    } catch (e) {
        console.error("ADMIN: Error resuming queue:", e);
        res.status(500).send("Error resuming queue");
    }
});


app.get('/admin/stop-all-jobs', async (req, res) => {
    try {
        const queues = [
            orderQueue, orderQueueMD, orderQueueSHRD, orderQueueCLEV, 
            orderQueueDRJOU, orderQueueMOSS, orderQueueGB, orderQueueIL, 
            orderQueueEV, orderQueueMMW, orderQueueCHESS, orderQueueSV, 
            orderQueuePN, orderQueueNB, orderQueueMIRAE, orderQueuePOLY
        ];

        console.log("ADMIN: Pausing all queues...");
        await Promise.all(queues.map(q => q.pause()));

        console.log("ADMIN: Nuke sequence initiated...");

        // Loop through every queue
        for (const q of queues) {
            // 1. Drain "Waiting" and "Delayed" (This is the built-in fast wipe)
            await q.drain(); 
            await q.drain(true);

            // 2. Forcefully remove "Active" (Zombie) jobs that are stuck running
            // We fetch ALL jobs in these states and delete them manually
            const zombieJobs = await q.getJobs(['active', 'wait', 'delayed', 'failed']);
            for (const job of zombieJobs) {
                await job.remove().catch(err => console.error(`Failed to remove job ${job.id}: ${err.message}`));
            }
            
            // 3. Clean history (Completed/Failed)
            await q.clean(0, 1000, 'failed');
            await q.clean(0, 1000, 'completed');
        }

        console.log("ADMIN: All queues have been NUKED. Zero jobs remain.");
        res.status(200).send("Queue PAUSED and ALL jobs (Active/Wait/Delayed/Failed) have been REMOVED.");

    } catch (e) {
        console.error("ADMIN: Error stopping all jobs:", e);
        res.status(500).send("Error stopping all jobs");
    }
});

app.get('/admin/flush-redis', async (req, res) => {
    try {
        console.log("ADMIN: Connecting to Redis for manual flush...");
        const connection = new Redis(process.env.REDIS_URL);
        
        // Send the FLUSHDB command directly
        await connection.flushdb();
        
        // Close this temporary connection
        await connection.quit();

        console.log("ADMIN: Redis FLUSHDB executed. All keys deleted.");
        res.status(200).send("REDIS FLUSHED. The database is empty. You may now Start Fresh.");
    } catch (e) {
        console.error("ADMIN: Error flushing Redis:", e);
        res.status(500).send("Error flushing Redis: " + e.message);
    }
});

// ... Your app.listen(...) ...


app.listen(port, async () => {
    console.log(`Server is running on http://localhost:${port}`);
    // scheduleDailyJob()
    //     .catch(err => console.error("Failed to schedule daily job:", err));  
})
```

## File: naruko_gmvmax.json
```
{
  "code": 0,
  "message": "OK",
  "request_id": "20251114155938363D0A64394AF648D1D9",
  "data": {
    "list": [
      {
        "dimensions": {
          "campaign_id": "1845471573444610",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1832717944552466",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1831256551835745",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1845471573444610",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "2529",
          "spend": "2562"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1840857928059986",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1832717944552466",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "698140",
          "spend": "738964"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1848007708145793",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1835776428640354",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1847473520538642",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1845956224839810",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1847474152825953",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "1147",
          "spend": "1147"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1845956224839810",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "423048",
          "spend": "423048"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1835776428640354",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1846143399992418",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "690",
          "spend": "709"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1847473520538642",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "376610",
          "spend": "376610"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1831256551835745",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "1130342",
          "spend": "1222401"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1840857928059986",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "283670",
          "spend": "283670"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1845471573444610",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "144",
          "spend": "144"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1840857928059986",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1835776428640354",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "1224529",
          "spend": "1224529"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1840857928059986",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "274488",
          "spend": "296516"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1832717944552466",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1831256551835745",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1835776428640354",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "MY"
        },
        "metrics": {
          "billed_cost": "1",
          "spend": "1"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1834778192991490",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1834778192991490",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "4943",
          "spend": "4980"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1847473520538642",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1832717944552466",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "409906",
          "spend": "409906"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1847474152825953",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "3074",
          "spend": "3247"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1847473520538642",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "186284",
          "spend": "193818"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1834778192991490",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1834778192991490",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "45263",
          "spend": "45263"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1845956224839810",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "328710",
          "spend": "335592"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1845956224839810",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "None"
        },
        "metrics": {
          "billed_cost": "0",
          "spend": "0"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1831256551835745",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "1021656",
          "spend": "1021656"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1835776428640354",
          "stat_time_day": "2025-11-12 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "909723",
          "spend": "911885"
        }
      },
      {
        "dimensions": {
          "campaign_id": "1846143399992418",
          "stat_time_day": "2025-11-13 00:00:00",
          "country_code": "ID"
        },
        "metrics": {
          "billed_cost": "169",
          "spend": "169"
        }
      }
    ],
    "page_info": {
      "total_page": 1,
      "total_number": 37,
      "page": 1,
      "page_size": 37
    }
  }
}
```

## File: order-detail.json
```
{
  "image": [],
  "buyer_videos": [],
  "reason": "NOT_RECEIPT",
  "text_reason": "Paket di order udh lama ga smpai2",
  "return_sn": "2510010VK2V09YA",
  "refund_amount": 275200,
  "currency": "IDR",
  "create_time": 1759283371,
  "update_time": 1759419203,
  "status": "ACCEPTED",
  "due_date": 1759542570,
  "tracking_number": "",
  "needs_logistics": false,
  "amount_before_discount": 348000,
  "user": {
    "username": "reginarenden",
    "email": "*********na@yahoo.com",
    "portrait": "http://mms.img.susercontent.com/642dcc009528544c39da9094cce17424"
  },
  "item": [
    {
      "item_id": 460504215,
      "model_id": 290663617998,
      "name": "EILEEN GRACE - Moisturize Rose Jelly Mask 300 ml | Masker Wajah | Jerawat | Bruntus | Bopeng | Bekas Jerawat | Kemerahan | Skin Barrier | Mencerahkan | Melembapkan",
      "images": [
        "http://mms.img.susercontent.com/id-11134207-7ra0m-mbxsac3qg53a15",
        "http://mms.img.susercontent.com/id-11134207-7rbk4-m7ucamheohhs59",
        "http://mms.img.susercontent.com/id-11134207-7ra0n-mcg3l7ne6pvfb0",
        "http://mms.img.susercontent.com/id-11134207-7ra0r-mcg3l7ne84fv88",
        "http://mms.img.susercontent.com/id-11134207-7ra0q-mcg3l7ne5baze5",
        "http://mms.img.susercontent.com/id-11134207-7ra0p-mb569uw0vflg30",
        "http://mms.img.susercontent.com/id-11134207-7rbkc-mb2ea7svt0tna4",
        "http://mms.img.susercontent.com/id-11134207-7rbkb-m7ucamhe91kna2"
      ],
      "amount": 1,
      "item_price": 344000,
      "is_add_on_deal": false,
      "is_main_item": false,
      "item_sku": "",
      "variation_sku": "EIGR0007",
      "add_on_deal_id": 0,
      "refund_amount": 275200,
      "hot_listing_item": false
    }
  ],
  "order_sn": "2509105J8RJMW7",
  "return_ship_due_date": 0,
  "return_seller_due_date": 0,
  "negotiation_status": "",
  "seller_proof_status": "NOT_NEEDED",
  "seller_compensation_status": "",
  "hot_listing_order": false,
  "return_refund_type": "RRBOC",
  "return_solution": 1,
  "seller_evidence_deadline": null,
  "negotiation": {
    "latest_solution": ""
  },
  "return_refund_request_type": 0,
  "validation_type": "seller_validation",
  "is_seller_arrange": false,
  "is_shipping_proof_mandatory": false
}
```

## File: package-lock.json
```
{
  "name": "api-shopee",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "api-shopee",
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "@google-cloud/bigquery": "^8.1.1",
        "@google-cloud/secret-manager": "^6.1.1",
        "axios": "^1.12.2",
        "bottleneck": "^2.19.5",
        "bullmq": "^5.58.9",
        "dotenv": "^17.2.2",
        "express": "^5.1.0",
        "ioredis": "^5.8.2"
      }
    },
    "node_modules/@google-cloud/bigquery": {
      "version": "8.1.1",
      "resolved": "https://registry.npmjs.org/@google-cloud/bigquery/-/bigquery-8.1.1.tgz",
      "integrity": "sha512-2GHlohfA/VJffTvibMazMsZi6jPRx8MmaMberyDTL8rnhVs/frKSXVVRtLU83uSAy2j/5SD4mOs4jMQgJPON2g==",
      "license": "Apache-2.0",
      "dependencies": {
        "@google-cloud/common": "^6.0.0",
        "@google-cloud/paginator": "^6.0.0",
        "@google-cloud/precise-date": "^5.0.0",
        "@google-cloud/promisify": "^5.0.0",
        "arrify": "^3.0.0",
        "big.js": "^6.2.2",
        "duplexify": "^4.1.3",
        "extend": "^3.0.2",
        "stream-events": "^1.0.5",
        "teeny-request": "^10.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google-cloud/common": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/common/-/common-6.0.0.tgz",
      "integrity": "sha512-IXh04DlkLMxWgYLIUYuHHKXKOUwPDzDgke1ykkkJPe48cGIS9kkL2U/o0pm4ankHLlvzLF/ma1eO86n/bkumIA==",
      "license": "Apache-2.0",
      "dependencies": {
        "@google-cloud/projectify": "^4.0.0",
        "@google-cloud/promisify": "^4.0.0",
        "arrify": "^2.0.0",
        "duplexify": "^4.1.3",
        "extend": "^3.0.2",
        "google-auth-library": "^10.0.0-rc.1",
        "html-entities": "^2.5.2",
        "retry-request": "^8.0.0",
        "teeny-request": "^10.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google-cloud/common/node_modules/@google-cloud/promisify": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/promisify/-/promisify-4.1.0.tgz",
      "integrity": "sha512-G/FQx5cE/+DqBbOpA5jKsegGwdPniU6PuIEMt+qxWgFxvxuFOzVmp6zYchtYuwAWV5/8Dgs0yAmjvNZv3uXLQg==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google-cloud/common/node_modules/arrify": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/arrify/-/arrify-2.0.1.tgz",
      "integrity": "sha512-3duEwti880xqi4eAMN8AyR4a0ByT90zoYdLlevfrvU43vb0YZwZVfxOgxWrLXXXpyugL0hNZc9G6BiB5B3nUug==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/@google-cloud/paginator": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/paginator/-/paginator-6.0.0.tgz",
      "integrity": "sha512-g5nmMnzC+94kBxOKkLGpK1ikvolTFCC3s2qtE4F+1EuArcJ7HHC23RDQVt3Ra3CqpUYZ+oXNKZ8n5Cn5yug8DA==",
      "license": "Apache-2.0",
      "dependencies": {
        "extend": "^3.0.2"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google-cloud/precise-date": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/precise-date/-/precise-date-5.0.0.tgz",
      "integrity": "sha512-9h0Gvw92EvPdE8AK8AgZPbMnH5ftDyPtKm7/KUfcJVaPEPjwGDsJd1QV0H8esBDV4II41R/2lDWH1epBqIoKUw==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google-cloud/projectify": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/projectify/-/projectify-4.0.0.tgz",
      "integrity": "sha512-MmaX6HeSvyPbWGwFq7mXdo0uQZLGBYCwziiLIGq5JVX+/bdI3SAq6bP98trV5eTWfLuvsMcIC1YJOF2vfteLFA==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@google-cloud/promisify": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/promisify/-/promisify-5.0.0.tgz",
      "integrity": "sha512-N8qS6dlORGHwk7WjGXKOSsLjIjNINCPicsOX6gyyLiYk7mq3MtII96NZ9N2ahwA2vnkLmZODOIH9rlNniYWvCQ==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google-cloud/secret-manager": {
      "version": "6.1.1",
      "resolved": "https://registry.npmjs.org/@google-cloud/secret-manager/-/secret-manager-6.1.1.tgz",
      "integrity": "sha512-dwSuxJ9RNmAW46FjK1StiNIeOiSHHQs/XIy4VArJ6bBMR+WsIvR+zhPh2pa40aFa9uTty67j38Rl268TVV62EA==",
      "license": "Apache-2.0",
      "dependencies": {
        "google-gax": "^5.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@grpc/grpc-js": {
      "version": "1.14.0",
      "resolved": "https://registry.npmjs.org/@grpc/grpc-js/-/grpc-js-1.14.0.tgz",
      "integrity": "sha512-N8Jx6PaYzcTRNzirReJCtADVoq4z7+1KQ4E70jTg/koQiMoUSN1kbNjPOqpPbhMFhfU1/l7ixspPl8dNY+FoUg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@grpc/proto-loader": "^0.8.0",
        "@js-sdsl/ordered-map": "^4.4.2"
      },
      "engines": {
        "node": ">=12.10.0"
      }
    },
    "node_modules/@grpc/proto-loader": {
      "version": "0.8.0",
      "resolved": "https://registry.npmjs.org/@grpc/proto-loader/-/proto-loader-0.8.0.tgz",
      "integrity": "sha512-rc1hOQtjIWGxcxpb9aHAfLpIctjEnsDehj0DAiVfBlmT84uvR0uUtN2hEi/ecvWVjXUGf5qPF4qEgiLOx1YIMQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "lodash.camelcase": "^4.3.0",
        "long": "^5.0.0",
        "protobufjs": "^7.5.3",
        "yargs": "^17.7.2"
      },
      "bin": {
        "proto-loader-gen-types": "build/bin/proto-loader-gen-types.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/@ioredis/commands": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/@ioredis/commands/-/commands-1.4.0.tgz",
      "integrity": "sha512-aFT2yemJJo+TZCmieA7qnYGQooOS7QfNmYrzGtsYd3g9j5iDP8AimYYAesf79ohjbLG12XxC4nG5DyEnC88AsQ==",
      "license": "MIT"
    },
    "node_modules/@js-sdsl/ordered-map": {
      "version": "4.4.2",
      "resolved": "https://registry.npmjs.org/@js-sdsl/ordered-map/-/ordered-map-4.4.2.tgz",
      "integrity": "sha512-iUKgm52T8HOE/makSxjqoWhe95ZJA1/G1sYsGev2JDKUSS14KAgg1LHb+Ba+IPow0xflbnSkOsZcO08C7w1gYw==",
      "license": "MIT",
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/js-sdsl"
      }
    },
    "node_modules/@msgpackr-extract/msgpackr-extract-darwin-arm64": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/@msgpackr-extract/msgpackr-extract-darwin-arm64/-/msgpackr-extract-darwin-arm64-3.0.3.tgz",
      "integrity": "sha512-QZHtlVgbAdy2zAqNA9Gu1UpIuI8Xvsd1v8ic6B2pZmeFnFcMWiPLfWXh7TVw4eGEZ/C9TH281KwhVoeQUKbyjw==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@msgpackr-extract/msgpackr-extract-darwin-x64": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/@msgpackr-extract/msgpackr-extract-darwin-x64/-/msgpackr-extract-darwin-x64-3.0.3.tgz",
      "integrity": "sha512-mdzd3AVzYKuUmiWOQ8GNhl64/IoFGol569zNRdkLReh6LRLHOXxU4U8eq0JwaD8iFHdVGqSy4IjFL4reoWCDFw==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@msgpackr-extract/msgpackr-extract-linux-arm": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/@msgpackr-extract/msgpackr-extract-linux-arm/-/msgpackr-extract-linux-arm-3.0.3.tgz",
      "integrity": "sha512-fg0uy/dG/nZEXfYilKoRe7yALaNmHoYeIoJuJ7KJ+YyU2bvY8vPv27f7UKhGRpY6euFYqEVhxCFZgAUNQBM3nw==",
      "cpu": [
        "arm"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@msgpackr-extract/msgpackr-extract-linux-arm64": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/@msgpackr-extract/msgpackr-extract-linux-arm64/-/msgpackr-extract-linux-arm64-3.0.3.tgz",
      "integrity": "sha512-YxQL+ax0XqBJDZiKimS2XQaf+2wDGVa1enVRGzEvLLVFeqa5kx2bWbtcSXgsxjQB7nRqqIGFIcLteF/sHeVtQg==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@msgpackr-extract/msgpackr-extract-linux-x64": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/@msgpackr-extract/msgpackr-extract-linux-x64/-/msgpackr-extract-linux-x64-3.0.3.tgz",
      "integrity": "sha512-cvwNfbP07pKUfq1uH+S6KJ7dT9K8WOE4ZiAcsrSes+UY55E/0jLYc+vq+DO7jlmqRb5zAggExKm0H7O/CBaesg==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@msgpackr-extract/msgpackr-extract-win32-x64": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/@msgpackr-extract/msgpackr-extract-win32-x64/-/msgpackr-extract-win32-x64-3.0.3.tgz",
      "integrity": "sha512-x0fWaQtYp4E6sktbsdAqnehxDgEc/VwM7uLsRCYWaiGu0ykYdZPiS8zCWdnjHwyiumousxfBm4SO31eXqwEZhQ==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@protobufjs/aspromise": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/aspromise/-/aspromise-1.1.2.tgz",
      "integrity": "sha512-j+gKExEuLmKwvz3OgROXtrJ2UG2x8Ch2YZUxahh+s1F2HZ+wAceUNLkvy6zKCPVRkU++ZWQrdxsUeQXmcg4uoQ==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/base64": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/base64/-/base64-1.1.2.tgz",
      "integrity": "sha512-AZkcAA5vnN/v4PDqKyMR5lx7hZttPDgClv83E//FMNhR2TMcLUhfRUBHCmSl0oi9zMgDDqRUJkSxO3wm85+XLg==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/codegen": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/@protobufjs/codegen/-/codegen-2.0.4.tgz",
      "integrity": "sha512-YyFaikqM5sH0ziFZCN3xDC7zeGaB/d0IUb9CATugHWbd1FRFwWwt4ld4OYMPWu5a3Xe01mGAULCdqhMlPl29Jg==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/eventemitter": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/eventemitter/-/eventemitter-1.1.0.tgz",
      "integrity": "sha512-j9ednRT81vYJ9OfVuXG6ERSTdEL1xVsNgqpkxMsbIabzSo3goCjDIveeGv5d03om39ML71RdmrGNjG5SReBP/Q==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/fetch": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/fetch/-/fetch-1.1.0.tgz",
      "integrity": "sha512-lljVXpqXebpsijW71PZaCYeIcE5on1w5DlQy5WH6GLbFryLUrBD4932W/E2BSpfRJWseIL4v/KPgBFxDOIdKpQ==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "@protobufjs/aspromise": "^1.1.1",
        "@protobufjs/inquire": "^1.1.0"
      }
    },
    "node_modules/@protobufjs/float": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/float/-/float-1.0.2.tgz",
      "integrity": "sha512-Ddb+kVXlXst9d+R9PfTIxh1EdNkgoRe5tOX6t01f1lYWOvJnSPDBlG241QLzcyPdoNTsblLUdujGSE4RzrTZGQ==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/inquire": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/inquire/-/inquire-1.1.0.tgz",
      "integrity": "sha512-kdSefcPdruJiFMVSbn801t4vFK7KB/5gd2fYvrxhuJYg8ILrmn9SKSX2tZdV6V+ksulWqS7aXjBcRXl3wHoD9Q==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/path": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/path/-/path-1.1.2.tgz",
      "integrity": "sha512-6JOcJ5Tm08dOHAbdR3GrvP+yUUfkjG5ePsHYczMFLq3ZmMkAD98cDgcT2iA1lJ9NVwFd4tH/iSSoe44YWkltEA==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/pool": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/pool/-/pool-1.1.0.tgz",
      "integrity": "sha512-0kELaGSIDBKvcgS4zkjz1PeddatrjYcmMWOlAuAPwAeccUrPHdUqo/J6LiymHHEiJT5NrF1UVwxY14f+fy4WQw==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/utf8": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/utf8/-/utf8-1.1.0.tgz",
      "integrity": "sha512-Vvn3zZrhQZkkBE8LSuW3em98c0FwgO4nxzv6OdSxPKJIEKY2bGbHn+mhGIPerzI4twdxaP8/0+06HBpwf345Lw==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@tootallnate/once": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/@tootallnate/once/-/once-2.0.0.tgz",
      "integrity": "sha512-XCuKFP5PS55gnMVu3dty8KPatLqUoy/ZYzDzAGCQ8JNFCkLXzmI7vNHCR+XpbZaMWQK/vQubr7PkYq8g470J/A==",
      "license": "MIT",
      "engines": {
        "node": ">= 10"
      }
    },
    "node_modules/@types/node": {
      "version": "24.7.2",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-24.7.2.tgz",
      "integrity": "sha512-/NbVmcGTP+lj5oa4yiYxxeBjRivKQ5Ns1eSZeB99ExsEQ6rX5XYU1Zy/gGxY/ilqtD4Etx9mKyrPxZRetiahhA==",
      "license": "MIT",
      "dependencies": {
        "undici-types": "~7.14.0"
      }
    },
    "node_modules/accepts": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-2.0.0.tgz",
      "integrity": "sha512-5cvg6CtKwfgdmVqY1WIiXKc3Q1bkRqGLi+2W/6ao+6Y7gu/RCwRuAhGEzh5B4KlszSuTLgZYuqFqo5bImjNKng==",
      "license": "MIT",
      "dependencies": {
        "mime-types": "^3.0.0",
        "negotiator": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/agent-base": {
      "version": "7.1.4",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-7.1.4.tgz",
      "integrity": "sha512-MnA+YT8fwfJPgBx3m60MNqakm30XOkyIoH1y6huTQvC0PwZG7ki8NacLBcrPbNoo8vEZy7Jpuk7+jMO+CUovTQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 14"
      }
    },
    "node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "license": "MIT",
      "dependencies": {
        "color-convert": "^2.0.1"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/arrify": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/arrify/-/arrify-3.0.0.tgz",
      "integrity": "sha512-tLkvA81vQG/XqE2mjDkGQHoOINtMHtysSnemrmoGe6PydDPMRbVugqyk4A6V/WDWEfm3l+0d8anA9r8cv/5Jaw==",
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==",
      "license": "MIT"
    },
    "node_modules/axios": {
      "version": "1.12.2",
      "resolved": "https://registry.npmjs.org/axios/-/axios-1.12.2.tgz",
      "integrity": "sha512-vMJzPewAlRyOgxV2dU0Cuz2O8zzzx9VYtbJOaBgXFeLc4IV/Eg50n4LowmehOOR61S8ZMpc2K5Sa7g6A4jfkUw==",
      "license": "MIT",
      "dependencies": {
        "follow-redirects": "^1.15.6",
        "form-data": "^4.0.4",
        "proxy-from-env": "^1.1.0"
      }
    },
    "node_modules/base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/big.js": {
      "version": "6.2.2",
      "resolved": "https://registry.npmjs.org/big.js/-/big.js-6.2.2.tgz",
      "integrity": "sha512-y/ie+Faknx7sZA5MfGA2xKlu0GDv8RWrXGsmlteyJQ2lvoKv9GBK/fpRMc2qlSoBAgNxrixICFCBefIq8WCQpQ==",
      "license": "MIT",
      "engines": {
        "node": "*"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/bigjs"
      }
    },
    "node_modules/bignumber.js": {
      "version": "9.3.1",
      "resolved": "https://registry.npmjs.org/bignumber.js/-/bignumber.js-9.3.1.tgz",
      "integrity": "sha512-Ko0uX15oIUS7wJ3Rb30Fs6SkVbLmPBAKdlm7q9+ak9bbIeFf0MwuBsQV6z7+X768/cHsfg+WlysDWJcmthjsjQ==",
      "license": "MIT",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/body-parser": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-2.2.0.tgz",
      "integrity": "sha512-02qvAaxv8tp7fBa/mw1ga98OGm+eCbqzJOKoRt70sLmfEEi+jyBYVTDGfCL/k06/4EMk/z01gCe7HoCH/f2LTg==",
      "license": "MIT",
      "dependencies": {
        "bytes": "^3.1.2",
        "content-type": "^1.0.5",
        "debug": "^4.4.0",
        "http-errors": "^2.0.0",
        "iconv-lite": "^0.6.3",
        "on-finished": "^2.4.1",
        "qs": "^6.14.0",
        "raw-body": "^3.0.0",
        "type-is": "^2.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/bottleneck": {
      "version": "2.19.5",
      "resolved": "https://registry.npmjs.org/bottleneck/-/bottleneck-2.19.5.tgz",
      "integrity": "sha512-VHiNCbI1lKdl44tGrhNfU3lup0Tj/ZBMJB5/2ZbNXRCPuRCO7ed2mgcK4r17y+KB2EfuYuRaVlwNbAeaWGSpbw==",
      "license": "MIT"
    },
    "node_modules/buffer-equal-constant-time": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/buffer-equal-constant-time/-/buffer-equal-constant-time-1.0.1.tgz",
      "integrity": "sha512-zRpUiDwd/xk6ADqPMATG8vc9VPrkck7T07OIx0gnjmJAnHnTVXNQG3vfvWNuiZIkwu9KrKdA1iJKfsfTVxE6NA==",
      "license": "BSD-3-Clause"
    },
    "node_modules/bullmq": {
      "version": "5.58.9",
      "resolved": "https://registry.npmjs.org/bullmq/-/bullmq-5.58.9.tgz",
      "integrity": "sha512-z29F6c/Nznl6wmQ/w+T0HIwCdDIY5C8pgyrjGxCgVzhm79IT10+yt3SrW2HFc2WUIYlh3TVtdu2d/kvaw/Awug==",
      "license": "MIT",
      "dependencies": {
        "cron-parser": "^4.9.0",
        "ioredis": "^5.4.1",
        "msgpackr": "^1.11.2",
        "node-abort-controller": "^3.1.1",
        "semver": "^7.5.4",
        "tslib": "^2.0.0",
        "uuid": "^11.1.0"
      }
    },
    "node_modules/bytes": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
      "integrity": "sha512-/Nf7TyzTx6S3yRJObOAV7956r8cr2+Oj8AC5dt8wSP3BQAoeX58NoHyCU8P8zGkNXStjTSi6fzO6F0pBdcYbEg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/call-bound": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
      "integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "get-intrinsic": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/cliui": {
      "version": "8.0.1",
      "resolved": "https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz",
      "integrity": "sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ==",
      "license": "ISC",
      "dependencies": {
        "string-width": "^4.2.0",
        "strip-ansi": "^6.0.1",
        "wrap-ansi": "^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/cluster-key-slot": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/cluster-key-slot/-/cluster-key-slot-1.1.2.tgz",
      "integrity": "sha512-RMr0FhtfXemyinomL4hrWcYJxmX6deFdCxpJzhDttxgO1+bcCnkk+9drydLVDmAMG7NE6aN/fl4F7ucU/90gAA==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "license": "MIT",
      "dependencies": {
        "color-name": "~1.1.4"
      },
      "engines": {
        "node": ">=7.0.0"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
      "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
      "license": "MIT"
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "license": "MIT",
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/content-disposition": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-1.0.0.tgz",
      "integrity": "sha512-Au9nRL8VNUut/XSzbQA38+M78dzP4D+eqg3gfJHMIHHYa3bg067xj1KxMUWj+VULbiZMowKngFFbKczUrNJ1mg==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "5.2.1"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/content-type": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
      "integrity": "sha512-nTjqfcBFEipKdXCv4YDQWCfmcLZKm81ldF0pAopTvyrFGVbcR6P/VAAd5G7N+0tTr8QqiU0tFadD6FK4NtJwOA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.7.2.tgz",
      "integrity": "sha512-yki5XnKuf750l50uGTllt6kKILY4nQ1eNIQatoXEByZ5dWgnKqbnqmTrBE5B4N7lrMJKQ2ytWMiTO2o0v6Ew/w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie-signature": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.2.2.tgz",
      "integrity": "sha512-D76uU73ulSXrD1UXF4KE2TMxVVwhsnCgfAyTg9k8P6KGZjlXKrOLe4dJQKI3Bxi5wjesZoFXJWElNWBjPZMbhg==",
      "license": "MIT",
      "engines": {
        "node": ">=6.6.0"
      }
    },
    "node_modules/cron-parser": {
      "version": "4.9.0",
      "resolved": "https://registry.npmjs.org/cron-parser/-/cron-parser-4.9.0.tgz",
      "integrity": "sha512-p0SaNjrHOnQeR8/VnfGbmg9te2kfyYSQ7Sc/j/6DtPL3JQvKxmjO9TSjNFpujqV3vEYYBvNNvXSxzyksBWAx1Q==",
      "license": "MIT",
      "dependencies": {
        "luxon": "^3.2.1"
      },
      "engines": {
        "node": ">=12.0.0"
      }
    },
    "node_modules/data-uri-to-buffer": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/data-uri-to-buffer/-/data-uri-to-buffer-4.0.1.tgz",
      "integrity": "sha512-0R9ikRb668HB7QDxT1vkpuUBtqc53YyAwMwGeUFKRojY/NWKvdZ+9UYtRfGmhqNbRkTSVpMbmyhXipFFv2cb/A==",
      "license": "MIT",
      "engines": {
        "node": ">= 12"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/denque": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/denque/-/denque-2.1.0.tgz",
      "integrity": "sha512-HVQE3AAb/pxF8fQAoiqpvg9i3evqug3hoiwakOyZAwJm+6vZehbkYXZ0l4JxS+I3QxM97v5aaRNhj8v5oBhekw==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=0.10"
      }
    },
    "node_modules/depd": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
      "integrity": "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/detect-libc": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.1.tgz",
      "integrity": "sha512-ecqj/sy1jcK1uWrwpR67UhYrIFQ+5WlGxth34WquCbamhFA6hkkwiu37o6J5xCHdo1oixJRfVRw+ywV+Hq/0Aw==",
      "license": "Apache-2.0",
      "optional": true,
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/dotenv": {
      "version": "17.2.2",
      "resolved": "https://registry.npmjs.org/dotenv/-/dotenv-17.2.2.tgz",
      "integrity": "sha512-Sf2LSQP+bOlhKWWyhFsn0UsfdK/kCWRv1iuA2gXAwt3dyNabr6QSj00I2V10pidqz69soatm9ZwZvpQMTIOd5Q==",
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://dotenvx.com"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/duplexify": {
      "version": "4.1.3",
      "resolved": "https://registry.npmjs.org/duplexify/-/duplexify-4.1.3.tgz",
      "integrity": "sha512-M3BmBhwJRZsSx38lZyhE53Csddgzl5R7xGJNk7CVddZD6CcmwMCH8J+7AprIrQKH7TonKxaCjcv27Qmf+sQ+oA==",
      "license": "MIT",
      "dependencies": {
        "end-of-stream": "^1.4.1",
        "inherits": "^2.0.3",
        "readable-stream": "^3.1.1",
        "stream-shift": "^1.0.2"
      }
    },
    "node_modules/ecdsa-sig-formatter": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/ecdsa-sig-formatter/-/ecdsa-sig-formatter-1.0.11.tgz",
      "integrity": "sha512-nagl3RYrbNv6kQkeJIpt6NJZy8twLB/2vtz6yN9Z4vRKHN4/QZJIEbqohALSgwKdnksuY3k5Addp5lg8sVoVcQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow==",
      "license": "MIT"
    },
    "node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "license": "MIT"
    },
    "node_modules/encodeurl": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz",
      "integrity": "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/end-of-stream": {
      "version": "1.4.5",
      "resolved": "https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.5.tgz",
      "integrity": "sha512-ooEGc6HP26xXq/N+GCGOT0JKCLDGrq2bQUZrQ7gyrJiZANJ/8YDTxTpQBXGMn+WbIQXNVpyWymm7KYVICQnyOg==",
      "license": "MIT",
      "dependencies": {
        "once": "^1.4.0"
      }
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz",
      "integrity": "sha512-FGgH2h8zKNim9ljj7dankFPcICIK9Cp5bm+c2gQSYePhpaG5+esrLODihIorn+Pe6FGJzWhXQotPv73jTaldXA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-set-tostringtag": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz",
      "integrity": "sha512-j6vWzfrGVfyXxge+O0x5sh6cvxAog0a/4Rdd2K36zCMV5eJ+/+tOAngRO8cODMNWbVRdVlmGZQL2YS3yR8bIUA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha512-NiSupZ4OeuGwr68lGIeym/ksIZMJodUGOSCZ/FSnTxcrekbvqrgdUxlJOMpijaKZVjAJrWrGs/6Jy8OMuyj9ow==",
      "license": "MIT"
    },
    "node_modules/etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha512-aIL5Fx7mawVa300al2BnEE4iNvo1qETxLrPI/o05L7z6go7fCw1J6EQmbK4FmJ2AS7kgVF/KEZWufBfdClMcPg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/express": {
      "version": "5.1.0",
      "resolved": "https://registry.npmjs.org/express/-/express-5.1.0.tgz",
      "integrity": "sha512-DT9ck5YIRU+8GYzzU5kT3eHGA5iL+1Zd0EutOmTE9Dtk+Tvuzd23VBU+ec7HPNSTxXYO55gPV/hq4pSBJDjFpA==",
      "license": "MIT",
      "dependencies": {
        "accepts": "^2.0.0",
        "body-parser": "^2.2.0",
        "content-disposition": "^1.0.0",
        "content-type": "^1.0.5",
        "cookie": "^0.7.1",
        "cookie-signature": "^1.2.1",
        "debug": "^4.4.0",
        "encodeurl": "^2.0.0",
        "escape-html": "^1.0.3",
        "etag": "^1.8.1",
        "finalhandler": "^2.1.0",
        "fresh": "^2.0.0",
        "http-errors": "^2.0.0",
        "merge-descriptors": "^2.0.0",
        "mime-types": "^3.0.0",
        "on-finished": "^2.4.1",
        "once": "^1.4.0",
        "parseurl": "^1.3.3",
        "proxy-addr": "^2.0.7",
        "qs": "^6.14.0",
        "range-parser": "^1.2.1",
        "router": "^2.2.0",
        "send": "^1.1.0",
        "serve-static": "^2.2.0",
        "statuses": "^2.0.1",
        "type-is": "^2.0.1",
        "vary": "^1.1.2"
      },
      "engines": {
        "node": ">= 18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/extend": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
      "integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==",
      "license": "MIT"
    },
    "node_modules/fetch-blob": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/fetch-blob/-/fetch-blob-3.2.0.tgz",
      "integrity": "sha512-7yAQpD2UMJzLi1Dqv7qFYnPbaPx7ZfFK6PiIxQ4PfkGPyNyl2Ugx+a/umUonmKqjhM4DnfbMvdX6otXq83soQQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/jimmywarting"
        },
        {
          "type": "paypal",
          "url": "https://paypal.me/jimmywarting"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "node-domexception": "^1.0.0",
        "web-streams-polyfill": "^3.0.3"
      },
      "engines": {
        "node": "^12.20 || >= 14.13"
      }
    },
    "node_modules/finalhandler": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-2.1.0.tgz",
      "integrity": "sha512-/t88Ty3d5JWQbWYgaOGCCYfXRwV1+be02WqYYlL6h0lEiUAMPM8o8qKGO01YIkOHzka2up08wvgYD0mDiI+q3Q==",
      "license": "MIT",
      "dependencies": {
        "debug": "^4.4.0",
        "encodeurl": "^2.0.0",
        "escape-html": "^1.0.3",
        "on-finished": "^2.4.1",
        "parseurl": "^1.3.3",
        "statuses": "^2.0.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/follow-redirects": {
      "version": "1.15.11",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.15.11.tgz",
      "integrity": "sha512-deG2P0JfjrTxl50XGCDyfI97ZGVCxIpfKYmfyrQ54n5FO/0gfIES8C/Psl6kWVDolizcaaxZJnTS0QSMxvnsBQ==",
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/RubenVerborgh"
        }
      ],
      "license": "MIT",
      "engines": {
        "node": ">=4.0"
      },
      "peerDependenciesMeta": {
        "debug": {
          "optional": true
        }
      }
    },
    "node_modules/form-data": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-4.0.4.tgz",
      "integrity": "sha512-KrGhL9Q4zjj0kiUt5OO4Mr/A/jlI2jDYs5eHBpYHPcBEVSiipAvn2Ko2HnPe20rmcuuvMHNdZFp+4IlGTMF0Ow==",
      "license": "MIT",
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.8",
        "es-set-tostringtag": "^2.1.0",
        "hasown": "^2.0.2",
        "mime-types": "^2.1.12"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/form-data/node_modules/mime-db": {
      "version": "1.52.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
      "integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/form-data/node_modules/mime-types": {
      "version": "2.1.35",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
      "integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
      "license": "MIT",
      "dependencies": {
        "mime-db": "1.52.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/formdata-polyfill": {
      "version": "4.0.10",
      "resolved": "https://registry.npmjs.org/formdata-polyfill/-/formdata-polyfill-4.0.10.tgz",
      "integrity": "sha512-buewHzMvYL29jdeQTVILecSaZKnt/RJWjoZCF5OW60Z67/GmSLBkOFM7qh1PI3zFNtJbaZL5eQu1vLfazOwj4g==",
      "license": "MIT",
      "dependencies": {
        "fetch-blob": "^3.1.2"
      },
      "engines": {
        "node": ">=12.20.0"
      }
    },
    "node_modules/forwarded": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.2.0.tgz",
      "integrity": "sha512-buRG0fpBtRHSTCOASe6hD258tEubFoRLb4ZNA6NxMVHNw2gOcwHo9wyablzMzOA5z9xA9L1KNjk/Nt6MT9aYow==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/fresh": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-2.0.0.tgz",
      "integrity": "sha512-Rx/WycZ60HOaqLKAi6cHRKKI7zxWbJ31MhntmtwMoaTeF7XFH9hhBp8vITaMidfljRQ6eYWCKkaTK+ykVJHP2A==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/gaxios": {
      "version": "7.1.2",
      "resolved": "https://registry.npmjs.org/gaxios/-/gaxios-7.1.2.tgz",
      "integrity": "sha512-/Szrn8nr+2TsQT1Gp8iIe/BEytJmbyfrbFh419DfGQSkEgNEhbPi7JRJuughjkTzPWgU9gBQf5AVu3DbHt0OXA==",
      "license": "Apache-2.0",
      "dependencies": {
        "extend": "^3.0.2",
        "https-proxy-agent": "^7.0.1",
        "node-fetch": "^3.3.2"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/gcp-metadata": {
      "version": "7.0.1",
      "resolved": "https://registry.npmjs.org/gcp-metadata/-/gcp-metadata-7.0.1.tgz",
      "integrity": "sha512-UcO3kefx6dCcZkgcTGgVOTFb7b1LlQ02hY1omMjjrrBzkajRMCFgYOjs7J71WqnuG1k2b+9ppGL7FsOfhZMQKQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "gaxios": "^7.0.0",
        "google-logging-utils": "^1.0.0",
        "json-bigint": "^1.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/get-caller-file": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz",
      "integrity": "sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==",
      "license": "ISC",
      "engines": {
        "node": "6.* || 8.* || >= 10.*"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/google-auth-library": {
      "version": "10.3.0",
      "resolved": "https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.3.0.tgz",
      "integrity": "sha512-ylSE3RlCRZfZB56PFJSfUCuiuPq83Fx8hqu1KPWGK8FVdSaxlp/qkeMMX/DT/18xkwXIHvXEXkZsljRwfrdEfQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "base64-js": "^1.3.0",
        "ecdsa-sig-formatter": "^1.0.11",
        "gaxios": "^7.0.0",
        "gcp-metadata": "^7.0.0",
        "google-logging-utils": "^1.0.0",
        "gtoken": "^8.0.0",
        "jws": "^4.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/google-gax": {
      "version": "5.0.4",
      "resolved": "https://registry.npmjs.org/google-gax/-/google-gax-5.0.4.tgz",
      "integrity": "sha512-HmQ6zIYBs2EikTk+kjeHmtHprNTEpsnVaKONw9cwZZwUNCkUb+D5RYrJpCxyjdvIDvJp3wLbVReolJLRZRms1g==",
      "license": "Apache-2.0",
      "dependencies": {
        "@grpc/grpc-js": "^1.12.6",
        "@grpc/proto-loader": "^0.8.0",
        "duplexify": "^4.1.3",
        "google-auth-library": "^10.1.0",
        "google-logging-utils": "^1.1.1",
        "node-fetch": "^3.3.2",
        "object-hash": "^3.0.0",
        "proto3-json-serializer": "^3.0.0",
        "protobufjs": "^7.5.3",
        "retry-request": "^8.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/google-logging-utils": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/google-logging-utils/-/google-logging-utils-1.1.1.tgz",
      "integrity": "sha512-rcX58I7nqpu4mbKztFeOAObbomBbHU2oIb/d3tJfF3dizGSApqtSwYJigGCooHdnMyQBIw8BrWyK96w3YXgr6A==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/gtoken": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/gtoken/-/gtoken-8.0.0.tgz",
      "integrity": "sha512-+CqsMbHPiSTdtSO14O51eMNlrp9N79gmeqmXeouJOhfucAedHw9noVe/n5uJk3tbKE6a+6ZCQg3RPhVhHByAIw==",
      "license": "MIT",
      "dependencies": {
        "gaxios": "^7.0.0",
        "jws": "^4.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-tostringtag": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
      "integrity": "sha512-NqADB8VjPFLM2V0VvHUewwwsw0ZWBaIdgo+ieHtK3hasLz4qeCRjYcqfB6AQrBggRKppKF8L52/VqdVsO47Dlw==",
      "license": "MIT",
      "dependencies": {
        "has-symbols": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz",
      "integrity": "sha512-0hJU9SCPvmMzIBdZFqNPXWa6dqh7WdH0cII9y+CyS8rG3nL48Bclra9HmKhVVUHyPWNH5Y7xDwAB7bfgSjkUMQ==",
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/html-entities": {
      "version": "2.6.0",
      "resolved": "https://registry.npmjs.org/html-entities/-/html-entities-2.6.0.tgz",
      "integrity": "sha512-kig+rMn/QOVRvr7c86gQ8lWXq+Hkv6CbAH1hLu+RG338StTpE8Z0b44SDVaqVu7HGKf27frdmUYEs9hTUX/cLQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/mdevils"
        },
        {
          "type": "patreon",
          "url": "https://patreon.com/mdevils"
        }
      ],
      "license": "MIT"
    },
    "node_modules/http-errors": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-2.0.0.tgz",
      "integrity": "sha512-FtwrG/euBzaEjYeRqOgly7G0qviiXoJWnvEH2Z1plBdXgbyjv34pHTSb9zoeHMyDy33+DWy5Wt9Wo+TURtOYSQ==",
      "license": "MIT",
      "dependencies": {
        "depd": "2.0.0",
        "inherits": "2.0.4",
        "setprototypeof": "1.2.0",
        "statuses": "2.0.1",
        "toidentifier": "1.0.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/http-errors/node_modules/statuses": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-2.0.1.tgz",
      "integrity": "sha512-RwNA9Z/7PrK06rYLIzFMlaF+l73iwpzsqRIFgbMLbTcLD6cOao82TaWefPXQvB2fOC4AjuYSEndS7N/mTCbkdQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/http-proxy-agent": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-5.0.0.tgz",
      "integrity": "sha512-n2hY8YdoRE1i7r6M0w9DIw5GgZN0G25P8zLCRQ8rjXtTU3vsNFBI/vWK/UIeE6g5MUUz6avwAPXmL6Fy9D/90w==",
      "license": "MIT",
      "dependencies": {
        "@tootallnate/once": "2",
        "agent-base": "6",
        "debug": "4"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/http-proxy-agent/node_modules/agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "license": "MIT",
      "dependencies": {
        "debug": "4"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/https-proxy-agent": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-7.0.6.tgz",
      "integrity": "sha512-vK9P5/iUfdl95AI+JVyUuIcVtd4ofvtrOr3HNtM2yxC9bnMbEdp3x01OhQNnjb8IJYi38VlTE3mBXwcfvywuSw==",
      "license": "MIT",
      "dependencies": {
        "agent-base": "^7.1.2",
        "debug": "4"
      },
      "engines": {
        "node": ">= 14"
      }
    },
    "node_modules/iconv-lite": {
      "version": "0.6.3",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.6.3.tgz",
      "integrity": "sha512-4fCk79wshMdzMp2rH06qWrJE4iolqLhCUH+OiuIgU++RB0+94NlDL81atO7GX55uUKueo0txHNtvEyI6D7WdMw==",
      "license": "MIT",
      "dependencies": {
        "safer-buffer": ">= 2.1.2 < 3.0.0"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "license": "ISC"
    },
    "node_modules/ioredis": {
      "version": "5.8.2",
      "resolved": "https://registry.npmjs.org/ioredis/-/ioredis-5.8.2.tgz",
      "integrity": "sha512-C6uC+kleiIMmjViJINWk80sOQw5lEzse1ZmvD+S/s8p8CWapftSaC+kocGTx6xrbrJ4WmYQGC08ffHLr6ToR6Q==",
      "license": "MIT",
      "dependencies": {
        "@ioredis/commands": "1.4.0",
        "cluster-key-slot": "^1.1.0",
        "debug": "^4.3.4",
        "denque": "^2.1.0",
        "lodash.defaults": "^4.2.0",
        "lodash.isarguments": "^3.1.0",
        "redis-errors": "^1.2.0",
        "redis-parser": "^3.0.0",
        "standard-as-callback": "^2.1.0"
      },
      "engines": {
        "node": ">=12.22.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/ioredis"
      }
    },
    "node_modules/ipaddr.js": {
      "version": "1.9.1",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz",
      "integrity": "sha512-0KI/607xoxSToH7GjN1FfSbLoU0+btTicjsQSWQlh/hZykN8KpmMf7uYwPW3R+akZ6R/w18ZlXSHBYXiYUPO3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/is-fullwidth-code-point": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
      "integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-promise": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/is-promise/-/is-promise-4.0.0.tgz",
      "integrity": "sha512-hvpoI6korhJMnej285dSg6nu1+e6uxs7zG3BYAm5byqDsgJNWwxzM6z6iZiAgQR4TJ30JmBTOwqZUw3WlyH3AQ==",
      "license": "MIT"
    },
    "node_modules/json-bigint": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/json-bigint/-/json-bigint-1.0.0.tgz",
      "integrity": "sha512-SiPv/8VpZuWbvLSMtTDU8hEfrZWg/mH/nV/b4o0CYbSxu1UIQPLdwKOCIyLQX+VIPO5vrLX3i8qtqFyhdPSUSQ==",
      "license": "MIT",
      "dependencies": {
        "bignumber.js": "^9.0.0"
      }
    },
    "node_modules/jwa": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/jwa/-/jwa-2.0.1.tgz",
      "integrity": "sha512-hRF04fqJIP8Abbkq5NKGN0Bbr3JxlQ+qhZufXVr0DvujKy93ZCbXZMHDL4EOtodSbCWxOqR8MS1tXA5hwqCXDg==",
      "license": "MIT",
      "dependencies": {
        "buffer-equal-constant-time": "^1.0.1",
        "ecdsa-sig-formatter": "1.0.11",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/jws": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/jws/-/jws-4.0.0.tgz",
      "integrity": "sha512-KDncfTmOZoOMTFG4mBlG0qUIOlc03fmzH+ru6RgYVZhPkyiy/92Owlt/8UEN+a4TXR1FQetfIpJE8ApdvdVxTg==",
      "license": "MIT",
      "dependencies": {
        "jwa": "^2.0.0",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/lodash.camelcase": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-4.3.0.tgz",
      "integrity": "sha512-TwuEnCnxbc3rAvhf/LbG7tJUDzhqXyFnv3dtzLOPgCG/hODL7WFnsbwktkD7yUV0RrreP/l1PALq/YSg6VvjlA==",
      "license": "MIT"
    },
    "node_modules/lodash.defaults": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/lodash.defaults/-/lodash.defaults-4.2.0.tgz",
      "integrity": "sha512-qjxPLHd3r5DnsdGacqOMU6pb/avJzdh9tFX2ymgoZE27BmjXrNy/y4LoaiTeAb+O3gL8AfpJGtqfX/ae2leYYQ==",
      "license": "MIT"
    },
    "node_modules/lodash.isarguments": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/lodash.isarguments/-/lodash.isarguments-3.1.0.tgz",
      "integrity": "sha512-chi4NHZlZqZD18a0imDHnZPrDeBbTtVN7GXMwuGdRH9qotxAjYs3aVLKc7zNOG9eddR5Ksd8rvFEBc9SsggPpg==",
      "license": "MIT"
    },
    "node_modules/long": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/long/-/long-5.3.2.tgz",
      "integrity": "sha512-mNAgZ1GmyNhD7AuqnTG3/VQ26o760+ZYBPKjPvugO8+nLbYfX6TVpJPseBvopbdY+qpZ/lKUnmEc1LeZYS3QAA==",
      "license": "Apache-2.0"
    },
    "node_modules/luxon": {
      "version": "3.7.2",
      "resolved": "https://registry.npmjs.org/luxon/-/luxon-3.7.2.tgz",
      "integrity": "sha512-vtEhXh/gNjI9Yg1u4jX/0YVPMvxzHuGgCm6tC5kZyb08yjGWGnqAjGJvcXbqQR2P3MyMEFnRbpcdFS6PBcLqew==",
      "license": "MIT",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/math-intrinsics": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
      "integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/media-typer": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-1.1.0.tgz",
      "integrity": "sha512-aisnrDP4GNe06UcKFnV5bfMNPBUw4jsLGaWwWfnH3v02GnBuXX2MCVn5RbrWo0j3pczUilYblq7fQ7Nw2t5XKw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/merge-descriptors": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-2.0.0.tgz",
      "integrity": "sha512-Snk314V5ayFLhp3fkUREub6WtjBfPdCPY1Ln8/8munuLuiYhsABgBVWsozAG+MWMbVEvcdcpbi9R7ww22l9Q3g==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/mime-db": {
      "version": "1.54.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.54.0.tgz",
      "integrity": "sha512-aU5EJuIN2WDemCcAp2vFBfp/m4EAhWJnUNSSw0ixs7/kXbd6Pg64EmwJkNdFhB8aWt1sH2CTXrLxo/iAGV3oPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime-types": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-3.0.1.tgz",
      "integrity": "sha512-xRc4oEhT6eaBpU1XF7AjpOFD+xQmXNB5OVKwp4tqCuBpHLS/ZbBDrc07mYTDqVMg6PfxUjjNp85O6Cd2Z/5HWA==",
      "license": "MIT",
      "dependencies": {
        "mime-db": "^1.54.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/msgpackr": {
      "version": "1.11.5",
      "resolved": "https://registry.npmjs.org/msgpackr/-/msgpackr-1.11.5.tgz",
      "integrity": "sha512-UjkUHN0yqp9RWKy0Lplhh+wlpdt9oQBYgULZOiFhV3VclSF1JnSQWZ5r9gORQlNYaUKQoR8itv7g7z1xDDuACA==",
      "license": "MIT",
      "optionalDependencies": {
        "msgpackr-extract": "^3.0.2"
      }
    },
    "node_modules/msgpackr-extract": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/msgpackr-extract/-/msgpackr-extract-3.0.3.tgz",
      "integrity": "sha512-P0efT1C9jIdVRefqjzOQ9Xml57zpOXnIuS+csaB4MdZbTdmGDLo8XhzBG1N7aO11gKDDkJvBLULeFTo46wwreA==",
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "node-gyp-build-optional-packages": "5.2.2"
      },
      "bin": {
        "download-msgpackr-prebuilds": "bin/download-prebuilds.js"
      },
      "optionalDependencies": {
        "@msgpackr-extract/msgpackr-extract-darwin-arm64": "3.0.3",
        "@msgpackr-extract/msgpackr-extract-darwin-x64": "3.0.3",
        "@msgpackr-extract/msgpackr-extract-linux-arm": "3.0.3",
        "@msgpackr-extract/msgpackr-extract-linux-arm64": "3.0.3",
        "@msgpackr-extract/msgpackr-extract-linux-x64": "3.0.3",
        "@msgpackr-extract/msgpackr-extract-win32-x64": "3.0.3"
      }
    },
    "node_modules/negotiator": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-1.0.0.tgz",
      "integrity": "sha512-8Ofs/AUQh8MaEcrlq5xOX0CQ9ypTF5dl78mjlMNfOK08fzpgTHQRQPBxcPlEtIw0yRpws+Zo/3r+5WRby7u3Gg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/node-abort-controller": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/node-abort-controller/-/node-abort-controller-3.1.1.tgz",
      "integrity": "sha512-AGK2yQKIjRuqnc6VkX2Xj5d+QW8xZ87pa1UK6yA6ouUyuxfHuMP6umE5QK7UmTeOAymo+Zx1Fxiuw9rVx8taHQ==",
      "license": "MIT"
    },
    "node_modules/node-domexception": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/node-domexception/-/node-domexception-1.0.0.tgz",
      "integrity": "sha512-/jKZoMpw0F8GRwl4/eLROPA3cfcXtLApP0QzLmUT/HuPCZWyB7IY9ZrMeKw2O/nFIqPQB3PVM9aYm0F312AXDQ==",
      "deprecated": "Use your platform's native DOMException instead",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/jimmywarting"
        },
        {
          "type": "github",
          "url": "https://paypal.me/jimmywarting"
        }
      ],
      "license": "MIT",
      "engines": {
        "node": ">=10.5.0"
      }
    },
    "node_modules/node-fetch": {
      "version": "3.3.2",
      "resolved": "https://registry.npmjs.org/node-fetch/-/node-fetch-3.3.2.tgz",
      "integrity": "sha512-dRB78srN/l6gqWulah9SrxeYnxeddIG30+GOqK/9OlLVyLg3HPnr6SqOWTWOXKRwC2eGYCkZ59NNuSgvSrpgOA==",
      "license": "MIT",
      "dependencies": {
        "data-uri-to-buffer": "^4.0.0",
        "fetch-blob": "^3.1.4",
        "formdata-polyfill": "^4.0.10"
      },
      "engines": {
        "node": "^12.20.0 || ^14.13.1 || >=16.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/node-fetch"
      }
    },
    "node_modules/node-gyp-build-optional-packages": {
      "version": "5.2.2",
      "resolved": "https://registry.npmjs.org/node-gyp-build-optional-packages/-/node-gyp-build-optional-packages-5.2.2.tgz",
      "integrity": "sha512-s+w+rBWnpTMwSFbaE0UXsRlg7hU4FjekKU4eyAih5T8nJuNZT1nNsskXpxmeqSK9UzkBl6UgRlnKc8hz8IEqOw==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "detect-libc": "^2.0.1"
      },
      "bin": {
        "node-gyp-build-optional-packages": "bin.js",
        "node-gyp-build-optional-packages-optional": "optional.js",
        "node-gyp-build-optional-packages-test": "build-test.js"
      }
    },
    "node_modules/object-hash": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/object-hash/-/object-hash-3.0.0.tgz",
      "integrity": "sha512-RSn9F68PjH9HqtltsSnqYC1XXoWe9Bju5+213R98cNGttag9q9yAOTzdbsqvIa7aNm5WffBZFpWYr2aWrklWAw==",
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/object-inspect": {
      "version": "1.13.4",
      "resolved": "https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz",
      "integrity": "sha512-W67iLl4J2EXEGTbfeHCffrjDfitvLANg0UlX3wFUUSTx92KXRFegMHUVgSqE+wvhAbi4WqjGg9czysTV2Epbew==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/on-finished": {
      "version": "2.4.1",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.4.1.tgz",
      "integrity": "sha512-oVlzkg3ENAhCk2zdv7IJwd/QUD4z2RxRwpkcGY8psCVcCYZNq4wYnVWALHM+brtuJjePWiYF/ClmuDr8Ch5+kg==",
      "license": "MIT",
      "dependencies": {
        "ee-first": "1.1.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/once": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
      "integrity": "sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==",
      "license": "ISC",
      "dependencies": {
        "wrappy": "1"
      }
    },
    "node_modules/parseurl": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz",
      "integrity": "sha512-CiyeOxFT/JZyN5m0z9PfXw4SCBJ6Sygz1Dpl0wqjlhDEGGBP1GnsUVEL0p63hoG1fcj3fHynXi9NYO4nWOL+qQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/path-to-regexp": {
      "version": "8.3.0",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-8.3.0.tgz",
      "integrity": "sha512-7jdwVIRtsP8MYpdXSwOS0YdD0Du+qOoF/AEPIt88PcCFrZCzx41oxku1jD88hZBwbNUIEfpqvuhjFaMAqMTWnA==",
      "license": "MIT",
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/proto3-json-serializer": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/proto3-json-serializer/-/proto3-json-serializer-3.0.3.tgz",
      "integrity": "sha512-iUi7jGLuECChuoUwtvf6eXBDcFXTHAt5GM6ckvtD3RqD+j2wW0GW6WndPOu9IWeUk7n933lzrskcNMHJy2tFSw==",
      "license": "Apache-2.0",
      "dependencies": {
        "protobufjs": "^7.4.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/protobufjs": {
      "version": "7.5.4",
      "resolved": "https://registry.npmjs.org/protobufjs/-/protobufjs-7.5.4.tgz",
      "integrity": "sha512-CvexbZtbov6jW2eXAvLukXjXUW1TzFaivC46BpWc/3BpcCysb5Vffu+B3XHMm8lVEuy2Mm4XGex8hBSg1yapPg==",
      "hasInstallScript": true,
      "license": "BSD-3-Clause",
      "dependencies": {
        "@protobufjs/aspromise": "^1.1.2",
        "@protobufjs/base64": "^1.1.2",
        "@protobufjs/codegen": "^2.0.4",
        "@protobufjs/eventemitter": "^1.1.0",
        "@protobufjs/fetch": "^1.1.0",
        "@protobufjs/float": "^1.0.2",
        "@protobufjs/inquire": "^1.1.0",
        "@protobufjs/path": "^1.1.2",
        "@protobufjs/pool": "^1.1.0",
        "@protobufjs/utf8": "^1.1.0",
        "@types/node": ">=13.7.0",
        "long": "^5.0.0"
      },
      "engines": {
        "node": ">=12.0.0"
      }
    },
    "node_modules/proxy-addr": {
      "version": "2.0.7",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.7.tgz",
      "integrity": "sha512-llQsMLSUDUPT44jdrU/O37qlnifitDP+ZwrmmZcoSKyLKvtZxpyV0n2/bD/N4tBAAZ/gJEdZU7KMraoK1+XYAg==",
      "license": "MIT",
      "dependencies": {
        "forwarded": "0.2.0",
        "ipaddr.js": "1.9.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/proxy-from-env": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-1.1.0.tgz",
      "integrity": "sha512-D+zkORCbA9f1tdWRK0RaCR3GPv50cMxcrz4X8k5LTSUD1Dkw47mKJEZQNunItRTkWwgtaUSo1RVFRIG9ZXiFYg==",
      "license": "MIT"
    },
    "node_modules/qs": {
      "version": "6.14.0",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.14.0.tgz",
      "integrity": "sha512-YWWTjgABSKcvs/nWBi9PycY/JiPJqOD4JA6o9Sej2AtvSGarXxKC3OQSk4pAarbdQlKAh5D4FCQkJNkW+GAn3w==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "side-channel": "^1.1.0"
      },
      "engines": {
        "node": ">=0.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/range-parser": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz",
      "integrity": "sha512-Hrgsx+orqoygnmhFbKaHE6c296J+HTAQXoxEF6gNupROmmGJRoyzfG3ccAveqCBrwr/2yxQ5BVd/GTl5agOwSg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/raw-body": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-3.0.1.tgz",
      "integrity": "sha512-9G8cA+tuMS75+6G/TzW8OtLzmBDMo8p1JRxN5AZ+LAp8uxGA8V8GZm4GQ4/N5QNQEnLmg6SS7wyuSmbKepiKqA==",
      "license": "MIT",
      "dependencies": {
        "bytes": "3.1.2",
        "http-errors": "2.0.0",
        "iconv-lite": "0.7.0",
        "unpipe": "1.0.0"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/raw-body/node_modules/iconv-lite": {
      "version": "0.7.0",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.7.0.tgz",
      "integrity": "sha512-cf6L2Ds3h57VVmkZe+Pn+5APsT7FpqJtEhhieDCvrE2MK5Qk9MyffgQyuxQTm6BChfeZNtcOLHp9IcWRVcIcBQ==",
      "license": "MIT",
      "dependencies": {
        "safer-buffer": ">= 2.1.2 < 3.0.0"
      },
      "engines": {
        "node": ">=0.10.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/readable-stream": {
      "version": "3.6.2",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz",
      "integrity": "sha512-9u/sniCrY3D5WdsERHzHE4G2YCXqoG5FTHUiCC4SIbr6XcLZBY05ya9EKjYek9O5xOAwjGq+1JdGBAS7Q9ScoA==",
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.3",
        "string_decoder": "^1.1.1",
        "util-deprecate": "^1.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/redis-errors": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/redis-errors/-/redis-errors-1.2.0.tgz",
      "integrity": "sha512-1qny3OExCf0UvUV/5wpYKf2YwPcOqXzkwKKSmKHiE6ZMQs5heeE/c8eXK+PNllPvmjgAbfnsbpkGZWy8cBpn9w==",
      "license": "MIT",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/redis-parser": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/redis-parser/-/redis-parser-3.0.0.tgz",
      "integrity": "sha512-DJnGAeenTdpMEH6uAJRK/uiyEIH9WVsUmoLwzudwGJUwZPp80PDBWPHXSAGNPwNvIXAbe7MSUB1zQFugFml66A==",
      "license": "MIT",
      "dependencies": {
        "redis-errors": "^1.0.0"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/require-directory": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz",
      "integrity": "sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/retry-request": {
      "version": "8.0.2",
      "resolved": "https://registry.npmjs.org/retry-request/-/retry-request-8.0.2.tgz",
      "integrity": "sha512-JzFPAfklk1kjR1w76f0QOIhoDkNkSqW8wYKT08n9yysTmZfB+RQ2QoXoTAeOi1HD9ZipTyTAZg3c4pM/jeqgSw==",
      "license": "MIT",
      "dependencies": {
        "extend": "^3.0.2",
        "teeny-request": "^10.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/router": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/router/-/router-2.2.0.tgz",
      "integrity": "sha512-nLTrUKm2UyiL7rlhapu/Zl45FwNgkZGaCpZbIHajDYgwlJCOzLSk+cIPAnsEqV955GjILJnKbdQC1nVPz+gAYQ==",
      "license": "MIT",
      "dependencies": {
        "debug": "^4.4.0",
        "depd": "^2.0.0",
        "is-promise": "^4.0.0",
        "parseurl": "^1.3.3",
        "path-to-regexp": "^8.0.0"
      },
      "engines": {
        "node": ">= 18"
      }
    },
    "node_modules/safe-buffer": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
      "integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==",
      "license": "MIT"
    },
    "node_modules/semver": {
      "version": "7.7.2",
      "resolved": "https://registry.npmjs.org/semver/-/semver-7.7.2.tgz",
      "integrity": "sha512-RF0Fw+rO5AMf9MAyaRXI4AV0Ulj5lMHqVxxdSgiVbixSCXoEmmX/jk0CuJw4+3SqroYO9VoUh+HcuJivvtJemA==",
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/send": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/send/-/send-1.2.0.tgz",
      "integrity": "sha512-uaW0WwXKpL9blXE2o0bRhoL2EGXIrZxQ2ZQ4mgcfoBxdFmQold+qWsD2jLrfZ0trjKL6vOw0j//eAwcALFjKSw==",
      "license": "MIT",
      "dependencies": {
        "debug": "^4.3.5",
        "encodeurl": "^2.0.0",
        "escape-html": "^1.0.3",
        "etag": "^1.8.1",
        "fresh": "^2.0.0",
        "http-errors": "^2.0.0",
        "mime-types": "^3.0.1",
        "ms": "^2.1.3",
        "on-finished": "^2.4.1",
        "range-parser": "^1.2.1",
        "statuses": "^2.0.1"
      },
      "engines": {
        "node": ">= 18"
      }
    },
    "node_modules/serve-static": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-2.2.0.tgz",
      "integrity": "sha512-61g9pCh0Vnh7IutZjtLGGpTA355+OPn2TyDv/6ivP2h/AdAVX9azsoxmg2/M6nZeQZNYBEwIcsne1mJd9oQItQ==",
      "license": "MIT",
      "dependencies": {
        "encodeurl": "^2.0.0",
        "escape-html": "^1.0.3",
        "parseurl": "^1.3.3",
        "send": "^1.2.0"
      },
      "engines": {
        "node": ">= 18"
      }
    },
    "node_modules/setprototypeof": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.2.0.tgz",
      "integrity": "sha512-E5LDX7Wrp85Kil5bhZv46j8jOeboKq5JMmYM3gVGdGH8xFpPWXUMsNrlODCrkoxMEeNi/XZIwuRvY4XNwYMJpw==",
      "license": "ISC"
    },
    "node_modules/side-channel": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz",
      "integrity": "sha512-ZX99e6tRweoUXqR+VBrslhda51Nh5MTQwou5tnUDgbtyM0dBgmhEDtWGP/xbKn6hqfPRHujUNwz5fy/wbbhnpw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3",
        "side-channel-list": "^1.0.0",
        "side-channel-map": "^1.0.1",
        "side-channel-weakmap": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-list": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.0.tgz",
      "integrity": "sha512-FCLHtRD/gnpCiCHEiJLOwdmFP+wzCmDEkc9y7NsYxeF4u7Btsn1ZuwgwJGxImImHicJArLP4R0yX4c2KCrMrTA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-map": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz",
      "integrity": "sha512-VCjCNfgMsby3tTdo02nbjtM/ewra6jPHmpThenkTYh8pG9ucZ/1P8So4u4FGBek/BjpOVsDCMoLA/iuBKIFXRA==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-weakmap": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz",
      "integrity": "sha512-WPS/HvHQTYnHisLo9McqBHOJk2FkHO/tlpvldyrnem4aeQp4hai3gythswg6p01oSoTl58rcpiFAjF2br2Ak2A==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3",
        "side-channel-map": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/standard-as-callback": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/standard-as-callback/-/standard-as-callback-2.1.0.tgz",
      "integrity": "sha512-qoRRSyROncaz1z0mvYqIE4lCd9p2R90i6GxW3uZv5ucSu8tU7B5HXUP1gG8pVZsYNVaXjk8ClXHPttLyxAL48A==",
      "license": "MIT"
    },
    "node_modules/statuses": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-2.0.2.tgz",
      "integrity": "sha512-DvEy55V3DB7uknRo+4iOGT5fP1slR8wQohVdknigZPMpMstaKJQWhwiYBACJE3Ul2pTnATihhBYnRhZQHGBiRw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/stream-events": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/stream-events/-/stream-events-1.0.5.tgz",
      "integrity": "sha512-E1GUzBSgvct8Jsb3v2X15pjzN1tYebtbLaMg+eBOUOAxgbLoSbT2NS91ckc5lJD1KfLjId+jXJRgo0qnV5Nerg==",
      "license": "MIT",
      "dependencies": {
        "stubs": "^3.0.0"
      }
    },
    "node_modules/stream-shift": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/stream-shift/-/stream-shift-1.0.3.tgz",
      "integrity": "sha512-76ORR0DO1o1hlKwTbi/DM3EXWGf3ZJYO8cXX5RJwnul2DEg2oyoZyjLNoQM8WsvZiFKCRfC1O0J7iCvie3RZmQ==",
      "license": "MIT"
    },
    "node_modules/string_decoder": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz",
      "integrity": "sha512-hkRX8U1WjJFd8LsDJ2yQ/wWWxaopEsABU1XfkM8A+j0+85JAGppt16cr1Whg6KIbb4okU6Mql6BOj+uup/wKeA==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "~5.2.0"
      }
    },
    "node_modules/string-width": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "license": "MIT",
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/stubs": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/stubs/-/stubs-3.0.0.tgz",
      "integrity": "sha512-PdHt7hHUJKxvTCgbKX9C1V/ftOcjJQgz8BZwNfV5c4B6dcGqlpelTbJ999jBGZ2jYiPAwcX5dP6oBwVlBlUbxw==",
      "license": "MIT"
    },
    "node_modules/teeny-request": {
      "version": "10.1.0",
      "resolved": "https://registry.npmjs.org/teeny-request/-/teeny-request-10.1.0.tgz",
      "integrity": "sha512-3ZnLvgWF29jikg1sAQ1g0o+lr5JX6sVgYvfUJazn7ZjJroDBUTWp44/+cFVX0bULjv4vci+rBD+oGVAkWqhUbw==",
      "license": "Apache-2.0",
      "dependencies": {
        "http-proxy-agent": "^5.0.0",
        "https-proxy-agent": "^5.0.0",
        "node-fetch": "^3.3.2",
        "stream-events": "^1.0.5"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/teeny-request/node_modules/agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "license": "MIT",
      "dependencies": {
        "debug": "4"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/teeny-request/node_modules/https-proxy-agent": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-5.0.1.tgz",
      "integrity": "sha512-dFcAjpTQFgoLMzC2VwU+C/CbS7uRL0lWmxDITmqm7C+7F0Odmj6s9l6alZc6AELXhrnggM2CeWSXHGOdX2YtwA==",
      "license": "MIT",
      "dependencies": {
        "agent-base": "6",
        "debug": "4"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/toidentifier": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz",
      "integrity": "sha512-o5sSPKEkg/DIQNmH43V0/uerLrpzVedkUh8tGNvaeXpfpuwjKenlSox/2O/BTlZUtEe+JG7s5YhEz608PlAHRA==",
      "license": "MIT",
      "engines": {
        "node": ">=0.6"
      }
    },
    "node_modules/tslib": {
      "version": "2.8.1",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
      "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
      "license": "0BSD"
    },
    "node_modules/type-is": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-2.0.1.tgz",
      "integrity": "sha512-OZs6gsjF4vMp32qrCbiVSkrFmXtG/AZhY3t0iAMrMBiAZyV9oALtXO8hsrHbMXF9x6L3grlFuwW2oAz7cav+Gw==",
      "license": "MIT",
      "dependencies": {
        "content-type": "^1.0.5",
        "media-typer": "^1.1.0",
        "mime-types": "^3.0.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/undici-types": {
      "version": "7.14.0",
      "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-7.14.0.tgz",
      "integrity": "sha512-QQiYxHuyZ9gQUIrmPo3IA+hUl4KYk8uSA7cHrcKd/l3p1OTpZcM0Tbp9x7FAtXdAYhlasd60ncPpgu6ihG6TOA==",
      "license": "MIT"
    },
    "node_modules/unpipe": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
      "integrity": "sha512-pjy2bYhSsufwWlKwPc+l3cN7+wuJlK6uz0YdJEOlQDbl6jo/YlPi4mb8agUkVC8BF7V8NuzeyPNqRksA3hztKQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
      "license": "MIT"
    },
    "node_modules/uuid": {
      "version": "11.1.0",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-11.1.0.tgz",
      "integrity": "sha512-0/A9rDy9P7cJ+8w1c9WD9V//9Wj15Ce2MPz8Ri6032usz+NfePxx5AcN3bN+r6ZL6jEo066/yNYB3tn4pQEx+A==",
      "funding": [
        "https://github.com/sponsors/broofa",
        "https://github.com/sponsors/ctavan"
      ],
      "license": "MIT",
      "bin": {
        "uuid": "dist/esm/bin/uuid"
      }
    },
    "node_modules/vary": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
      "integrity": "sha512-BNGbWLfd0eUPabhkXUVm0j8uuvREyTh5ovRa/dyow/BqAbZJyC+5fU+IzQOzmAKzYqYRAISoRhdQr3eIZ/PXqg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/web-streams-polyfill": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/web-streams-polyfill/-/web-streams-polyfill-3.3.3.tgz",
      "integrity": "sha512-d2JWLCivmZYTSIoge9MsgFCZrt571BikcWGYkjC1khllbTeDlGqZ2D8vD8E/lJa8WGWbb7Plm8/XJYV7IJHZZw==",
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/wrap-ansi": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
      "integrity": "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==",
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^4.0.0",
        "string-width": "^4.1.0",
        "strip-ansi": "^6.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
      }
    },
    "node_modules/wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==",
      "license": "ISC"
    },
    "node_modules/y18n": {
      "version": "5.0.8",
      "resolved": "https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz",
      "integrity": "sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA==",
      "license": "ISC",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/yargs": {
      "version": "17.7.2",
      "resolved": "https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz",
      "integrity": "sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w==",
      "license": "MIT",
      "dependencies": {
        "cliui": "^8.0.1",
        "escalade": "^3.1.1",
        "get-caller-file": "^2.0.5",
        "require-directory": "^2.1.1",
        "string-width": "^4.2.3",
        "y18n": "^5.0.5",
        "yargs-parser": "^21.1.1"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/yargs-parser": {
      "version": "21.1.1",
      "resolved": "https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz",
      "integrity": "sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    }
  }
}

```

## File: package.json
```
{
  "name": "api-shopee",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "@google-cloud/bigquery": "^8.1.1",
    "@google-cloud/secret-manager": "^6.1.1",
    "axios": "^1.12.2",
    "bottleneck": "^2.19.5",
    "bullmq": "^5.58.9",
    "dotenv": "^17.2.2",
    "express": "^5.1.0",
    "ioredis": "^5.8.2"
  }
}

```

## File: processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios from 'axios';
import crypto from 'crypto';
import 'dotenv/config';
import { fetchAdsTotalBalance } from './functions/fetchAdsTotalBalance.js';
import { fetchAffiliateSpending } from './functions/fetchAffiliateSpending.js';
import { fetchGMVMaxSpending } from './functions/fetchGMVMaxSpending.js';
import { fetchTiktokBasicAds } from './functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from './functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from './functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from './functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from './functions/fetchPGMVMaxBreakdown.js';
import { fetchAdsProductLevel } from './functions/fetchAdsProductLevel.js';
import { fetchAffiliateData } from './functions/amsProcessor.js';
import { fetchDanaDilepas, mainDanaDilepas } from './functions/escrowProcessor.js';
import { handleWalletTransactions } from './functions/walletTransactions.js';
// import fs from 'fs';
// import path from 'path';
// import { fileURLToPath } from 'url';

const port = 3000
const secretClient = new SecretManagerServiceClient();

export const HOST = "https://partner.shopeemobile.com";
const PATH = "/api/v2/order/get_order_list";

export const PARTNER_ID = parseInt(process.env.PARTNER_ID);
export const PARTNER_KEY = process.env.PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.SHOP_ID);

const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";

export let ACCESS_TOKEN;
let REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');

    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        ACCESS_TOKEN = newAccessToken;
        REFRESH_TOKEN = newRefreshToken;

        // saveTokensToFile({ accessToken: ACCESS_TOKEN, refreshToken: REFRESH_TOKEN });

        saveTokensToSecret({ accessToken: ACCESS_TOKEN, refreshToken: REFRESH_TOKEN });
    } else {
        console.log("[EG] Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'UTF-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
    } catch (e) {
        console.log("Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.log("Error loading tokens from Secret Manager: ", e);
    }
}

const jakartaOffset = 7 * 60 * 60;

function getJakartaTimestampTimeFrom(year, month, day, hour, minute, second) {
    const date = new Date(Date.UTC(year, month, day, hour, minute, second));
    return Math.floor(date.getTime() / 1000) - jakartaOffset;
}

function getJakartaTimestampTimeTo(year, month, day, hour, minute, second) {
    const date = new Date(Date.UTC(year, month, day, hour, minute, second));
    return Math.floor(date.getTime() / 1000) - jakartaOffset;
}

export function getStartOfMonthTimestampWIB() {
    const now = new Date(); 
    const year = now.getFullYear();
    const month = now.getMonth();
    const startOfMonthUTC = new Date(Date.UTC(year, month, 0, 0, 0, 0)); 
    const startOfMonthWIB = new Date(startOfMonthUTC.getTime() - (7 * 60 * 60 * 1000));
    return Math.floor(startOfMonthWIB.getTime() / 1000);
}

export function getEndOfYesterdayTimestampWIB() {
    const now = new Date(); 
    const startOfTodayUTC = new Date(Date.UTC(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0));
    const startOfTodayWIB = new Date(startOfTodayUTC.getTime() - (7 * 60 * 60 * 1000));
    const endOfYesterdayWIB = new Date(startOfTodayWIB.getTime() - 1000); // Subtract 1 second
    return Math.floor(endOfYesterdayWIB.getTime() / 1000);
}

// Function to get UTC Unix timestamp for the START of the PREVIOUS month in WIB
export function getStartOfPreviousMonthTimestampWIB() {
    const now = new Date();
    // Calculate the year and month of the previous month
    let prevMonthYear = now.getFullYear();
    let prevMonthMonth = now.getMonth() - 1; // Month is 0-indexed (Jan=0)
    if (prevMonthMonth < 0) {
        prevMonthMonth = 11; // December
        prevMonthYear--;
    }
    // Create date for the 1st of the PREVIOUS month IN UTC, then adjust back 7 hours for WIB
    const startOfPrevMonthUTC = new Date(Date.UTC(prevMonthYear, prevMonthMonth, 1, 0, 0, 0));
    const startOfPrevMonthWIB = new Date(startOfPrevMonthUTC.getTime() - (7 * 60 * 60 * 1000));
    return Math.floor(startOfPrevMonthWIB.getTime() / 1000);
}

// Function to get UTC Unix timestamp for the END of the PREVIOUS month in WIB
export function getEndOfPreviousMonthTimestampWIB() {
    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth(); // Current month
    // Create date for the 1st of the CURRENT month IN UTC, adjust back 7 hours for WIB midnight
    const startOfMonthUTC = new Date(Date.UTC(year, month, 1, 0, 0, 0));
    const startOfMonthWIB = new Date(startOfMonthUTC.getTime() - (7 * 60 * 60 * 1000));
    // Subtract 1 second to get the end of the PREVIOUS month WIB
    const endOfPrevMonthWIB = new Date(startOfMonthWIB.getTime() - 1000);
    return Math.floor(endOfPrevMonthWIB.getTime() / 1000);
}

export async function fetchAndProcessOrders() {
    console.log("[EG] Start fetching ads total balance. Calling the function.");
    let brand = "Eileen Grace";

    const loadedTokens = await loadTokensFromSecret();
    ACCESS_TOKEN = loadedTokens.accessToken;
    REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, ACCESS_TOKEN, SHOP_ID)
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, ACCESS_TOKEN, SHOP_ID);
    // await fetchDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, ACCESS_TOKEN, SHOP_ID);
    // await fetchAdsProductLevel(brand, PARTNER_ID, PARTNER_KEY, ACCESS_TOKEN, SHOP_ID);


    await fetchAffiliateData(brand, SHOP_ID, 1000);

    let advIdEG = "6899326735087566850";
    const basicAdsData = await fetchTiktokBasicAds(brand, advIdEG);
    const pgmvMaxData = await fetchProductGMVMax(brand, advIdEG);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advIdEG);
    
    console.log("[EG] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advIdEG);

    // Rocketindo Shop
    let advIdRshop = "7581835025746771976";
    let brandRshop = "Rocketindo Shop"
    
    const basicAdsDataRshop = await fetchTiktokBasicAds(brandRshop, advIdRshop, 50000);
    const pgmvMaxDataRshop = await fetchProductGMVMax(brandRshop, advIdRshop, 52000);
    const lgmvMaxDataRshop = await fetchLiveGMVMax(brandRshop, advIdRshop, 54000);

    await handleTiktokAdsData(basicAdsDataRshop, pgmvMaxDataRshop, lgmvMaxDataRshop, brandRshop);

    await fetchPGMVMaxBreakdown(brandRshop, advIdRshop)

    // Relove, JR, Enchante
    await handleNaruko();
    await handleRelove();
    await handleJR();
    // await handleEnchante();
    await handleRocketindoShop();
}

export const DRJOU_PARTNER_ID = parseInt(process.env.DRJOU_PARTNER_ID);
export const DRJOU_PARTNER_KEY = process.env.DRJOU_PARTNER_KEY;
const NEW_BRANDS_REFRESH_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
let NEW_BRANDS_ACCESS_TOKEN, NEW_BRANDS_REFRESH_TOKEN;

async function refreshTokenNewBrands(brand, shop_id) {
    console.log("Refreshing token for brand: ", brand);

    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${DRJOU_PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', DRJOU_PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${NEW_BRANDS_REFRESH_URL}?partner_id=${DRJOU_PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: NEW_BRANDS_REFRESH_TOKEN,
        partner_id: DRJOU_PARTNER_ID,
        shop_id: shop_id
    }

    console.log("Hitting Refresh Token endpoint New Brands: ", fullUrl);

    try {
        const response = await axios.post(fullUrl, body, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
    
        const newAccessToken = response.data.access_token;
        const newRefreshToken = response.data.refresh_token;
    
        if(newAccessToken && newRefreshToken) {
            NEW_BRANDS_ACCESS_TOKEN = newAccessToken;
            NEW_BRANDS_REFRESH_TOKEN = newRefreshToken;
    
            await saveTokensNewBrands(brand, {
                accessToken: NEW_BRANDS_ACCESS_TOKEN,
                refreshToken: NEW_BRANDS_REFRESH_TOKEN
            });
        } else {
            console.log("[NEW-BRANDS] token refresh not found :(")
            throw new Error("NEW BRANDS Tokens dont exist");
        }
    } catch (e) {
        console.log("[NEW-BRANDS] Error refreshing new brands token: ", e);
    }
}

let brandSecret = {
    "Naruko": "projects/231801348950/secrets/naruko-shopee-tokens",
    "Relove": "projects/231801348950/secrets/relove-shopee-tokens",
    "Joey & Roo": "projects/231801348950/secrets/joey-roo-shopee-tokens",
    "Enchante": "projects/231801348950/secrets/enchante-shopee-tokens",
    "Rocketindo Shop": "projects/231801348950/secrets/rocketindoshop-shopee-tokens",
}

async function saveTokensNewBrands(brand, tokens) {
    let parent = brandSecret[brand];
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');
    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("[NEW-BRANDS] Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[NEW-BRANDS] Successfully saved tokens to New Brands Secret Manager: ", parent);
    } catch (e) {
        console.error("[NEW-BRANDS] Error saving tokens to Secret Manager: ", e);
    }
}


async function loadTokensNewBrands(brand) {
    let brandSecretName = {
        "Naruko": "projects/231801348950/secrets/naruko-shopee-tokens/versions/latest",
        "Relove": "projects/231801348950/secrets/relove-shopee-tokens/versions/latest",
        "Joey & Roo": "projects/231801348950/secrets/joey-roo-shopee-tokens/versions/latest",
        "Enchante": "projects/231801348950/secrets/enchante-shopee-tokens/versions/latest",
        "Rocketindo Shop": "projects/231801348950/secrets/rocketindoshop-shopee-tokens/versions/latest",
    }
    const secretName = brandSecretName[brand];
    console.log("SECRET NAME: ", secretName);
    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log(brand, " Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[NEW-BRANDS] Error loading tokens from Secret Manager: ", e);
    }
}

async function handleNaruko() {
    let brand = "Naruko";
    let shopId = 1638001566;

    const loadedTokens = await loadTokensNewBrands(brand);
    NEW_BRANDS_ACCESS_TOKEN = loadedTokens.accessToken;
    NEW_BRANDS_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshTokenNewBrands(brand, shopId)

    await mainDanaDilepas(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
    await handleWalletTransactions(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
}

async function handleRelove() {
    let advId = "7374006579160612865";
    let brand = "Relove";
    let shopId = 1684312913;

    const basicAds = await fetchTiktokBasicAds(brand, advId, 56000);
    const pgmvMax = await fetchProductGMVMax(brand, advId, 58000);
    const lgmvMax = await fetchLiveGMVMax(brand, advId, 60000);

    await handleTiktokAdsData(basicAds, pgmvMax, lgmvMax, brand);

    await fetchPGMVMaxBreakdown(brand, advId);
    
    const loadedTokens = await loadTokensNewBrands(brand);
    NEW_BRANDS_ACCESS_TOKEN = loadedTokens.accessToken;
    NEW_BRANDS_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshTokenNewBrands(brand, shopId);

    await mainDanaDilepas(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
    await fetchAdsTotalBalance(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId)
    await handleWalletTransactions(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
}

async function handleJR() {
    let advId = "7431433066935091201"
    let brand = "Joey & Roo"
    let brandTT = "Joey Roo"
    let shopId = 1682176843

    const basicAds = await fetchTiktokBasicAds(brandTT, advId, 62000);
    const pgmvMax = await fetchProductGMVMax(brandTT, advId, 64000);
    const lgmvMax = await fetchLiveGMVMax(brandTT, advId, 66000);

    await handleTiktokAdsData(basicAds, pgmvMax, lgmvMax, brand);

    await fetchPGMVMaxBreakdown(brandTT, advId);
    const loadedTokens = await loadTokensNewBrands(brand);
    NEW_BRANDS_ACCESS_TOKEN = loadedTokens.accessToken;
    NEW_BRANDS_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshTokenNewBrands(brand, shopId);

    await mainDanaDilepas(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
    await handleWalletTransactions(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
}

async function handleEnchante() {
    let advId = "7579206207240765448"
    let brand = "Enchante"
    let shopId = 1684342027

    const basicAds = await fetchTiktokBasicAds(brand, advId, 68000);
    const pgmvMax = await fetchProductGMVMax(brand, advId, 70000);
    const lgmvMax = await fetchLiveGMVMax(brand, advId, 72000);

    await handleTiktokAdsData(basicAds, pgmvMax, lgmvMax, brand);

    await fetchPGMVMaxBreakdown(brand, advId);
    
    const loadedTokens = await loadTokensNewBrands(brand);
    NEW_BRANDS_ACCESS_TOKEN = loadedTokens.accessToken;
    NEW_BRANDS_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshTokenNewBrands(brand, shopId);

    await mainDanaDilepas(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
    await handleWalletTransactions(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
}

async function handleRocketindoShop() {
    let brand = "Rocketindo Shop";
    let shopId = 375791385;

    const loadedTokens = await loadTokensNewBrands(brand);
    NEW_BRANDS_ACCESS_TOKEN = loadedTokens.accessToken;
    NEW_BRANDS_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshTokenNewBrands(brand, shopId)

    await mainDanaDilepas(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
    await handleWalletTransactions(brand, DRJOU_PARTNER_ID, DRJOU_PARTNER_KEY, NEW_BRANDS_ACCESS_TOKEN, shopId);
}
```

## File: return-list.json
```
{
    "image": [],
    "buyer_videos": [],
    "reason": "NOT_RECEIPT",
    "text_reason": "Paket di order udh lama ga smpai2",
    "return_sn": "2510010VK2V09YA",
    "refund_amount": 275200,
    "currency": "IDR",
    "create_time": 1759283371,
    "update_time": 1759419203,
    "status": "ACCEPTED",
    "due_date": 1759542570,
    "tracking_number": "",
    "needs_logistics": false,
    "amount_before_discount": 348000,
    "user": {
        "username": "reginarenden",
        "email": "*********na@yahoo.com",
        "portrait": "http://mms.img.susercontent.com/642dcc009528544c39da9094cce17424"
    },
    "item": [
        {
            "item_id": 460504215,
            "model_id": 290663617998,
            "name": "EILEEN GRACE - Moisturize Rose Jelly Mask 300 ml | Masker Wajah | Jerawat | Bruntus | Bopeng | Bekas Jerawat | Kemerahan | Skin Barrier | Mencerahkan | Melembapkan",
            "images": [
                "http://mms.img.susercontent.com/id-11134207-7ra0m-mbxsac3qg53a15",
                "http://mms.img.susercontent.com/id-11134207-7rbk4-m7ucamheohhs59",
                "http://mms.img.susercontent.com/id-11134207-7ra0n-mcg3l7ne6pvfb0",
                "http://mms.img.susercontent.com/id-11134207-7ra0r-mcg3l7ne84fv88",
                "http://mms.img.susercontent.com/id-11134207-7ra0q-mcg3l7ne5baze5",
                "http://mms.img.susercontent.com/id-11134207-7ra0p-mb569uw0vflg30",
                "http://mms.img.susercontent.com/id-11134207-7rbkc-mb2ea7svt0tna4",
                "http://mms.img.susercontent.com/id-11134207-7rbkb-m7ucamhe91kna2"
            ],
            "amount": 1,
            "item_price": 344000,
            "is_add_on_deal": false,
            "is_main_item": false,
            "item_sku": "",
            "variation_sku": "EIGR0007",
            "add_on_deal_id": 0,
            "refund_amount": 275200,
            "hot_listing_item": false
        }
    ],
    "order_sn": "2509105J8RJMW7",
    "return_ship_due_date": 0,
    "return_seller_due_date": 0,
    "negotiation_status": "",
    "seller_proof_status": "NOT_NEEDED",
    "seller_compensation_status": "",
    "hot_listing_order": false,
    "return_refund_type": "RRBOC",
    "return_solution": 1,
    "seller_evidence_deadline": null,
    "negotiation": {
        "latest_solution": ""
    },
    "return_refund_request_type": 0,
    "validation_type": "seller_validation",
    "is_seller_arrange": false,
    "is_shipping_proof_mandatory": false
}
```

## File: todos.txt
```
TODOS:

# PRIORITY
- To create: LockGMV function.

# FEEDBACK - UPDATED WORK
- Lock GMV. On day 16 of the next month, fetch the previous month's orders & returns again.
- Integrate & re-run both handleOrders & handleReturns
- Deploy to GCP.


# MINIMUM VIABLE WORK - Oct 6th 2025
- Testing Case day 2 - 16. v
- Configure data structure to be like eileen_grace_orders_partitioned - SHOULD create new table.
- Datetime formatted UTC+7: YYYY-MM-DD XX:XX. Done with formatUnixTime(). v
- Hit v2.payment.get_escrow_detail_batch v
- Hit v2.returns.get_return_list and get_return_detail v


## Daily Scheduler
- Run at a specified time, like 17:00 today. v
- Run hourly. If this succeeds, then scheduler is complete. v
- Run everyday at a specified time, 00:05. v hehe

## Issues
- Case if day 1 - 16, configured. v
- Case if day 17 - 30/31 is done-ish. v
- Case day 1 October is tested and correct. Yay! v
- Case day 2 - 16, should try today. v

## Data to Merge
- Data structure to be configured like eileen_grace_orders_partitioned
- Datetime kudu formatted UTC+7: YYYY-MM-DD XX:XX v
- Fetch orders from get_order_list v
- Merge orders to eileen_grace_orders_log v
- Fetch orders with details from get_order_detail v
- Merge orders with details to eileen_grace_order_detail v

## Deployment
- GCP: Cloud Run, Cloud Scheduler, and Memorystore for Redis.

# Scaling up
- Replicate the same authorization thing for other brands.
- Shopee: might need more App for each brand.
- Backend: should scale to accommodate 16 brands

# AUTHORIZATION
- Authorization is, gratefully, valid for 365 days hehe.
- Access token is invalid after 4 hours. How to get a new one? v
- Refresh token is invalid after 30 days. How to get a new one? v

# Stacks
- Express
- BullMQ
- Redis local on Docker, later Memorystore on GCP
- Shopee API & BigQuery API
- GCP: Cloud Run, Cloud Scheduler, Memorystore.

# API
- Get order list v
- Get order detail: REQUIRE customer detail, address, product bought, order value, etc. 
Current order detail lacks details. v
- Run the Get order list & Get order detail DAILY (see How Orders Are Fetched)
- Process the data according to BigQuery data structure
- Merge / Write to BigQuery
    - require table Order List Status Changes Log
        - order_sn
        - status
        - updated_at
    if status changed, REPLACE previous order_sn with the latest order_sn,
    so eileen_grace_orders_log should include UNIQUE order_sn with latest status.
    - require table Order Detail List
        - order_sn

# How Orders Are Fetched
- On the first day of the month, the whole previous month's orders are fetched.
- On October 1st, orders from 1 - 30 Sept are fetched.
- The equation: firstDayOfTheMonth until currentDay - 1 (yesterday)


# Reliability
- DATA MATCHED. Check if order data matches that of Shopee's. (try comparing first & last order) v
    - Order is not sorted by datetime
    - Earliest order fetched has id 250901AE5EY3DY and IS timely correct. v
    - Latest order fetched has id 250924A236C19G and IS timely correct. v
- Auto-retrying operations if network is bad or fails the first time.
```

## File: worker.js
```
import { fetchAndProcessOrdersMD } from './workers/md_processor.js';
import { fetchAndProcessOrders } from './processor.js';
import { fetchAndProcessOrdersSHRD } from './workers/shrd_processor.js';
import { Worker } from 'bullmq';
import 'dotenv/config';
import express from 'express';
import { fetchAndProcessOrdersCLEV } from './workers/clev_processor.js';
import { fetchAndProcessOrdersDRJOU } from './workers/drjou_processor.js';
import { fetchAndProcessOrdersMOSS } from './workers/moss_processor.js';
import { fetchAndProcessOrdersGB } from './workers/gb_processor.js';
import { fetchAndProcessOrdersIL } from './workers/il_processor.js';
import { fetchAndProcessOrdersEVOKE } from './workers/evoke_processor.js';
import { fetchAndProcessOrdersMMW } from './workers/mmw_processor.js';
import { fetchAndProcessOrdersCHESS } from './workers/chess_processor.js';
import { fetchAndProcessOrdersSV } from './workers/sv_processor.js';
import { fetchAndProcessOrdersPN } from './workers/pn_processor.js';
import { fetchAndProcessOrdersNB } from './workers/nb_processor.js';
import { fetchAndProcessOrdersMIRAE } from './workers/mirae_processor.js';
import { fetchAndProcessOrdersPOLY } from './workers/poly_processor.js';

const workerApp = express();
const port = process.env.PORT || 8080;

workerApp.get('/', (req, res) => {
    res.status(200).send("Worker is healthy");
});

workerApp.listen(port, () => {
    console.log("Health check server listening on port: ", port);
});

const workerOptions = {
    connection: {
        url: process.env.REDIS_URL,
        connectTimeout: 30000,
    },
    lockDuration: 5400000,
}

console.log("Worker is starting!");

const orderProcessor = async (job) => {
    switch(job.name) {
        case 'fetch-daily-orders':
        case 'manual-fetch':
            return fetchAndProcessOrders();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const orderWorker = new Worker("order-processing", orderProcessor, workerOptions);

const mdOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-md':
            return fetchAndProcessOrdersMD();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const mdWorker = new Worker("fetch-orders-md", mdOrderProcessor, workerOptions);

const shrdOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-shrd':
            return fetchAndProcessOrdersSHRD();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const shrdWorker = new Worker("fetch-orders-shrd", shrdOrderProcessor, workerOptions);

const clevOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-clev':
            return fetchAndProcessOrdersCLEV();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const clevWorker = new Worker("fetch-orders-clev", clevOrderProcessor, workerOptions);

const drjouOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-drjou':
            return fetchAndProcessOrdersDRJOU();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const drjouWorker = new Worker("fetch-orders-drjou", drjouOrderProcessor, workerOptions);

const mossOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-moss':
            return fetchAndProcessOrdersMOSS();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const mossWorker = new Worker("fetch-orders-moss", mossOrderProcessor, workerOptions);

const gbOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-gb':
            return fetchAndProcessOrdersGB();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const gbWorker = new Worker("fetch-orders-gb", gbOrderProcessor, workerOptions);

const ilOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-il':
            return fetchAndProcessOrdersIL();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const ilWorker = new Worker("fetch-orders-il", ilOrderProcessor, workerOptions);

const evOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-evoke':
            return fetchAndProcessOrdersEVOKE();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const evWorker = new Worker("fetch-orders-evoke", evOrderProcessor, workerOptions);

const mmwOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-mmw':
            return fetchAndProcessOrdersMMW();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const mmwWorker = new Worker("fetch-orders-mmw", mmwOrderProcessor, workerOptions);

const chessOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-chess':
            return fetchAndProcessOrdersCHESS();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const chessWorker = new Worker("fetch-orders-chess", chessOrderProcessor, workerOptions);

const svOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-sv':
            return fetchAndProcessOrdersSV();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const svWorker = new Worker("fetch-orders-sv", svOrderProcessor, workerOptions);

const pnOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-pn':
            return fetchAndProcessOrdersPN();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const pnWorker = new Worker("fetch-orders-pn", pnOrderProcessor, workerOptions);

const miraeOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-mirae':
            return fetchAndProcessOrdersMIRAE();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const miraeWorker = new Worker("fetch-orders-mirae", miraeOrderProcessor, workerOptions);

const polyOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-poly':
            return fetchAndProcessOrdersPOLY();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const polyWorker = new Worker("fetch-orders-poly", polyOrderProcessor, workerOptions);

const nbOrderProcessor = async (job) => {
    switch (job.name) {
        case 'fetch-orders-nb':
            return fetchAndProcessOrdersNB();
        default:
            throw new Error(`Unknown job name: ${job.name}`);
    }
}
const nbWorker = new Worker("fetch-orders-nb", nbOrderProcessor, workerOptions);

// Eileen Grace worker events
orderWorker.on('active', (job) => {
    console.log(`[eg-worker] Picked up job with ID ${job.id}.`);
});
orderWorker.on('completed', (job) => {
    console.log(`[eg-worker] Job with ID ${job.id} has completed.`);
});
orderWorker.on('ready', (job) => {
    console.log("[eg-worker] Worker is ready to listen.");
});
orderWorker.on('failed', (job, err) => {
    console.error(`[eg-worker] Job with ID ${job.id} has failed. Error:`, err);
});
orderWorker.on('error', (err) => {
    console.error('[eg-worker] Worker encountered an error:', err);
});

// Miss Daisy worker events
mdWorker.on('active', (job) => {
    console.log(`[MD] ACTIVE: Job ${job.id}.`);
});
mdWorker.on('completed', (job) => {
    console.log(`[MD] COMPLETED: Job ${job.id}.`);
});
mdWorker.on('ready', (job) => {
    console.log("[MD] MD Worker is ready to listen");
});
mdWorker.on('failed', (job, err) => {
    console.error(`[MD] FAILED: Job ${job.id}.`, err);
});

// SHRD
shrdWorker.on('active', (job) => {
    console.log(`[SHRD] ACTIVE: Job ${job.id}.`);
});
shrdWorker.on('completed', (job) => {
    console.log(`[SHRD] COMPLETED: Job ${job.id}.`);
});
shrdWorker.on('ready', (job) => {
    console.log("[SHRD] SHRD Worker is ready to listen");
});
shrdWorker.on('failed', (job, err) => {
    console.error(`[SHRD] FAILED: Job ${job.id}.`, err);
});

// Cleviant
clevWorker.on('active', (job) => {
    console.log(`[CLEV] ACTIVE: Job ${job.id}.`);
});
clevWorker.on('completed', (job) => {
    console.log(`[CLEV] COMPLETED: Job ${job.id}.`);
});
clevWorker.on('ready', (job) => {
    console.log("[CLEV] CLEV Worker is ready to listen");
});
clevWorker.on('failed', (job, err) => {
    console.error(`[CLEV] FAILED: Job ${job.id}.`, err);
});

// Dr. Jou
drjouWorker.on('active', (job) => {
    console.log(`[DRJOU] ACTIVE: Job ${job.id}.`);
});
drjouWorker.on('completed', (job) => {
    console.log(`[DRJOU] COMPLETED: Job ${job.id}.`);
});
drjouWorker.on('ready', (job) => {
    console.log("[DRJOU] DRJOU Worker is ready to listen");
});
drjouWorker.on('failed', (job, err) => {
    console.error(`[DRJOU] FAILED: Job ${job.id}.`, err);
});

// Mosseru
mossWorker.on('active', (job) => {
    console.log(`[MOSS] ACTIVE: Job ${job.id}.`);
});
mossWorker.on('completed', (job) => {
    console.log(`[MOSS] COMPLETED: Job ${job.id}.`);
});
mossWorker.on('ready', (job) => {
    console.log("[MOSS] MOSS Worker is ready to listen");
});
mossWorker.on('failed', (job, err) => {
    console.error(`[MOSS] FAILED: Job ${job.id}.`, err);
});

// G-Belle
gbWorker.on('active', (job) => {
    console.log(`[GBELLE] ACTIVE: Job ${job.id}.`);
});
gbWorker.on('completed', (job) => {
    console.log(`[GBELLE] COMPLETED: Job ${job.id}.`);
});
gbWorker.on('ready', (job) => {
    console.log("[GBELLE] GBELLE Worker is ready to listen");
});
gbWorker.on('failed', (job, err) => {
    console.error(`[GBELLE] FAILED: Job ${job.id}.`, err);
});

// Ivy & Lily
ilWorker.on('active', (job) => {
    console.log(`[IVYLILY] ACTIVE: Job ${job.id}.`);
});
ilWorker.on('completed', (job) => {
    console.log(`[IVYLILY] COMPLETED: Job ${job.id}.`);
});
ilWorker.on('ready', (job) => {
    console.log("[IVYLILY] IVYLILY Worker is ready to listen");
});
ilWorker.on('failed', (job, err) => {
    console.error(`[IVYLILY] FAILED: Job ${job.id}.`, err);
});

// Evoke
evWorker.on('active', (job) => {
    console.log(`[EVOKE] ACTIVE: Job ${job.id}.`);
});
evWorker.on('completed', (job) => {
    console.log(`[EVOKE] COMPLETED: Job ${job.id}.`);
});
evWorker.on('ready', (job) => {
    console.log("[EVOKE] EVOKE Worker is ready to listen");
});
evWorker.on('failed', (job, err) => {
    console.error(`[EVOKE] FAILED: Job ${job.id}.`, err);
});

// MMW
mmwWorker.on('active', (job) => {
    console.log(`[MMW] ACTIVE: Job ${job.id}.`);
});
mmwWorker.on('completed', (job) => {
    console.log(`[MMW] COMPLETED: Job ${job.id}.`);
});
mmwWorker.on('ready', (job) => {
    console.log("[MMW] MMW Worker is ready to listen");
});
mmwWorker.on('failed', (job, err) => {
    console.error(`[MMW] FAILED: Job ${job.id}.`, err);
});

// CHESS
chessWorker.on('active', (job) => {
    console.log(`[CHESS] ACTIVE: Job ${job.id}.`);
});
chessWorker.on('completed', (job) => {
    console.log(`[CHESS] COMPLETED: Job ${job.id}.`);
});
chessWorker.on('ready', (job) => {
    console.log("[CHESS] CHESS Worker is ready to listen");
});
chessWorker.on('failed', (job, err) => {
    console.error(`[CHESS] FAILED: Job ${job.id}.`, err);
});

// SV
svWorker.on('active', (job) => {
    console.log(`[SV] ACTIVE: Job ${job.id}.`);
});
svWorker.on('completed', (job) => {
    console.log(`[SV] COMPLETED: Job ${job.id}.`);
});
svWorker.on('ready', (job) => {
    console.log("[SV] SV Worker is ready to listen");
});
svWorker.on('failed', (job, err) => {
    console.error(`[SV] FAILED: Job ${job.id}.`, err);
});

// PN
pnWorker.on('active', (job) => {
    console.log(`[PN] ACTIVE: Job ${job.id}.`);
});
pnWorker.on('completed', (job) => {
    console.log(`[PN] COMPLETED: Job ${job.id}.`);
});
pnWorker.on('ready', (job) => {
    console.log("[PN] PN Worker is ready to listen");
});
pnWorker.on('failed', (job, err) => {
    console.error(`[PN] FAILED: Job ${job.id}.`, err);
});

// NB
nbWorker.on('active', (job) => {
    console.log(`[NB] ACTIVE: Job ${job.id}.`);
});
nbWorker.on('completed', (job) => {
    console.log(`[NB] COMPLETED: Job ${job.id}.`);
});
nbWorker.on('ready', (job) => {
    console.log("[NB] NB Worker is ready to listen");
});
nbWorker.on('failed', (job, err) => {
    console.error(`[NB] FAILED: Job ${job.id}.`, err);
});

// Poly
polyWorker.on('active', (job) => {
    console.log(`[POLY] ACTIVE: Job ${job.id}.`);
});
polyWorker.on('completed', (job) => {
    console.log(`[POLY] COMPLETED: Job ${job.id}.`);
});
polyWorker.on('ready', (job) => {
    console.log("[POLY] POLY Worker is ready to listen");
});
polyWorker.on('failed', (job, err) => {
    console.error(`[POLY] FAILED: Job ${job.id}.`, err);
});

// Mirae
miraeWorker.on('active', (job) => {
    console.log(`[MIRAE] ACTIVE: Job ${job.id}.`);
});
miraeWorker.on('completed', (job) => {
    console.log(`[MIRAE] COMPLETED: Job ${job.id}.`);
});
miraeWorker.on('ready', (job) => {
    console.log("[MIRAE] MIRAE Worker is ready to listen");
});
miraeWorker.on('failed', (job, err) => {
    console.error(`[MIRAE] FAILED: Job ${job.id}.`, err);
});

const gracefulShutdown = async () => {
    console.log("Shutting down worker...");

    await Promise.all([
        orderWorker.close(),
        mdWorker.close(),
        shrdWorker.close()
    ])
    
    console.log("Worker shut down complete.");
    process.exit(0);
}

process.on('SIGINT', gracefulShutdown);
process.on('SIGTERM', gracefulShutdown);

// 251001VCHANUW9
```

## File: functions\amsProcessor.js
```
import { BigQuery } from '@google-cloud/bigquery';
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios from 'axios';
import crypto from 'crypto';

export const PARTNER_ID = parseInt(process.env.AMS_PARTNER_ID);
export const PARTNER_KEY = process.env.AMS_PARTNER_KEY;

const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";
const secretClient = new SecretManagerServiceClient();
let AMS_ACCESS_TOKEN, AMS_REFRESH_TOKEN;

async function refreshToken(brand, shop_id) {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: AMS_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: shop_id
    }

    console.log("Hitting Refresh Token endpoint AMS: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        AMS_ACCESS_TOKEN = newAccessToken;
        AMS_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret(brand, {
            accessToken: AMS_ACCESS_TOKEN,
            refreshToken: AMS_REFRESH_TOKEN
        });
    } else {
        console.log("[AMS] token refresh not found :(")
        throw new Error("AMS Tokens dont exist");
    }
}

let brandSecret = {
    "Eileen Grace": "projects/231801348950/secrets/ams-shopee-tokens",
    "Mamaway": "projects/231801348950/secrets/mamaway-ams-shopee-tokens",
    "SH-RD": "projects/231801348950/secrets/shrd-ams-shopee-tokens",
    "Miss Daisy": "projects/231801348950/secrets/md-ams-shopee-tokens",
    "Polynia": "projects/231801348950/secrets/poly-ams-shopee-tokens",
    "Chess": "projects/231801348950/secrets/chess-ams-shopee-tokens",
    "Cleviant": "projects/231801348950/secrets/clev-ams-shopee-tokens",
    "Mosseru": "projects/231801348950/secrets/moss-ams-shopee-tokens",
    "Evoke": "projects/231801348950/secrets/evoke-ams-shopee-tokens",
    "Dr.Jou": "projects/231801348950/secrets/drjou-ams-shopee-tokens",
    "Mirae": "projects/231801348950/secrets/mirae-ams-shopee-tokens",
    "Swissvita": "projects/231801348950/secrets/sv-ams-shopee-tokens",
    "G-Belle": "projects/231801348950/secrets/gb-ams-shopee-tokens",
    "Past Nine": "projects/231801348950/secrets/pn-ams-shopee-tokens",
    "Nutri & Beyond": "projects/231801348950/secrets/nb-ams-shopee-tokens",
    "Ivy & Lily": "projects/231801348950/secrets/il-ams-shopee-tokens",
}

async function saveTokensToSecret(brand, tokens) {
    let parent = brandSecret[brand];
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');
    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("[AMS] Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[AMS] Successfully saved tokens to AMS Secret Manager: ", parent);
    } catch (e) {
        console.error("[AMS] Error saving tokens to Secret Manager: ", e);
    }
}


async function loadTokensFromSecret(brand) {
    let brandSecretName = {
        "Eileen Grace": "projects/231801348950/secrets/ams-shopee-tokens/versions/latest",
        "Mamaway": "projects/231801348950/secrets/mamaway-ams-shopee-tokens/versions/latest",
        "SH-RD": "projects/231801348950/secrets/shrd-ams-shopee-tokens/versions/latest",
        "Miss Daisy": "projects/231801348950/secrets/md-ams-shopee-tokens/versions/latest",
        "Polynia": "projects/231801348950/secrets/poly-ams-shopee-tokens/versions/latest",
        "Chess": "projects/231801348950/secrets/chess-ams-shopee-tokens/versions/latest",
        "Cleviant": "projects/231801348950/secrets/clev-ams-shopee-tokens/versions/latest",
        "Mosseru": "projects/231801348950/secrets/moss-ams-shopee-tokens/versions/latest",
        "Evoke": "projects/231801348950/secrets/evoke-ams-shopee-tokens/versions/latest",
        "Dr.Jou": "projects/231801348950/secrets/drjou-ams-shopee-tokens/versions/latest",
        "Mirae": "projects/231801348950/secrets/mirae-ams-shopee-tokens/versions/latest",
        "Swissvita": "projects/231801348950/secrets/sv-ams-shopee-tokens/versions/latest",
        "G-Belle": "projects/231801348950/secrets/gb-ams-shopee-tokens/versions/latest",
        "Past Nine": "projects/231801348950/secrets/pn-ams-shopee-tokens/versions/latest",
        "Nutri & Beyond": "projects/231801348950/secrets/nb-ams-shopee-tokens/versions/latest",
        "Ivy & Lily": "projects/231801348950/secrets/il-ams-shopee-tokens/versions/latest",
    }
    const secretName = brandSecretName[brand];
    console.log("SECRET NAME: ", secretName);
    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[AMS] Error loading tokens from Secret Manager: ", e);
    }
}

async function getPerformanceUpdateTime(brand, shop_id) {
    console.log("Running performance update time for brand: ", brand);

    let path = "/api/v2/ams/get_performance_data_update_time";

    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}${AMS_ACCESS_TOKEN}${shop_id}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');

    const params = new URLSearchParams({
        partner_id: PARTNER_ID, 
        timestamp,
        access_token: AMS_ACCESS_TOKEN,
        shop_id: shop_id,
        sign,
        marker_type: "AmsMarker"
    });

    const fullUrl = `${HOST}${path}?${params.toString()}`;
    
    try {
        const response = await axios.get(fullUrl, {
            headers: {
                'Content-Type': 'application/json'
            }
        })    
        if(response && response.data && response.data.response) {
            return response.data.response.last_report_date;
        }
        return "No data";
    } catch (e) {
        console.error("Error get performance update time: ", e.response);
    }
}

export async function fetchAffiliateData(brand, shop_id, sleepValue) {
    
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    
    await sleep(sleepValue);

    
    console.log('Fetch affiliate data on brand: ', brand);
    
    const loadedTokens = await loadTokensFromSecret(brand);
    AMS_ACCESS_TOKEN = loadedTokens.accessToken;
    AMS_REFRESH_TOKEN = loadedTokens.refreshToken;
    
    await refreshToken(brand, shop_id);
    
    const updateTime = await getPerformanceUpdateTime(brand, shop_id);
    if(updateTime) {
        console.log(`Performance Update Time for ${brand} is ${updateTime}`);
    }
    // Fetch affiliate data per shop_id

    const startDateUpdateTime = new Date(updateTime);
    // const startDateUpdateTime = new Date("2026-01-17");
    const startY = startDateUpdateTime.getFullYear();
    const startM = String(startDateUpdateTime.getMonth() + 1).padStart(2, '0');
    const startD = String(startDateUpdateTime.getDate()).padStart(2, '0');
    const startStr = `${startY}${startM}${startD}`;
    const startForData = `${startY}-${startM}-${startD}`;
    
    let success = false;
    let retries = 5;
    let data;
    
    const yesterday = new Date("2026-01-02");
    yesterday.setDate(yesterday.getDate());
    const yyyy = yesterday.getFullYear();
    const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
    const dd = String(yesterday.getDate()).padStart(2, '0');
    const yesterdayStr = `${yyyy}${mm}${dd}`;
    const yesterdayForData = `${yyyy}-${mm}-${dd}`;

    const today = new Date();
    const year = today.getFullYear();
    const month = String(yesterday.getMonth() + 1).padStart(2, '0');
    const day = String(yesterday.getDate()).padStart(2, '0');
    const todayStr = `${year}${month}${day}`;
    
    while(!success && retries > 0) {
        try {
            
            let path = "/api/v2/ams/get_shop_performance";
            
            const timestamp = Math.floor(Date.now() / 1000);
            const baseString = `${PARTNER_ID}${path}${timestamp}${AMS_ACCESS_TOKEN}${shop_id}`;
            const sign = crypto.createHmac('sha256', PARTNER_KEY)
                .update(baseString)
                .digest('hex');
            

            const params = new URLSearchParams({
                partner_id: PARTNER_ID, 
                timestamp,
                access_token: AMS_ACCESS_TOKEN,
                shop_id: shop_id,
                sign,
                period_type: 'Day',
                start_date: startStr,
                end_date: startStr,
                order_type: 'ConfirmedOrder',
                channel: 'AllChannel',
            });
            
            const fullUrl = `${HOST}${path}?${params.toString()}`;
            console.log(`[AMS] Hitting Affiliate Spending for ${brand}`);
            console.log(fullUrl);
            
            const response = await axios.get(fullUrl, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
    
            if(response && response.data && response.data.response) {
                success = true;
                console.log(`[AMS] res AMS data on brand: ${brand}`);
                data = response.data.response;
            } else {
                success = true;
                console.log("Non-retryable error.");
                console.log(response);
            }
        } catch (e) {
            console.error("[AMS] Error fetching AMS data on brand: ", brand);
            if(e.response?.status == 429) {
                console.log("Rate limit error");
                retries -= 1;
                await sleep(sleepValue * 1.5)
            } else {
                success = true;
                console.log("Non-rate-limit error: ");
                console.log(e.response);
            }
        }
    }
    console.log('Data before mergeData\n');
    console.log(data);

    await mergeData(data, brand, startForData);
}

const brandTables = {
    "Chess": "chess_ams",
    "Cleviant": "cleviant_ams",
    "Dr.Jou": "dr_jou_ams",
    "Evoke": "evoke_ams",
    "G-Belle": "gbelle_ams",
    "Ivy & Lily": "ivy_lily_ams",
    "Naruko": "naruko_ams",
    "Miss Daisy": "miss_daisy_ams",
    "Mirae": "mirae_ams",
    "Mamaway": "mamaway_ams",
    "Mosseru": "mosseru_ams",
    "Nutri & Beyond": "nutri_beyond_ams",
    "Past Nine": "past_nine_ams",
    "Polynia": "polynia_ams",
    "SH-RD": "shrd_ams",
    "Swissvita": "swissvita_ams",
    "Eileen Grace": "eileen_grace_ams",
    "Relove": "relove_ams",
    "Joey & Roo": "joey_roo_ams",
    "Enchante": "enchante_ams",
    "Rocketindo Shop": "rocketindo_shop_ams",
}

async function mergeData(data, brand, data_date) {
    console.log("[AMS] Start merging for brand: ", brand);
    console.log(data);
    const tableName = brandTables[brand];
    const bigquery = new BigQuery();
    const datasetId = 'shopee_api';

    try {
        const query = `
            SELECT date
            FROM \`${datasetId}.${tableName}\`
            WHERE date = @date
        `;

        const options = {
            query,
            params: {
                date: data_date
            }
        }

        const [rows] = await bigquery.query(options);

        if(rows.length > 0) {
            console.log("[AMS] Row already exists");
            return;
        }

        await bigquery 
            .dataset(datasetId)
            .table(tableName)
            .insert({
                date: data_date,
                sales: data.sales,
                gross_item_sold: data.gross_item_sold,
                orders: data.orders,
                clicks: data.clicks,
                est_commission: data.est_commission,
                roi: data.roi,
                total_buyers: data.total_buyers,
                new_buyers: data.new_buyers,
                process_dttm: new Date(Date.now() + 7 * 60 * 60 * 1000).toISOString().replace('T', ' ').substring(0, 19)
            });
        console.log(`[AMS] Merged to table ${tableName}`);
    } catch (e) {
        console.error(`Error inserting AMS data on ${brand}: ${e}`);
    }
}
```

## File: functions\escrowProcessor.js
```
import { BigQuery } from '@google-cloud/bigquery';
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios from 'axios';
import crypto from 'crypto';

export async function fetchDanaDilepas(brand, partner_id, partner_key, access_token, shop_id) {
    console.log("Fetch Dana Dilepas of brand: ", brand);

    const HOST = "https://partner.shopeemobile.com";
    const PATH = "/api/v2/payment/get_escrow_list";

    try {
    
        console.log("[SHOPEE-WITHDRAWAL] Raw response for brand: ", brand);
        const timestamp = Math.floor(Date.now() / 1000);
        const baseString = `${partner_id}${PATH}${timestamp}${access_token}${shop_id}`;
        const sign = crypto.createHmac('sha256', partner_key)
            .update(baseString)
            .digest('hex');
        
        let count = 0;
        let hasMore = true;
        let pageNumber = 1;
        let escrowContainer = [];

        while(hasMore) {
            const now = new Date();
            const releaseTimeEnd = Math.floor(now.getTime() / 1000);
            const releaseTimeStart = Math.floor((now.getTime() - (7 * 24 * 60 * 60 * 1000)) / 1000);
            const params = new URLSearchParams({
                partner_id: partner_id,
                timestamp,
                access_token: access_token,
                shop_id: shop_id,
                sign,
                release_time_from: releaseTimeStart,
                release_time_to: releaseTimeEnd,
                page_size: 100,
                page_no: pageNumber,
            });

            const fullUrl = `${HOST}${PATH}?${params.toString()}`;
            console.log(`Hitting Dana Dilepas for ${brand}: `, fullUrl, " - page: ", pageNumber);

            const response = await axios.get(fullUrl, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            let escrowList = response.data.response.escrow_list;
            escrowContainer.push(...escrowList);

            count += escrowList.length;
            hasMore = response.data.response.more;
            pageNumber += 1;
        }

        console.log("[SHOPEE-WITHDRAWAL] Data count: ", count);
        return escrowContainer;
    } catch (e) {
        console.log("[SHOPEE-WITHDRAWAL] ERROR on fetching Dana Dilepas on brand: ", brand);
        console.log(e.response);
    }

    // console.log("All Dana Dilepas on brand: ", brand);
    // console.log("Count: ", danaDilepas.length);
}

async function transformData(data, brand) {
    console.log("Dana Dilepas on brand: ", brand)
    console.log("All Order_Sns on Data before Transform: \n");
    
    let twentyBatchContainer = [];
    let twentyBatch = [];
    data.forEach(d => {
        
        twentyBatch.push(d.order_sn);

        if(twentyBatch.length == 20) {
            twentyBatchContainer.push(twentyBatch);
            twentyBatch = [];
        }
    });

    if (twentyBatch.length > 0) {
        twentyBatchContainer.push(twentyBatch);
    }

    return twentyBatchContainer;
}

async function breakdownEscrow(data, brand, partner_id, partner_key, access_token, shop_id) {
    const HOST = "https://partner.shopeemobile.com";
    const PATH = "/api/v2/payment/get_escrow_detail_batch";

    try {
        let escrowBreakdown = [];
        for(let i=0; i<data.length; i++) {

            const timestamp = Math.floor(Date.now() / 1000);
            const baseString = `${partner_id}${PATH}${timestamp}${access_token}${shop_id}`;
            const sign = crypto.createHmac('sha256', partner_key)
                .update(baseString)
                .digest('hex');
            
            const params = new URLSearchParams({
                partner_id: partner_id,
                timestamp,
                access_token: access_token,
                shop_id: shop_id,
                sign,
            });

            const fullUrl = `${HOST}${PATH}?${params.toString()}`;
            console.log("Hitting withdrawal URL: ", fullUrl, "on batch: ", i);

            console.log("Data[i]: ", data[i]);

            const response = await axios.post(fullUrl, {
                "order_sn_list": data[i]
            });

            let escrowDetailList = response.data.response;

            escrowDetailList.forEach(e => {
                let obj = {
                    "No_Pesanan": e.escrow_detail.order_sn,
                    "Harga_Asli_Produk": e.escrow_detail.order_income.order_original_price,
                    "Total_Diskon_Produk": e.escrow_detail.order_income.order_seller_discount,
                    "Diskon_Produk_Dari_Shopee": e.escrow_detail.order_income.shopee_discount,
                    "Diskon_Voucher_Ditanggung_Penjual": e.escrow_detail.order_income.voucher_from_seller,
                    "Biaya_Komisi_AMS": e.escrow_detail.order_income.order_ams_commission_fee,
                    "Biaya_Administrasi_with_PPN_11": e.escrow_detail.order_income.commission_fee,
                    "Biaya_Layanan": e.escrow_detail.order_income.service_fee,
                    "Biaya_Proses_Pesanan": e.escrow_detail.order_income.seller_order_processing_fee,
                    "Total_Penghasilan": e.escrow_detail.order_income.escrow_amount,
                    "process_dttm": new Date(Date.now() + 7 * 60 * 60 * 1000).toISOString().replace('T', ' ').substring(0, 19)
                }
                escrowBreakdown.push(obj);
            });
        }
        await mergeData(escrowBreakdown, brand);
    } catch (e) {
        console.error("[SHOPEE-WITHDRAWAL] Error getting ESCROW DETAIL BATCH: ", brand);
        console.error(e);
    }
}

const brandTables = {
    "Chess": "chess_finance",
    "Cleviant": "cleviant_finance",
    "Dr.Jou": "dr_jou_finance",
    "Evoke": "evoke_finance",
    "G-Belle": "gbelle_finance",
    "Ivy & Lily": "ivy_lily_finance",
    "Naruko": "naruko_finance",
    "Miss Daisy": "miss_daisy_finance",
    "Mirae": "mirae_finance",
    "Mamaway": "mamaway_finance",
    "Mosseru": "mosseru_finance",
    "Nutri & Beyond": "nutri_beyond_finance",
    "Past Nine": "past_nine_finance",
    "Polynia": "polynia_finance",
    "SH-RD": "shrd_finance",
    "Swissvita": "swissvita_finance",
    "Eileen Grace": "eileen_grace_finance",
    "Relove": "relove_finance",
    "Joey & Roo": "joey_roo_finance",
    "Enchante": "enchante_finance",
    "Rocketindo Shop": "pinkrocket_finance",
}

async function mergeData(data, brand) {
    console.log("[SHOPEE-WITHDRAWAL] Start merging for brand: ", brand);
    const tableName = brandTables[brand];
    const bigquery = new BigQuery();
    const datasetId = 'shopee_api';

    try {
        console.log("[SHOPEE-WITHDRAWAL] Data before merging. First two: ");
        console.log(data.slice(0, 2));

        const incomingOrderSNs = data.map(row => `'${row.No_Pesanan}'`).join(",");
        const query = `
            SELECT No_Pesanan 
            FROM \`${bigquery.projectId}.${datasetId}.${tableName}\`
            WHERE No_Pesanan IN (${incomingOrderSNs})
        `;
        const [existingRows] = await bigquery.query({ query });
        
        const existingIds = new Set(existingRows.map(row => row.No_Pesanan));
        console.log(`[SHOPEE-WITHDRAWAL] Found ${existingIds.size} duplicates in BigQuery.`);

        const recordsToInsert = data.filter(row => !existingIds.has(row.No_Pesanan));

        if (recordsToInsert.length === 0) {
            console.log("[SHOPEE-WITHDRAWAL] All data already exists. Skipping insert.");
            return;
        }

        console.log(`[SHOPEE-WITHDRAWAL] Inserting ${recordsToInsert.length} new rows`);
        await bigquery
            .dataset(datasetId)
            .table(tableName)
            .insert(recordsToInsert);

        console.log(`[SHOPEE-WITHDRAWAL] Successfully inserted rows for ${brand}.`);
    } catch (e) {
        console.error("[SHOPEE-WITHDRAWAL] Error inserting FINANCE data on brand: ", brand);
        console.error(e);
    }
}

/*** 
TODO:
1. Should hit two endpoints: get_escrow_list and get_escrow_detail per order_sn
2. Transform the data with the required structure
***/
export async function mainDanaDilepas(brand, partner_id, partner_key, access_token, shop_id) {
    // const escrowContainer = await fetchDanaDilepas(brand, partner_id, partner_key, access_token, shop_id);
    // const twentyBatchContainer = await transformData(escrowContainer, brand);

    // if(twentyBatchContainer && twentyBatchContainer.length > 0) {
    //     await breakdownEscrow(twentyBatchContainer, brand, partner_id, partner_key, access_token, shop_id);
    // }

    console.log("[SHOPEE-WITHDRAWAL] Uncomment when required for backfill.")
}


```

## File: functions\fetchAdsProductLevel.js
```
import axios from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from './fetchAdsTotalBalance.js';
import { BigQuery } from '@google-cloud/bigquery';
import { backfillEndDate, backfillStartDate } from './fetchTiktokBasicAds.js';
const bigquery = new BigQuery();

export async function fetchAdsProductLevel(brand, partner_id, partner_key, access_token, shop_id) {
    let brandName = brand.toLowerCase().replace(/\s/g, "");
    let tableName = {
        "eileengrace": "eileen_grace_product_ads",
        "shrd": "shrd_product_ads",
        "missdaisy": "miss_daisy_product_ads",
        "polynia": "polynia_product_ads",
        "cleviant": "cleviant_product_ads",
        "mosseru": "mosseru_product_ads",
        "mirae": "mirae_product_ads",
        "mamaway": "mamaway_product_ads",
        "chess": "chess_product_ads", 
        "nutribeyond": "nutri_beyond_product_ads",
        "evoke": "evoke_product_ads",
        "drjou": "dr_jou_product_ads",
        "swissvita": "swissvita_product_ads",
        "gbelle": "gbelle_product_ads",
        "pastnine": "past_nine_product_ads",
        "ivylily": "ivy_lily_product_ads",
        "naruko": "naruko_product_ads"
    }

    const HOST = "https://partner.shopeemobile.com";

    // 1. Get campaign id list
    const campaignIdPath = "/api/v2/ads/get_product_level_campaign_id_list";

    // 2. Get product-level campaign daily performance
    const productCampaignPath = "/api/v2/ads/get_product_campaign_daily_performance";

    const yesterday = new Date(Date.now() - 86400000 * 1);
    const day = String(yesterday.getDate()).padStart(2, '0');
    const month = String(yesterday.getMonth() + 1).padStart(2, '0'); 
    const year = yesterday.getFullYear();
    const yesterdayString = `${day}-${month}-${year}`;
    
    // Get campaign id list per brand
    let campaignIdList = [];
    try {
        // Common parameters
        const timestamp = Math.floor(Date.now() / 1000);
        const baseString = `${partner_id}${campaignIdPath}${timestamp}${access_token}${shop_id}`;
        const sign = crypto.createHmac('sha256', partner_key)
            .update(baseString)
            .digest('hex');

        // Request parameters
        const params = new URLSearchParams({
            partner_id: partner_id,
            timestamp,
            access_token: access_token,
            shop_id: shop_id,
            sign,
        });

        const fullUrl = `${HOST}${campaignIdPath}?${params.toString()}`;
        console.log(`[SHOPEE-PRODUCT] Hitting Campaign Id List for ${brand}: `, fullUrl);

        const response = await axios.get(fullUrl, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if(response && response?.data && response?.data?.response) {
            console.log("[SHOPEE-PRODUCT] Campaign Id List for brand: ", brand, "\n");
            // console.log(response.data.response.campaign_list);

            campaignIdList = campaignIdList.concat(response.data.response.campaign_list);
        }

    } catch (e) {
        console.error(`[SHOPEE-PRODUCT] Error fetch campaign id list on ${brand}\n`);
        console.error(e);
    }

    console.log("Campaign Id List on brand: ", brand, "\n");
    console.log(campaignIdList);
    console.log("\n");
    
    let campaignPerformanceList = []

    if(campaignIdList.length > 0) {

        const idList = campaignIdList.map(c => String(c.campaign_id));
        const css = idList.join(',');


        try {
            console.log('[SHOPEE-PRODUCT] Comma Separated Campaign Ids: ', css);

            let startDate = new Date(backfillStartDate);
            let endDate = new Date(backfillEndDate);

            while(startDate <= endDate) {
                
                const timestamp = Math.floor(Date.now() / 1000);
                const baseString = `${partner_id}${productCampaignPath}${timestamp}${access_token}${shop_id}`;
                const sign = crypto.createHmac('sha256', partner_key)
                .update(baseString)
                .digest('hex');
                
                const stYear = startDate.getFullYear();
                const stMont = String(startDate.getMonth() + 1).padStart(2, '0');
                const stDay = String(startDate.getDate()).padStart(2, '0');
                const stString = `${stDay}-${stMont}-${stYear}`;

                const params = new URLSearchParams({
                    partner_id: partner_id,
                    timestamp,
                    access_token: access_token,
                    shop_id: shop_id,
                    sign,
                    start_date: stString,
                    end_date: stString,
                    campaign_id_list: css
                });
    
                const fullUrl = `${HOST}${productCampaignPath}?${params.toString()}`;
                console.log(`[SHOPEE-PRODUCT] Hitting Product-level Campaign for ${brand}: `, fullUrl);
    
                const response = await axios.get(fullUrl, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
    
                if(response && response.data && response.data.response) {

                    let campaignList = response.data.response.campaign_list;
                    campaignList.forEach(c => {
                        if(c.metrics_list[0].expense > 0) {
                            let obj = {
                                date: c.metrics_list[0].date,
                                prod_name: c.ad_name,
                                expense: c.metrics_list[0].expense,
                            }
                            campaignPerformanceList.push(obj);
                        }
                    })
                }

                startDate.setDate(startDate.getDate() + 1);
            }

        } catch (e) {
            console.error(`[SHOPEE-PRODUCT] Error fetch product-level campaign expenses on brand ${brand}\n`);
            console.error(e);
        }

    }


    // Process and transform data

    const totalExpense = await fetchAdsTotalBalance(brand, partner_id, partner_key, access_token, shop_id);

    console.log("PERIOD: 2025-11-01 to 2025-11-26")
    console.log("Campaign Performance List on brand: ", brand, "\n");
    console.log("Total Expense\n");

    let totalExpenseMerged = []
    totalExpense.forEach(t => {
        let obj = {
            date: t.date,
            prod_name: "Iklan Toko",
            expense: t.expense,
        }
        totalExpenseMerged.push(obj);
    });

    let productExpenseMap = {};
    campaignPerformanceList.forEach(item => {
        if (!productExpenseMap[item.date]) {
            productExpenseMap[item.date] = 0;
        }
        productExpenseMap[item.date] += item.expense;
    });

    let newTotalExpenseMerged = [];
    totalExpenseMerged.forEach(t => {
        const totalProductExpenseOnDate = productExpenseMap[t.date] || 0;
        const actualIklanTokoExpense = t.expense - totalProductExpenseOnDate;

        let obj = {
            date: t.date,
            prod_name: "Iklan Toko",
            expense: actualIklanTokoExpense > 0 ? actualIklanTokoExpense : 0, 
        }
        newTotalExpenseMerged.push(obj);
    });

    let dataToMerge = campaignPerformanceList.concat(newTotalExpenseMerged);

    await mergeProductShopeeAds(tableName[brandName], dataToMerge);
}

async function mergeProductShopeeAds(tableName, data) {
    console.log(`[PRODUCT-SHOPEE] Merging to ${tableName}`)
    // data.forEach(d => {
    //     console.log(`Date: ${d.date}. Prod Name: ${d.prod_name}. Expense: ${d.expense}`);
    // })

    try {
        const datasetId = "shopee_api";

        for(const d of data) {

            const checkQuery = `
                SELECT date 
                FROM \`${datasetId}.${tableName}\` 
                WHERE date = @date 
                AND prod_name = @prod_name
            `;
            
            const options = {
                query: checkQuery,
                params: {
                    date: d.date.split('-').reverse().join('-'),
                    prod_name: d.prod_name,
                }
            };

            const [existingRows] = await bigquery.query(options);

            if (existingRows.length > 0) {
                continue; // Skip this insertion
            }

            await bigquery
                .dataset(datasetId)
                .table(tableName)
                .insert({
                    date: d.date.split('-').reverse().join('-'),
                    prod_name: d.prod_name,
                    cost: parseInt(d.expense),
                    process_dttm: new Date(Date.now() + 7 * 60 * 60 * 1000).toISOString().replace('T', ' ').substring(0, 19)
                });
        }
        console.log(`[PRODUCT-SHOPEE] Successfully processed ${data.length} row(s) for ${tableName}`);
    } catch (e) {
        console.log(`Error merging product-level shopee ads on ${tableName}`);
        console.log(e);
    }
} 
```

## File: functions\fetchAdsTotalBalance.js
```
import axios from 'axios';
import crypto from 'crypto';
import { BigQuery } from '@google-cloud/bigquery';
const bigquery = new BigQuery();

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

export async function fetchAdsTotalBalance(brand, partner_id, partner_key, accessToken, shop_id) {
    console.log("Fetch Ads Total Balance of brand: ", brand);
    
    const HOST = "https://partner.shopeemobile.com"
    const PATH = "/api/v2/ads/get_all_cpc_ads_daily_performance";

    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${partner_id}${PATH}${timestamp}${accessToken}${shop_id}`;
    const sign = crypto.createHmac('sha256', partner_key)
        .update(baseString)
        .digest('hex');

    const yesterday = new Date(Date.now() - 86400000 * 1);
    const day = String(yesterday.getDate()).padStart(2, '0');
    const month = String(yesterday.getMonth() + 1).padStart(2, '0'); 
    const year = yesterday.getFullYear();
    const yesterdayString = `${day}-${month}-${year}`;
    
    const params = new URLSearchParams({
        partner_id: partner_id,
        timestamp,
        access_token: accessToken,
        shop_id: shop_id,
        sign,
        start_date: yesterdayString,
        end_date: yesterdayString
    });

    const fullUrl = `${HOST}${PATH}?${params.toString()}`;
    console.log(`Hitting Ads Total Balance for ${brand}: `, fullUrl);

    let totalExpense = [];

    let retries = 3;
    let success = false;

    while(!success && retries > 0) {
        try {
            const response = await axios.get(fullUrl, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
    
            if(response && response.data.response) {
                // console.log(`${brand} Ads Total Balance: ${response.data.response[0].expense} on ${response.data.response[0].date}`);
                
                success = true;

                let responseList = response.data.response;
                responseList.forEach(r => {
                    if(r.expense > 0) {
                        totalExpense.push(r);
                    }
                })
                // return totalExpense;
                // await submitData(brand, response.data.response[0].expense, response.data.response[0].date);
                await submitData(brand, totalExpense);
            } else {
                console.log("[SHOPEE] response ads does not exist: ", brand);
                
                retries -= 1;
                if(retries > 0) await sleep(5000);
            }
        } catch (e) {
            console.log(`Error fetching total balance for ${brand}: ${e}`);
        }
    }
}

async function submitData(brand, expenses) {
    let tableName = ""
    
    if(brand == "Eileen Grace") {
        tableName = "eileen_grace_ads_spending";
    } else if(brand == "Miss Daisy") {
        tableName = "miss_daisy_ads_spending";
    } else if(brand == "SH-RD") {
        tableName = "shrd_ads_spending";
    } else if(brand == "Cleviant") {
        tableName = "cleviant_ads_spending";
    } else if(brand == "Mosseru") {
        tableName = "mosseru_ads_spending";
    } else if(brand == "Dr.Jou") {
        tableName = "drjou_ads_spending";
    } else if(brand == "G-Belle") {
        tableName = "gbelle_ads_spending";
    } else if(brand == "Ivy & Lily") {
        tableName = "ivylily_ads_spending"
    } else if(brand == "Evoke") {
        tableName = "evoke_ads_spending";
    } else if(brand == "Mamaway") {
        tableName = "mmw_ads_spending";
    } else if(brand == "Chess") {
        tableName = "chess_ads_spending";
    } else if(brand == "Swissvita") {
        tableName = "swissvita_ads_spending";
    } else if(brand == "Past Nine") {
        tableName = "pastnine_ads_spending";
    } else if(brand == "Nutri & Beyond") {
        tableName = "nutribeyond_ads_spending";
    } else if(brand == "Polynia") {
        tableName = "polynia_ads_spending";
    } else if(brand == "Mirae") {
        tableName = "mirae_ads_spending";
    } else if(brand == "Naruko") {
        tableName = "naruko_ads_spending";
    } else if(brand == "Relove") {
        tableName = "relove_ads_spending";
    } else if(brand == "Joey Roo") {
        tableName = "joey_roo_ads_spending";
    } else if(brand == "Enchante") {
        tableName = "enchante_ads_spending";
    }
 
    const datasetId = 'shopee_api';

    console.log(`[SHOPEE] Ads Total Balance on ${brand}`);

    
    try {

        for(const expense of expenses) {
            const query = `
                SELECT Tanggal_Dibuat
                FROM \`${datasetId}.${tableName}\`
                WHERE Tanggal_Dibuat = @date
            `;
            const options = {
                query,
                params: { 
                    date: expense.date 
                }
            }
            const [rows] = await bigquery.query(options);
    
            if(rows.length > 0) {
                console.log("Row already exists");
                continue;
            }
    
            await bigquery
                .dataset(datasetId)
                .table(tableName)
                .insert({
                    Tanggal_Dibuat: expense.date,
                    Spending: expense.expense,
                });
        }

        console.log(`Successfully written ads spending to ${brand} table.`)
    } catch (e) {
        console.error(`Error inserting ads spending on ${brand}: ${e}`);
    }
}
```

## File: functions\fetchAffiliateSpending.js
```
import axios from 'axios';
import crypto from 'crypto';

export async function fetchAffiliateSpending(brand, PARTNER_ID, PARTNER_KEY, ACCESS_TOKEN, SHOP_ID) {
    console.log("Fetch Affiliate Spending of brand: ", brand);

    const HOST = "https://partner.shopeemobile.com";
    const PATH = "/api/v2/ams/get_managed_affiliate_list";

    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${PATH}${timestamp}${ACCESS_TOKEN}${SHOP_ID}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');

    const params = new URLSearchParams({
        partner_id: PARTNER_ID, 
        timestamp,
        access_token: ACCESS_TOKEN,
        shop_id: SHOP_ID,
        sign,
        page_no: 1,
        page_size: 20
    });

    const fullUrl = `${HOST}${PATH}?${params.toString()}`;
    console.log(`Hitting Affiliate Spending for ${brand}: ${fullUrl}`);

    try {
        const response = await axios.get(fullUrl, {
            headers: {
                'Content-Type': 'application/json'
            }
        })

        if(response && response.data.response) {
            console.log("[AFFILIATE] res affiliate spending eg: ", response.data.response.transaction_list);
        } else {
            console.error(response);
        }
    } catch (e) {
        console.error(`[AFFILIATE] Error fetching affiliate spending for ${brand}`);
        console.log(e);
    }
}
```

## File: functions\fetchGMVMaxSpending.js
```
import axios from 'axios';
import { BigQuery } from '@google-cloud/bigquery';
const bigquery = new BigQuery();

export function formatToDDMMYYYY(dateString) {
    // Expects input like "2025-11-12 00:00:00"
    const [datePart] = dateString.split(' ');
    const [year, month, day] = datePart.split('-');
    return `${day}-${month}-${year}`;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

export async function fetchGMVMaxSpending(brand, advertiser_id) {

    await sleep(1000);

    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yyyy = yesterday.getFullYear();
    const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
    const dd = String(yesterday.getDate()).padStart(2, '0');
    const yesterdayStr = `${yyyy}-${mm}-${dd}`;

    let access_token = process.env.TIKTOK_MARKETING_ACCESS_TOKEN;
    let brandName = brand.toLowerCase().replace(/\s/g, "");
    let tableName = `${brandName}_gmvmax`;
    
    let multiBrandAcc = {
        "mamaway": "7494499456018189063",
        "chess": "7494919612596259170", 
        "nutribeyond": "7496045913194138312",
        "evoke": "7495667268174318445",
        "drjou": "7495803189501659725",
        "swissvita": "7494835443584567449",
        "gbelle": "7495908629104331053",
        "pastnine": "7495997119882693518",
        "ivylily": "7496045415576275429",
        "naruko": "7496241553706617176"
    }
    if(
        brand == "Eileen Grace" ||
        brand == "SHRD" ||
        brand == "Miss Daisy" ||
        brand == "Polynia" ||
        brand == "Cleviant" ||
        brand == "Mosseru" ||
        brand == "Mirae"
    ) {
        console.log("Fetching single brand account");
        const url = 'https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/';
        const params = {
            advertiser_id: advertiser_id,
            service_type: 'AUCTION',
            report_type: 'TT_SHOP',
            data_level: 'AUCTION_ADVERTISER',
            dimensions: JSON.stringify(["advertiser_id", "country_code", "stat_time_day"]),
            metrics: JSON.stringify(["spend", "billed_cost"]),
            start_date: yesterdayStr,
            end_date: yesterdayStr,
            page: 1,
            page_size: 100
        };

        try {
            const response = await axios.get(url, {
                headers: {
                    'Access-Token': access_token
                },
                params
            });

            const costList = response.data.data.list;
            let processedCostList = [];

            costList.forEach(c => {
                if(c.metrics.spend !== "0") {
                    let costElement = {
                        "Tanggal_Dibuat": formatToDDMMYYYY(c.dimensions.stat_time_day),
                        "Spending": parseInt(c.metrics.spend)
                    }
                    processedCostList.push(costElement);
                }
            });

            if(processedCostList) {
                await mergeGMVMax(tableName, processedCostList);
            }
        } catch (e) {
            console.error("[SINGLE] Error fetching GMV Max Spending: ", e);
        }
    } else {
        console.log("Fetching multiple brand account: ", brandName);
        const url = 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/';
        const params = {
            advertiser_id,
            store_ids: JSON.stringify([multiBrandAcc[brandName]]),
            start_date: yesterdayStr,
            end_date: yesterdayStr,
            dimensions: JSON.stringify(["advertiser_id", "stat_time_day"]),
            metrics: JSON.stringify(["cost", "orders", "cost_per_order", "gross_revenue", "roi", "net_cost"]),
            page: 1,
            page_size: 1000
        }

        try {
            let success = false;
            let retries = 3;

            while(!success && retries > 0) {

                const response = await axios.get(url, {
                    headers: {
                        'Access-Token': access_token
                    },
                    params
                });
    
                if(response && response.data && response.data.data && response.data.data.list) {
                    success = true;
                    const costList = response.data.data.list;
                    let processedCostList = [];
        
                    costList.forEach(c => {
                        if(c.metrics.cost !== "0") {
                            let costElement = {
                                "Tanggal_Dibuat": formatToDDMMYYYY(c.dimensions.stat_time_day),
                                "Spending": parseInt(c.metrics.cost)
                            }
                            processedCostList.push(costElement);
                        }
                    });
        
                    if(processedCostList) {
                        // console.log(`[MULTI] Cost list to merge on ${brandName}\n`);
                        // console.log(processedCostList);
                        await mergeGMVMax(tableName, processedCostList);
                    }
                } else {
                    retries -= 1;
                    console.log(`[MULTI] Response does not exist on brand: ${brand}`)
                    if (retries > 0) await sleep(3000);
                }

            }
        } catch (e) {
            retries -= 1;
            console.error(`[MULTIPLE] Error getting store list on ${brandName}: ${e}, retries left: ${retries}`);
            if (retries > 0) await sleep(3000);
        }
    }
}

async function mergeGMVMax(tableName, costList) {
    const datasetId = "tiktok_api_us";
    console.log("\n");
    console.log("Table name: ", tableName);
    console.log("Cost length: ", costList.length);
    console.log("\n");

    if(tableName == "eileengrace_gmvmax") tableName = "eileen_grace_gmvmax";
    if(tableName == "missdaisy_gmvmax") tableName = "miss_daisy_gmvmax";

    try {
        if (!costList.length) return;

        const dates = costList.map(c => c.Tanggal_Dibuat);
        const query = `
            SELECT Tanggal_Dibuat
            FROM \`${datasetId}.${tableName}\`
            WHERE Tanggal_Dibuat IN UNNEST(@dates)
        `;
        const options = {
            query,
            params: { dates }
        };

        const [rows] = await bigquery.query(options);
        const existingDates = new Set(rows.map(r => r.Tanggal_Dibuat));
        const newRows = costList.filter(c => !existingDates.has(c.Tanggal_Dibuat));

        if (!newRows.length) {
            console.log("[BASIC] All rows already exist, nothing to insert.");
            return;
        }

        await bigquery
            .dataset(datasetId)
            .table(tableName)
            .insert(newRows)

        console.log(`Merged ${newRows.length} cost element to ${tableName} table`);
    } catch (e) {
        console.log(`Failed to merge to bigquery on ${tableName}: ${e}`);
    }
}
```

## File: functions\fetchLiveGMVMax.js
```
import axios from 'axios';
import { formatToDDMMYYYY } from './fetchGMVMaxSpending.js';
import { BigQuery } from '@google-cloud/bigquery';
import { backfillEndDate, backfillStartDate } from './fetchTiktokBasicAds.js';
const bigquery = new BigQuery();

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

export async function fetchLiveGMVMax(brand, advertiser_id, sleepValue=4000) {

    await sleep(sleepValue);

    console.log(`[LIVE] GMV MAX - ${brand}`);
    let access_token = process.env.TIKTOK_MARKETING_ACCESS_TOKEN;
    let brandName = brand.toLowerCase().replace(/\s/g, "");
    let tableName = `${brandName}_productgmvmax`;

    const yesterday = new Date();

    yesterday.setDate(yesterday.getDate() - 1);

    const yyyy = yesterday.getFullYear();
    const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
    const dd = String(yesterday.getDate()).padStart(2, '0');
    const yesterdayStr = `${yyyy}-${mm}-${dd}`;

    let storeIdAcc = {
        "eileengrace": "7494055813163943155",
        "shrd": "7494060372131481134",
        "missdaisy": "7494083757647759179",
        "polynia": "7494718012797651378",
        "cleviant": "7495299579063405468",
        "mosseru": "7495297011747293899",
        "mirae": "7495819231306943483",
        "mamaway": "7494499456018189063",
        "chess": "7494919612596259170", 
        "nutribeyond": "7496045913194138312",
        "evoke": "7495667268174318445",
        "drjou": "7495803189501659725",
        "swissvita": "7494835443584567449",
        "gbelle": "7495908629104331053",
        "pastnine": "7495997119882693518",
        "ivylily": "7496045415576275429",
        "naruko": "7496241553706617176",
        "rocketindoshop": "7495827950440450460",
        "relove": "7494271470068139382",
        "joeyroo": "7494266461991830655",
        "enchante": "7494271538671289804"
    }

    let success = false;
    let retries = 10;
    try {   

        while(!success && retries > 0) {

            const params = {
                advertiser_id: advertiser_id,
                store_ids: JSON.stringify([storeIdAcc[brandName]]),
                start_date: yesterdayStr,
                end_date: yesterdayStr,
                dimensions: JSON.stringify(["advertiser_id", "stat_time_day"]),
                metrics: JSON.stringify(["cost", "orders", "net_cost", "gross_revenue"]),
                filtering: JSON.stringify({ gmv_max_promotion_types: ["LIVE"] }),
                page: 1,
                page_size: 1000
            }

            const url = "https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/";
            const response = await axios.get(url, {
                headers: {
                    'Access-Token': access_token
                },
                params
            });

            console.log(`[LIVE] response on brand ${brandName}`);
            // console.log(response.data);

            if(response && response.data && response.data.data && response.data.data.list) {
                success = true;
                const costList = response.data.data.list;
                let processedCostList = [];

                costList.forEach(c => {
                    if(c.metrics.cost !== "0") {
                        let costElement = {
                            "date": c.dimensions.stat_time_day,
                            "lgmax_cost": parseInt(c.metrics.cost),
                            "lgmax_gmv": parseInt(c.metrics.gross_revenue)
                        }
                        processedCostList.push(costElement);
                    }
                });

                if(processedCostList) {
                    console.log(`[LIVE] ${brandName} PROCESSEDCOSTLIST EXISTS`);
                    return processedCostList;
                }
            } else {
                retries -= 1;
                console.log(`[LIVE] ${brandName} does not exist. Retries left: ${retries}`);
                console.log("[LIVE] Failed response: ", response?.data);
                if(retries > 0) await sleep(3000)
                else return [];
            }
        }
    } catch (e) {
        retries -= 1;
        console.log(`[LIVE] Error fetching Product GMV Max spending on ${brandName}: ${e}`)
        // --- ACTION: HARD WAIT ON RATE LIMIT ---
        if (e.response?.status === 429 || e.message.includes('40100')) {
             console.log("[PRODUCT] Hit Rate Limit. Sleeping 15s before retry...");
             await sleep(15000);
        } else {
             if(retries > 0) await sleep(5000);
        }

        // --- THE CRITICAL FIX ---
        // If we ran out of retries, THROW THE ERROR.
        // Do NOT let the function finish and return undefined.
        if (retries === 0) {
            throw new Error(`[STRICT MODE] Failed to fetch data for ${brand} after all retries. Failing job to trigger BullMQ backoff.`);
        }
    }
}

async function mergeProductGMVMax(brand, costList) {
    const datasetId = "tiktok_api_us";

    console.log("\n");
    console.log("[LGMVMAX] Data: ", brand);
    console.log("Data: ", costList);
    console.log("\n");
}
```

## File: functions\fetchPGMVMaxBreakdown.js
```
import axios from 'axios';
import { BigQuery } from '@google-cloud/bigquery';
import { isRedisCluster } from 'bullmq';
import { backfillEndDate, backfillStartDate } from './fetchTiktokBasicAds.js';
const bigquery = new BigQuery();
let access_token = process.env.TIKTOK_MARKETING_ACCESS_TOKEN;

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

let storeIdAcc = {
    "eileengrace": {
        store_id: "7494055813163943155",
        table_name: "eileen_grace_pgmax"
    },
    "shrd": {
        store_id: "7494060372131481134",
        table_name: "shrd_pgmax"
    },
    "missdaisy": {
        store_id: "7494083757647759179",
        table_name: "miss_daisy_pgmax"
    },
    "polynia": {
        store_id: "7494718012797651378",
        table_name: "polynia_pgmax"
    },
    "cleviant": {
        store_id: "7495299579063405468",
        table_name: "cleviant_pgmax"
    },
    "mosseru": {
        store_id: "7495297011747293899",
        table_name: "mosseru_pgmax",
    },
    "mirae": {
        store_id: "7495819231306943483",
        table_name: "mirae_pgmax"
    },
    "mamaway": {
        store_id: "7494499456018189063",
        table_name: "mamaway_pgmax"
    },
    "chess": {
        store_id: "7494919612596259170",
        table_name: "chess_pgmax"
    }, 
    "nutribeyond": {
        store_id: "7496045913194138312",
        table_name: "nutri_beyond_pgmax"
    },
    "evoke": {
        store_id: "7495667268174318445",
        table_name: "evoke_pgmax"
    },
    "drjou": {
        store_id: "7495803189501659725",
        table_name: "dr_jou_pgmax"
    },
    "swissvita": {
        store_id: "7494835443584567449",
        table_name: "swissvita_pgmax"
    },
    "gbelle": {
        store_id: "7495908629104331053",
        table_name: "gbelle_pgmax"
    },
    "pastnine": {
        store_id: "7495997119882693518",
        table_name: "past_nine_pgmax"
    },
    "ivylily": {
        store_id: "7496045415576275429",
        table_name: "ivy_lily_pgmax"
    },
    "naruko": {
        store_id: "7496241553706617176",
        table_name: "naruko_pgmax"
    },
    "rocketindoshop": {
        store_id: "7495827950440450460",
        table_name: "rocketindo_shop_pgmax"
    },
    "relove": {
        store_id: "7494271470068139382",
        table_name: "relove_pgmax"
    },
    "joeyroo": {
        store_id: "7494266461991830655",
        table_name: "joey_roo_pgmax"
    },
    "enchante": {
        store_id: "7494271538671289804",
        table_name: "enchante_pgmax"
    }
}    

export async function fetchPGMVMaxBreakdown(brand, advertiser_id) {
    // Get campaign_ids on store's Product GMV Max campaigns
    // request parameter: advertiser_id, store_ids (per brand), gmv_max_promotion_types: ["PRODUCT_GMV_MAX"]
    // expected response: campaign_id, campaign_name

    await sleep(10000);

    let brandName = brand.toLowerCase().replace(/\s/g, "");


    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yyyy = yesterday.getFullYear();
    const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
    const dd = String(yesterday.getDate()).padStart(2, '0');
    const yesterdayStr = `${yyyy}-${mm}-${dd}`;

    const hh = String(yesterday.getHours()).padStart(2, '0'); // Hours (00-23)
    const mi = String(yesterday.getMinutes()).padStart(2, '0'); // Minutes (00-59)
    const ss = String(yesterday.getSeconds()).padStart(2, '0'); // Seconds (00-59)

    // Combine all parts into the desired string format (e.g., YYYY-MM-DD HH:MI:SS)
    const yesterdayStrWithTime = `${yyyy}-${mm}-${dd} ${hh}:${mi}:${ss}`;

    try {
        const params = {
            advertiser_id: advertiser_id,
            fields: JSON.stringify(["campaign_id", "campaign_name"]),
            filtering: JSON.stringify({ 
                gmv_max_promotion_types: ["PRODUCT_GMV_MAX"],
                store_ids: [storeIdAcc[brandName].store_id],
                // primary_status: "STATUS_DELIVERY_OK",
            }),
            // creation_filter_start_time: "2025-01-01 00:00:01",
            // creation_filter_end_time: yesterdayStrWithTime,
            page: 1, 
            page_size: 100
        }

        const url = "https://business-api.tiktok.com/open_api/v1.3/gmv_max/campaign/get/";
        const response = await axios.get(url, {
            headers: {
                'Access-Token': access_token
            },
            params
        });

        let campaignIdsAsParam = [];
        if(response && response.data && response.data.data && response.data.data.list) {
            // console.log(response?.data?.data?.list);

            let campaignIdList = response.data.data.list;
            campaignIdList.forEach((c) => {
                campaignIdsAsParam.push({
                    campaign_id: c.campaign_id,
                    campaign_name: c.campaign_name
                });
            })
        } else {
            console.log(`[PRODUCT-BREAKDOWN] response does not exist on ${brand}`);
        }

        
        if(campaignIdsAsParam.length > 0) {
            console.log(`🥰 Campaign Id & Name on brand ${brand}\n`);
            // console.log(campaignIdsAsParam);
            // console.log("\n");

            let breakdownCostList = [];
            for(const c of campaignIdsAsParam) {

                let success = false;
                let retries = 10;
                while(!success && retries > 0) {
                    try {
                        const params = {
                            advertiser_id: advertiser_id,
                            store_ids: JSON.stringify([storeIdAcc[brandName].store_id]),
                            metrics: JSON.stringify(["product_name", "item_group_id", "cost", "gross_revenue"]),
                            dimensions: JSON.stringify(["item_group_id", "stat_time_day"]),
                            filtering: JSON.stringify({
                                campaign_ids: [c.campaign_id],
                            }),
                            start_date: yesterdayStr,
                            end_date: yesterdayStr,
                            page: 1,
                            page_size: 1000
                        }
                        const url = "https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/";
                        const response = await axios.get(url, {
                            headers: {
                                'Access-Token': access_token
                            },
                            params
                        });

                        await sleep(3000);
                        
                        // console.log(`🔥 [PRODUCT-BREAKDOWN] raw response product-level metrics: `);
                        // console.log(response);
        
                        if(response && response.data && response.data.data && response.data.data.list) {

                            success = true;
                            
                            if(brand == "SHRD") {
                                console.log(`🔥 [PRODUCT-BREAKDOWN] product-level metrics response on ${brand} and Campaign Name: ${c.campaign_name} and ID: ${c.campaign_id}`);
                                // console.log(response.data.data.list);
                            }

                            // let sumCost = 0;
                            let productLevelList = response.data.data.list;
                            
                            productLevelList.forEach(p => {
                                if(p.metrics.cost !== "0") {
                                    let obj = {
                                        date: p.dimensions.stat_time_day.substring(0, 10),
                                        campaign_name: c.campaign_name,
                                        prod_id: p.metrics.item_group_id,
                                        prod_name: p.metrics.product_name,
                                        cost: parseInt(p.metrics.cost),
                                        gmv: parseInt(p.metrics.gross_revenue),
                                        process_dttm: new Date(Date.now() + 7 * 60 * 60 * 1000).toISOString().replace('T', ' ').substring(0, 19)
                                    }
                                    // sumCost += p.metrics.cost;
                                    breakdownCostList.push(obj);
                                }
                            });
                        } else {
                            retries -= 1;
                            console.log(`🥶 [PRODUCT-BREAKDOWN] Failed response on ${brand}. Retries left: ${retries}`);
                            // console.log(response?.data);

                            if(retries > 0) await sleep(25000);
                        }
                    } catch (e) {
                        console.log("🤯 [PRODUCT-BREAKDOWN] Error getting product-level metrics on: ", brand, "error: ", e);
                    }
                }
            }

            if(breakdownCostList.length > 0) {
                console.log(`🔥 [PRODUCT-BREAKDOWN] Breakdown Cost List on ${brand}`);
                // console.log(breakdownCostList);
                console.log("Breakdown Cost List length: ", breakdownCostList.length);

                // await mergeBreakdown(storeIdAcc[brandName].table_name, breakdownCostList);

                await preprocessData(advertiser_id, brandName, storeIdAcc[brandName].table_name, breakdownCostList, campaignIdsAsParam);
            }
        }

    } catch (e) {
        console.log("🤯 [PRODUCT-BREAKDOWN] Error getting campaign_id on: ", brand, "error: ", e);
    }
}

async function preprocessData(advertiser_id, brandName, tableName, dataReference, campaignIdList) {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yyyy = yesterday.getFullYear();
    const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
    const dd = String(yesterday.getDate()).padStart(2, '0');
    const yesterdayStr = `${yyyy}-${mm}-${dd}`;
    
    let processedData = dataReference;
    console.log("PREPROCESS DATA: ", tableName);

    let campaignMetricsList = [];
    
    for(const c of campaignIdList) {

        try {
            const params = {
                advertiser_id: advertiser_id,
                store_ids: JSON.stringify([storeIdAcc[brandName].store_id]),
                metrics: JSON.stringify(["campaign_id", "campaign_name", "cost"]),
                dimensions: JSON.stringify(["campaign_id", "stat_time_day"]),
                filtering: JSON.stringify({
                    gmv_max_promotion_types: ["PRODUCT"],
                    campaign_ids: [c.campaign_id]
                }),
                start_date: yesterdayStr,
                end_date: yesterdayStr,
                page: 1,
                page_size: 1000
            }
            const url = "https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/";
            const response = await axios.get(url, {
                headers: {
                    'Access-Token': access_token
                },
                params
            });
    
            if(response && response.data && response.data.data && response.data.data.list) {
                const refList = response.data.data.list;
                refList.forEach(r => {
                    let obj = {
                        date: r.dimensions.stat_time_day.substring(0, 10),
                        campaign_id: r.metrics.campaign_id,
                        campaign_name: r.metrics.campaign_name,
                        cost: parseInt(r.metrics.cost),
                    }
                    campaignMetricsList.push(obj);
                })
            }
        } catch (e) {
            console.log(`PREPROCESS ERROR on brand ${brandName}`);
            console.log(e);
        }
    }

    // console.log(`CAMPAIGN METRICS LIST ON ${tableName}\n`);
    // campaignMetricsList.forEach(c => console.log(c));
    // console.log("\n")
    
    // console.log(`PRODUCT METRICS LIST ON ${tableName}`);
    // dataReference.forEach(d => console.log(d));
    // console.log("\n");

    campaignMetricsList.forEach(camp => {
        const cName = camp.campaign_name;
        const cDate = camp.date; // Get the specific date for this campaign entry
        const campaignTotalCost = camp.cost;
        
        // --- UPDATED: Filter by Campaign Name AND Date ---
        let productsInCampaign = processedData.filter(p => p.campaign_name === cName && p.date === cDate);

        if(productsInCampaign.length > 0) {
            
            let productSumCost = productsInCampaign.reduce((sum, p) => sum + p.cost, 0);
            let diff = campaignTotalCost - productSumCost;

            if (Math.abs(diff) > 1000) { 
                console.warn(`⚠️ [MISMATCH] Date: ${cDate} | Campaign: "${cName}" | Camp Cost: ${campaignTotalCost} | Prod Sum: ${productSumCost} | Diff: ${diff}`);
                
                let highestCostProduct = productsInCampaign.reduce((prev, current) => {
                    return (prev.cost > current.cost) ? prev : current;
                });
                
                highestCostProduct.cost += diff;        
                console.log(`   > Adjusted "${highestCostProduct.prod_name}". New Cost: ${highestCostProduct.cost}\n`);
            
            } else {
                // console.log(`✅ [MATCH] Date: ${cDate} | Campaign: "${cName}" is balanced.`);
            }
        }
    });
    // 1. Get sum of all products' cost in a campaign on a given date.
    // const productCostMap = dataReference.reduce((acc, curr) => {
    //     const cName = curr.campaign_name;
    //     const pCost = parseInt(curr.cost) || 0;

    //     if (!acc[cName]) {
    //         acc[cName] = 0;
    //     }
    //     acc[cName] += pCost;
    //     return acc;
    // }, {});

    // campaignMetricsList.forEach(camp => {
    //     const cName = camp.campaign_name;
    //     const campaignTotalCost = camp.cost;
        
    //     let productSumCost = productCostMap[cName] || 0;

    //     const diff = Math.abs(campaignTotalCost - productSumCost);

    //     // We allow a very small epsilon for floating point differences, 
    //     // or check strict inequality if your data is perfectly clean.
    //     if (diff > 1000) { 
    //         console.warn(`⚠️ [MISMATCH DETECTED] Campaign: "${cName}"`);
    //         console.warn(`   > Campaign Level Cost: ${campaignTotalCost}`);
    //         console.warn(`   > Sum of Products Cost: ${productSumCost}`);
    //         console.warn(`   > Difference: ${diff.toFixed(4)}\n`);
    //     } else {
    //         console.log(`✅ [MATCH] Campaign: "${cName}" is balanced (Cost: ${campaignTotalCost})`);
    //     }
    // });

    await mergeBreakdown(tableName, processedData);
}

async function mergeBreakdown(tableName, data) {
    console.log("🥶 Merging to table: ", tableName);
    console.log("🥶 Data: \n");
    console.log(data.length);

    const datasetId = "tiktok_api_us";

    try {
        for(const d of data) {
            
            const checkQuery = `
                SELECT date 
                FROM \`${datasetId}.${tableName}\` 
                WHERE date = @date 
                AND campaign_name = @campaign_name
                AND prod_id = @prod_id
            `;
            
            const options = {
                query: checkQuery,
                params: {
                    date: d.date,
                    campaign_name: d.campaign_name,
                    prod_id: d.prod_id
                }
            };

            const [existingRows] = await bigquery.query(options);

            if (existingRows.length > 0) {
                continue; // Skip this insertion
            }

            await bigquery
                .dataset(datasetId)
                .table(tableName)
                .insert({
                    date: d.date,
                    campaign_name: d.campaign_name, 
                    prod_id: d.prod_id,
                    prod_name: d.prod_name,
                    cost: parseInt(d.cost),
                    gmv: parseInt(d.gmv),
                    process_dttm: new Date(Date.now() + 7 * 60 * 60 * 1000).toISOString().replace('T', ' ').substring(0, 19)
                });
        }
        console.log(`[MERGE-BREAKDOWN] Successfully processed ${data.length} row(s) for ${tableName}`);
    } catch (e) {
        console.error(`🤯 Error merge breakdown data on ${tableName}`)
    }
}
```

## File: functions\fetchProductGMVMax.js
```
import axios from 'axios';
import { formatToDDMMYYYY } from './fetchGMVMaxSpending.js';
import { BigQuery } from '@google-cloud/bigquery';
import { backfillEndDate, backfillStartDate } from './fetchTiktokBasicAds.js';
const bigquery = new BigQuery();

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

export async function fetchProductGMVMax(brand, advertiser_id, sleepValue=5000) {

    await sleep(sleepValue);

    console.log(`[PRODUCT] GMV MAX - ${brand}`);
    let access_token = process.env.TIKTOK_MARKETING_ACCESS_TOKEN;
    let brandName = brand.toLowerCase().replace(/\s/g, "");

    const yesterday = new Date();

    yesterday.setDate(yesterday.getDate() - 1);

    const yyyy = yesterday.getFullYear();
    const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
    const dd = String(yesterday.getDate()).padStart(2, '0');
    const yesterdayStr = `${yyyy}-${mm}-${dd}`;

    let storeIdAcc = {
        "eileengrace": "7494055813163943155",
        "shrd": "7494060372131481134",
        "missdaisy": "7494083757647759179",
        "polynia": "7494718012797651378",
        "cleviant": "7495299579063405468",
        "mosseru": "7495297011747293899",
        "mirae": "7495819231306943483",
        "mamaway": "7494499456018189063",
        "chess": "7494919612596259170", 
        "nutribeyond": "7496045913194138312",
        "evoke": "7495667268174318445",
        "drjou": "7495803189501659725",
        "swissvita": "7494835443584567449",
        "gbelle": "7495908629104331053",
        "pastnine": "7495997119882693518",
        "ivylily": "7496045415576275429",
        "naruko": "7496241553706617176",
        "rocketindoshop": "7495827950440450460",
        "relove": "7494271470068139382",
        "joeyroo": "7494266461991830655",
        "enchante": "7494271538671289804"
    }

    let success = false;
    let retries = 10;
    try {   

        while(!success && retries > 0) {

            const params = {
                advertiser_id: advertiser_id,
                store_ids: JSON.stringify([storeIdAcc[brandName]]),
                start_date: yesterdayStr,
                end_date: yesterdayStr,
                dimensions: JSON.stringify(["advertiser_id", "stat_time_day"]),
                metrics: JSON.stringify(["cost", "orders", "net_cost", "gross_revenue"]),
                filtering: JSON.stringify({ gmv_max_promotion_types: ["PRODUCT"] }),
                page: 1,
                page_size: 1000
            }

            const url = "https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/";
            const response = await axios.get(url, {
                headers: {
                    'Access-Token': access_token
                },
                params
            });

            console.log(`[PRODUCT] response on brand ${brandName}`);

            if(response && response.data && response.data.data && response.data.data.list) {
                success = true;
                const costList = response.data.data.list;
                let processedCostList = [];

                costList.forEach(c => {
                    if(c.metrics.cost !== "0") {
                        let costElement = {
                            "date": c.dimensions.stat_time_day,
                            "pgmax_cost": parseInt(c.metrics.cost),
                            "pgmax_gmv": parseInt(c.metrics.gross_revenue)
                        }
                        processedCostList.push(costElement);
                    }
                });

                if(processedCostList) {
                    console.log(`[PRODUCT] ${brandName} PROCESSEDCOSTLIST EXISTS`);
                    // await mergeProductGMVMax(brand, processedCostList);
                    return processedCostList;
                }
            } else {
                retries -= 1;
                console.log(`[PRODUCT] ${brandName} does not exist. Retries left: ${retries}`);
                console.log("[PRODUCT] Failed response: ", response?.data);
                if(retries > 0) await sleep(sleepValue)
                else return [];
            }
        }
    } catch (e) {
        retries -= 1;
        console.log(`[PRODUCT] Error fetching Product GMV Max spending on ${brandName}: ${e}`)

        // --- ACTION: HARD WAIT ON RATE LIMIT ---
        if (e.response?.status === 429 || e.message.includes('40100')) {
             console.log("[PRODUCT] Hit Rate Limit. Sleeping 15s before retry...");
             await sleep(15000);
        } else {
             if(retries > 0) await sleep(5000);
        }

        // --- THE CRITICAL FIX ---
        // If we ran out of retries, THROW THE ERROR.
        // Do NOT let the function finish and return undefined.
        if (retries === 0) {
            throw new Error(`[STRICT MODE] Failed to fetch data for ${brand} after all retries. Failing job to trigger BullMQ backoff.`);
        }
    }
}

async function mergeProductGMVMax(brand, costList) {
    const datasetId = "tiktok_api_us";

    console.log("\n");
    console.log("[PGMVMAX] Data: ", brand);
    console.log("Data: ", costList);
    console.log("\n");
}
```

## File: functions\fetchTiktokBasicAds.js
```
import axios from 'axios';
import { formatToDDMMYYYY } from './fetchGMVMaxSpending.js';
import { BigQuery } from '@google-cloud/bigquery';
const bigquery = new BigQuery();

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const yesterday = new Date();
yesterday.setDate(yesterday.getDate() - 1);
const yyyy = yesterday.getFullYear();
const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
const dd = String(yesterday.getDate()).padStart(2, '0');
const yesterdayStr = `${yyyy}-${mm}-${dd}`;

// For backfill only. Not for production.
export let backfillStartDate = "2025-09-01";
export let backfillEndDate = "2025-09-26";

// export let backfillStartDate = yesterdayStr;
// export let backfillEndDate = yesterdayStr;

export async function fetchTiktokBasicAds(brand, advertiser_id, sleepValue=3000) {
    
    // CHANGE 1: Must await sleep
    await sleep(sleepValue);

    // For backfill only. Yes, including the parent brand. The single-brand function fetches all data on the basis of advertiser_id. Not store_id
    // Thus removing this for backfill would make the data explode to ruins. 
    // let multiBrandAcc = [
    //     "mamaway",
    //     "chess",
    //     "nutribeyond",
    //     "evoke",
    //     "drjou",
    //     "swissvita",
    //     "gbelle",
    //     "pastnine",
    //     "ivylily",
    //     "naruko"
    // ];

    // For production. No question asked. For production.
    let multiBrandAcc = [
        "nananan",
    ]

    const access_token = process.env.TIKTOK_MARKETING_ACCESS_TOKEN;
    let brandName = brand.toLowerCase().replace(/\s/g, "");
    let tableName = `${brandName}_basicads`;

    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);

    const yyyy = yesterday.getFullYear();
    const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
    const dd = String(yesterday.getDate()).padStart(2, '0');
    const yesterdayStr = `${yyyy}-${mm}-${dd}`;
    
    // CHANGE 2: Retry Variables
    let success = false;
    let retries = 10;

    while(!success && retries > 0) {
        try {
            if(multiBrandAcc.includes(brandName)) {

                console.log(`🔥 MULTIBRAND ACC ${brandName}`)

                let troubles = ["chess", "nutribeyond", "pastnine", "ivylily", "naruko", "drjou", "swissvita"];
                if(troubles.includes(brandName)) console.warn(`TROUBLES ${brandName} RUNNING. Check below.`);
                
                // 1. Get campaigns by advertiser_id
                const cbyAurl = "https://business-api.tiktok.com/open_api/v1.3/campaign/get/"

                // 2. Get ad spend by advertiser_id on campaign level
                const spendByCurl = "https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/";
                
                // Initialize arrays inside loop to ensure clean slate on retry
                let resData1 = [];
                let resData2 = [];

                // 1. Call Campaigns
                const params1 = { advertiser_id };
                const response1 = await axios.get(cbyAurl, {
                    headers: { 'Access-Token': access_token },
                    params: params1
                });

                // CHANGE 3: Manual Rate Limit Check
                if (response1.data?.code === 40100 || response1.data?.message?.includes('Too many requests')) {
                    throw new Error("40100 - Rate Limit (Campaigns)");
                }
                resData1 = resData1.concat(response1.data.data.list);
                
                // Small safety wait between calls
                await sleep(1000); 

                // 2. Call Spend
                const params2 = {
                    advertiser_id: advertiser_id,
                    service_type: "AUCTION",
                    report_type: "BASIC",
                    data_level: "AUCTION_CAMPAIGN",
                    dimensions: JSON.stringify(["campaign_id", "stat_time_day"]),
                    metrics: JSON.stringify(["spend", "impressions", "reach"]),
                    start_date: yesterdayStr,
                    end_date: yesterdayStr,
                    page: 1,
                    page_size: 200
                };

                const response2 = await axios.get(spendByCurl, {
                    headers: { 'Access-Token': access_token },
                    params: params2
                });
                
                // CHANGE 3: Manual Rate Limit Check
                if (response2.data?.code === 40100 || response2.data?.message?.includes('Too many requests')) {
                    throw new Error("40100 - Rate Limit (Spend)");
                }

                console.log(`[BASIC - GROUPED] response on ${brandName}`);
                console.log(response2?.data?.data?.list);

                resData2 = resData2.concat(response2.data.data.list);

                if(resData1.length > 0 && resData2.length > 0) {
                    let filteredSpending = processData(brandName, resData1, resData2);
                    console.log(`${brand} filteredSpending`);
                    return filteredSpending; // Success
                } else {
                    // Success but empty data
                    return []; 
                }
            } else {
                console.log("[BASIC] Fetching single brand account: ", brand);
                
                const singleUrl = "https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/";

                const params = {
                    advertiser_id: advertiser_id,
                    service_type: "AUCTION",
                    report_type: "BASIC",
                    data_level: "AUCTION_ADVERTISER",
                    dimensions: JSON.stringify(["advertiser_id", "stat_time_day"]),
                    metrics: JSON.stringify(["spend", "impressions", "reach"]),
                    start_date: yesterdayStr,
                    end_date: yesterdayStr,
                    page: 1,    
                    page_size: 200
                }

                const response = await axios.get(singleUrl, {
                    headers: { 'Access-Token': access_token },
                    params
                });

                // CHANGE 3: Manual Rate Limit Check
                if (response.data?.code === 40100 || response.data?.message?.includes('Too many requests')) {
                    throw new Error("40100 - Rate Limit (Single)");
                }

                console.log(`[BASIC-SINGLE] Res on ${brandName}`);
                
                if(response && response.data && response.data.data && response.data.data.list) {
                    const costList = response.data.data.list;
                    let singleCostList = [];

                    costList.forEach(c => {
                        if(c.metrics.spend !== "0") {
                            let costElement = {
                                "date": c.dimensions.stat_time_day,
                                "basic_cost": parseInt(c.metrics.spend),
                            }
                            singleCostList.push(costElement);
                        }
                    });

                    if(singleCostList) {
                        console.log(`[BASIC-SINGLE] ${brand} singleCostList`);
                        return singleCostList; // Success
                    }
                } else {
                    console.log(`[BASIC-SINGLE] Data on brand ${brandName} does not exist.`);
                    return []; // Success but empty
                }
            }
        } catch (e) {
            retries -= 1;
            console.log(`[BASIC] Error fetching basic ads data on brand ${brandName}: ${e.message}`);
            
            // CHANGE 4: Strict Rate Limit Backoff
            if (e.message.includes('40100') || e.response?.status === 429) {
                console.log("[BASIC] Hit Rate Limit. Sleeping 15s...");
                await sleep(15000);
            } else {
                if(retries > 0) await sleep(5000);
            }

            // CHANGE 5: Strict Failure (Throw error to BullMQ)
            if (retries === 0) {
                throw new Error(`[STRICT MODE] Failed to fetch Basic Ads for ${brand} after all retries.`);
            }
        }
    }
}

function processData(brandName, resData1, resData2) {
    console.log("Processing data: ", brandName);

    // 1. Define the mapping logic from normalized brandName to Campaign Prefix
    let campaignPrefixes = [];
    switch (brandName) {
        case "nutribeyond":
            campaignPrefixes = ["NB"];
            break;
        case "chess":
            campaignPrefixes = ["CHESS"];
            break;
        case "mamaway":
            campaignPrefixes = ["MMW", "Mamaway", "MAMAWAY"];
            break;
        case "evoke":
            campaignPrefixes = ["Evoke"];
            break;
        case "drjou":
            campaignPrefixes = ["Dr Jou"];
            break;
        case "swissvita":
            campaignPrefixes = ["Swissvita", "SWVT"];
            break;
        case "gbelle":
            campaignPrefixes = ["Gbelle"];
            break;
        case "pastnine":
            campaignPrefixes = ["Past Nine", "Past 9"];
            break;
        case "ivylily":
            campaignPrefixes = ["Ivy & Lily", "IL"];
            break;
        case "naruko":
            campaignPrefixes = ["Naruko"];
            break;
        default:
            console.warn(`No specific campaign prefix defined for brand: ${brandName}`);
            return [];
    }

    // 2. Create a Map of Campaign IDs to Campaign Names (for quick lookup)
    const campaignIdToNameMap = new Map();
    resData1.forEach(campaign => {
        console.log("[PROCESS] CAMPAIGN NAME: ", campaign.campaign_name);
        campaignIdToNameMap.set(campaign.campaign_id, campaign.campaign_name);
    });

    // 3. Filter and Transform the Spend Data (resData2)
    const filteredSpending = [];

    resData2.forEach(reportItem => {
        const campaignId = reportItem.dimensions.campaign_id;
        const campaignName = campaignIdToNameMap.get(campaignId);

        // Check if the campaign name exists and starts with the required prefix
        if (campaignName) {
            const isMatch = campaignPrefixes.some(prefix => campaignName.startsWith(prefix));

            if(isMatch) {
                const spending = parseInt(reportItem.metrics.spend);
                const dateStr = reportItem.dimensions.stat_time_day;
                
                // console.log("CAMPAIGN NAME: ", campaignName, "SPENDING: ", spending);
    
                if(spending > 0) {
                    filteredSpending.push({
                        "date": dateStr,
                        "basic_cost": spending,
                    });
                }
            }
        }
    });

    console.log(`Successfully filtered ${filteredSpending.length} records for ${brandName} (Prefix: ${campaignPrefixes})`);
    
    return filteredSpending; 
}

// import axios from 'axios';
// import { formatToDDMMYYYY } from './fetchGMVMaxSpending.js';
// import { BigQuery } from '@google-cloud/bigquery';
// const bigquery = new BigQuery();

// function sleep(ms) {
//     return new Promise(resolve => setTimeout(resolve, ms));
// }

// export async function fetchTiktokBasicAds(brand, advertiser_id, sleepValue=3000) {

//     await sleep(sleepValue);

//     let multiBrandAcc = [
//         "mamaway",
//         "chess",
//         "nutribeyond",
//         "evoke",
//         "drjou",
//         "swissvita",
//         "gbelle",
//         "pastnine",
//         "ivylily",
//         "naruko"
//     ];

//     const access_token = process.env.TIKTOK_MARKETING_ACCESS_TOKEN;
//     let brandName = brand.toLowerCase().replace(/\s/g, "");
//     let tableName = `${brandName}_basicads`;

//     const yesterday = new Date();

//     yesterday.setDate(yesterday.getDate() - 1);

//     const yyyy = yesterday.getFullYear();
//     const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
//     const dd = String(yesterday.getDate()).padStart(2, '0');
//     const yesterdayStr = `${yyyy}-${mm}-${dd}`;
    
//     if(multiBrandAcc.includes(brandName)) {

//         // 1. Get campaigns by advertiser_id
//         const cbyAurl = "https://business-api.tiktok.com/open_api/v1.3/campaign/get/"

//         // 2. Get ad spend by advertiser_id on campaign level
//         const spendByCurl = "https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/";
        
//         let resData1 = [];
//         let resData2 = [];

//         // 1
//         try {
//             const params = { advertiser_id };
//             const response = await axios.get(cbyAurl, {
//                 headers: {
//                     'Access-Token': access_token
//                 },
//                 params
//             });
//             resData1 = resData1.concat(response.data.data.list);
//         } catch (e) {
//             console.log(`Failed to get campaigns by ads id on brand ${brandName}: ${e}`);
//         }

//         // 2
//         try {
//             const params = {
//                 advertiser_id: advertiser_id,
//                 service_type: "AUCTION",
//                 report_type: "BASIC",
//                 data_level: "AUCTION_CAMPAIGN",
//                 dimensions: JSON.stringify(["campaign_id", "stat_time_day"]),
//                 metrics: JSON.stringify(["spend", "impressions", "reach"]),
//                 start_date: yesterdayStr,
//                 end_date: yesterdayStr,
//                 page: 1,
//                 page_size: 200
//             };

//             const response = await axios.get(spendByCurl, {
//                 headers: {
//                     'Access-Token': access_token
//                 },
//                 params
//             });
            
//             console.log(`[BASIC - GROUPED] response on ${brandName}`);
//             // console.log(response.data.data.list);

//             resData2 = resData2.concat(response.data.data.list);
//         } catch (e) {
//             console.log(`Failed to get ads spend on campaign level on brand ${brandName}: ${e}`);
//         }

//         if(resData1.length > 0 && resData2.length > 0) {
//             let filteredSpending = processData(brandName, tableName, resData1, resData2);
//             console.log(`${brand} filteredSpending`);
//             return filteredSpending;
//         }
//     } else {
//         console.log("[BASIC] Fetching single brand account: ", brand);
        
//         const singleUrl = "https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/";

//         try {
//             const params = {
//                 advertiser_id: advertiser_id,
//                 service_type: "AUCTION",
//                 report_type: "BASIC",
//                 data_level: "AUCTION_ADVERTISER",
//                 dimensions: JSON.stringify(["advertiser_id", "stat_time_day"]),
//                 metrics: JSON.stringify(["spend", "impressions", "reach"]),
//                 start_date: yesterdayStr,
//                 end_date: yesterdayStr,
//                 page: 1,
//                 page_size: 200
//             }

//             const response = await axios.get(singleUrl, {
//                 headers: {
//                     'Access-Token': access_token
//                 },
//                 params
//             });

//             console.log(`[BASIC-SINGLE] Res on ${brandName}`);
//             // console.log(response.data)
            
//             if(response && response.data && response.data.data && response.data.data.list) {
//                 const costList = response.data.data.list;
//                 let singleCostList = [];

//                 costList.forEach(c => {
//                     if(c.metrics.spend !== "0") {
//                         let costElement = {
//                             "date": c.dimensions.stat_time_day,
//                             "basic_cost": parseInt(c.metrics.spend),
//                         }
//                         singleCostList.push(costElement);
//                     }
//                 });

//                 if(singleCostList) {
//                     console.log(`[BASIC-SINGLE] ${brand} singleCostList`);
//                     console.log(singleCostList);
//                     return singleCostList;
//                 }
//             } else {
//                 console.log(`[BASIC-SINGLE] Data on brand ${brandName} does not exist.`);
//             }
//         } catch (e) {
//             console.log(`Error getting basic ads data on brand: ${brandName}: ${e}`);
//         }
//     }
// }

// function processData(brandName, tableName, resData1, resData2) {
//     console.log("Processing data: ", brandName);

//     // 1. Define the mapping logic from normalized brandName to Campaign Prefix
//     let campaignPrefixes = [];
//     switch (brandName) {
//         case "nutribeyond":
//             campaignPrefixes = ["NB"];
//             break;
//         case "chess":
//             campaignPrefixes = ["CHESS"];
//             break;
//         case "mamaway":
//             campaignPrefixes = ["MMW", "Mamaway", "MAMAWAY"];
//             break;
//         case "evoke":
//             campaignPrefixes = ["Evoke"];
//             break;
//         case "drjou":
//             campaignPrefixes = ["Dr Jou"];
//             break;
//         case "swissvita":
//             campaignPrefixes = ["Swissvita", "SWVT"];
//             break;
//         case "gbelle":
//             campaignPrefixes = ["Gbelle"];
//             break;
//         case "pastnine":
//             campaignPrefixes = ["Past Nine", "Past 9"];
//             break;
//         case "ivylily":
//             campaignPrefixes = ["Ivy & Lily", "IL"];
//             break;
//         case "naruko":
//             campaignPrefixes = ["Naruko"];
//             break;
//         default:
//             console.warn(`No specific campaign prefix defined for brand: ${brandName}`);
//             return [];
//     }

//     // 2. Create a Map of Campaign IDs to Campaign Names (for quick lookup)
//     const campaignIdToNameMap = new Map();
//     resData1.forEach(campaign => {
//         console.log("[PROCESS] CAMPAIGN NAME: ", campaign.campaign_name);
//         campaignIdToNameMap.set(campaign.campaign_id, campaign.campaign_name);
//     });

//     // 3. Filter and Transform the Spend Data (resData2)
//     const filteredSpending = [];

//     resData2.forEach(reportItem => {
//         const campaignId = reportItem.dimensions.campaign_id;
//         const campaignName = campaignIdToNameMap.get(campaignId);

//         // Check if the campaign name exists and starts with the required prefix
//         if (campaignName) {
//             const isMatch = campaignPrefixes.some(prefix => campaignName.startsWith(prefix));

//             if(isMatch) {
//                 const spending = parseInt(reportItem.metrics.spend);
//                 const dateStr = reportItem.dimensions.stat_time_day;
                
//                 // console.log("CAMPAIGN NAME: ", campaignName, "SPENDING: ", spending);
    
//                 if(spending > 0) {
//                     filteredSpending.push({
//                         "date": dateStr,
//                         "basic_cost": spending,
//                     });
//                 }
//             }
//         }
//     });

//     console.log(`Successfully filtered ${filteredSpending.length} records for ${brandName} (Prefix: ${campaignPrefixes})`);
    
//     return filteredSpending; 
// }
```

## File: functions\formatUnixTime.js
```
export function formatUnixTime(origin, unixTimestamp) {
  const date = new Date(unixTimestamp * 1000);
  const options = {
    timeZone: 'Asia/Jakarta',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hourCycle: 'h23' 
  };

  return new Intl.DateTimeFormat('sv-SE', options).format(date);
}
```

## File: functions\handleTiktokAdsData.js
```
import { BigQuery } from '@google-cloud/bigquery';
import { backfillEndDate, backfillStartDate } from './fetchTiktokBasicAds.js';
const bigquery = new BigQuery();

let tableNameMap = {
    "Chess": "chess_tiktok_ads",
    "Cleviant": "cleviant_tiktok_ads",
    "Dr.Jou": "dr_jou_tiktok_ads",
    "Evoke": "evoke_tiktok_ads",
    "G-Belle": "gbelle_tiktok_ads",
    "Ivy & Lily": "ivy_lily_tiktok_ads",
    "Naruko": "naruko_tiktok_ads",
    "Miss Daisy": "miss_daisy_tiktok_ads",
    "Mirae": "mirae_tiktok_ads",
    "Mamaway": "mamaway_tiktok_ads",
    "Mosseru": "mosseru_tiktok_ads",
    "Nutri & Beyond": "nutri_beyond_tiktok_ads",
    "Past Nine": "past_nine_tiktok_ads",
    "Polynia": "polynia_tiktok_ads",
    "SHRD": "shrd_tiktok_ads",
    "Swissvita": "swissvita_tiktok_ads",
    "Eileen Grace": "eileen_grace_tiktok_ads",
    "Rocketindo Shop": "rocketindo_shop_tiktok_ads",
    "Relove": "relove_tiktok_ads",
    "Joey & Roo": "joey_roo_tiktok_ads",
    "Enchante": "enchante_tiktok_ads"
}

export async function handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand) {
    console.log(`Handle Tiktok Ads Brand ${brand}`);
    if(basicAdsData && pgmvMaxData && lgmvMaxData) {

        const yesterday = new Date();

        yesterday.setDate(yesterday.getDate() - 1);
        
        const yyyy = yesterday.getFullYear();
        const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
        const dd = String(yesterday.getDate()).padStart(2, '0');
        const yesterdayStr = `${yyyy}-${mm}-${dd}`;

        let dataTiktokAds = [];
        
        let currentDate = new Date(yesterdayStr);
        let endDate = new Date(yesterdayStr);

        // let currentDate = new Date(yesterdayStr);
        // let endDate = new Date(yesterdayStr);

        while(currentDate <= endDate) {
            let tiktokAds = {
                "date": currentDate.toISOString().substring(0, 10),
                "basic_cost": 0,
                "pgmax_cost": 0,
                "lgmax_cost": 0,
                "pgmax_gmv": 0,
                "lgmax_gmv": 0,
            }
            dataTiktokAds.push(tiktokAds);
            currentDate.setDate(currentDate.getDate() + 1);
        }

        // Process basicAdsData
        dataTiktokAds.forEach((d) => {
            const match = basicAdsData.find((b) => b.date.substring(0, 10) === d.date);
            if(match) {
                d.basic_cost = match.basic_cost;
            }
        });

        // Process pgmvMaxData
        dataTiktokAds.forEach((d) => {
            const match = pgmvMaxData.find((b) => b.date.substring(0, 10) === d.date);
            if(match) {
                d.pgmax_cost = match.pgmax_cost;
                d.pgmax_gmv = match.pgmax_gmv;
            }
        });

        // Process lgmvMaxData
        dataTiktokAds.forEach((d) => {
            const match = lgmvMaxData.find((b) => b.date.substring(0, 10) === d.date);
            if(match) {
                d.lgmax_cost = match.lgmax_cost;
                d.lgmax_gmv = match.lgmax_gmv;
            }
        });

        console.log("TO MERGE - Data Tiktok Ads: ", brand);
        // Added 'brand' to arguments so logging works
        await mergeTiktokAdsData(dataTiktokAds, tableNameMap[brand], brand);
    }
}

async function mergeTiktokAdsData(data, tableName, brand) {
    console.log("Merging data to table: ", tableName);

    const datasetId = "tiktok_api_us";

    try {
        for(const d of data) {
            // --- NEW: DUPLICATION CHECK ---
            // Check if this date already exists in the table
            const checkQuery = `SELECT date FROM \`${datasetId}.${tableName}\` WHERE date = '${d.date}'`;
            const [existingRows] = await bigquery.query({ query: checkQuery });

            if (existingRows.length > 0) {
                console.log(`[SKIP] Data for ${d.date} already exists in ${tableName}. Skipping to prevent duplication.`);
                continue; // Skip this insertion
            }

            // If not exists, proceed to insert
            await bigquery
                .dataset(datasetId)
                .table(tableName)
                .insert({
                    date: d.date,
                    basic_cost: d.basic_cost, 
                    pgmax_cost: d.pgmax_cost,
                    lgmax_cost: d.lgmax_cost,
                    pgmax_gmv: d.pgmax_gmv,
                    lgmax_gmv: d.lgmax_gmv,
                    process_dttm: new Date(Date.now() + 7 * 60 * 60 * 1000).toISOString().replace('T', ' ').substring(0, 19)
                });
        }
        console.log(`Successfully processed ${data.length} row(s) for ${tableName}`);
    } catch (e) {
        console.log("Error merge tiktok ads data on: ", brand, "error: ", e);
    }
}


// Revert to this version if above ver fails.
// import { BigQuery } from '@google-cloud/bigquery';
// const bigquery = new BigQuery();

// let tableNameMap = {
//     "Chess": "chess_tiktok_ads",
//     "Cleviant": "cleviant_tiktok_ads",
//     "Dr.Jou": "dr_jou_tiktok_ads",
//     "Evoke": "evoke_tiktok_ads",
//     "G-Belle": "gbelle_tiktok_ads",
//     "Ivy & Lily": "ivy_lily_tiktok_ads",
//     "Naruko": "naruko_tiktok_ads",
//     "Miss Daisy": "miss_daisy_tiktok_ads",
//     "Mirae": "mirae_tiktok_ads",
//     "Mamaway": "mamaway_tiktok_ads",
//     "Mosseru": "mosseru_tiktok_ads",
//     "Nutri & Beyond": "nutri_beyond_tiktok_ads",
//     "Past Nine": "past_nine_tiktok_ads",
//     "Polynia": "polynia_tiktok_ads",
//     "SHRD": "shrd_tiktok_ads",
//     "Swissvita": "swissvita_tiktok_ads",
//     "Eileen Grace": "eileen_grace_tiktok_ads"
// }

// export async function handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand) {
//     console.log(`Handle Tiktok Ads Brand ${brand}`);
//     if(basicAdsData && pgmvMaxData && lgmvMaxData) {

//         const yesterday = new Date();
//         yesterday.setDate(yesterday.getDate() - 1);
//         const yyyy = yesterday.getFullYear();
//         const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
//         const dd = String(yesterday.getDate()).padStart(2, '0');
//         const yesterdayStr = `${yyyy}-${mm}-${dd}`;

//         let dataTiktokAds = [];
//         // Process basicAdsData first, then pgmvMax, then lgmvMax

//         // let startDate = new Date(yesterdayStr);
//         let endDate = new Date(yesterdayStr);
//         let currentDate = new Date(yesterdayStr);

//         while(currentDate <= endDate) {

//             let tiktokAds = {
//                 "date": currentDate.toISOString().substring(0, 10),
//                 "basic_cost": 0,
//                 "pgmax_cost": 0,
//                 "lgmax_cost": 0
//             }
//             dataTiktokAds.push(tiktokAds);
//             currentDate.setDate(currentDate.getDate() + 1);
//         }

//         // Process basicAdsData
//         dataTiktokAds.forEach((d) => {
//             const match = basicAdsData.find((b) => b.date.substring(0, 10) === d.date);
//             if(match) {
//                 d.basic_cost = match.basic_cost;
//             }
//         });

//         // Process pgmvMaxData
//         dataTiktokAds.forEach((d) => {
//             const match = pgmvMaxData.find((b) => b.date.substring(0, 10) === d.date);
//             if(match) {
//                 d.pgmax_cost = match.pgmax_cost;
//             }
//         });

//         // Process lgmvMaxData
//         dataTiktokAds.forEach((d) => {
//             const match = lgmvMaxData.find((b) => b.date.substring(0, 10) === d.date);
//             if(match) {
//                 d.lgmax_cost = match.lgmax_cost;
//             }
//         });

//         // Ver 23.11.25.2141: No timeouts on brand functions. Checking data to merge first.
//         // Problem: undefined data (can be basic, product, or live data)
//         // Additional: data duplication.
//         // Probable cause: race condition, rate limiting. 
//         console.log("TO MERGE - Data Tiktok Ads: ", brand);
//         await mergeTiktokAdsData(dataTiktokAds, tableNameMap[brand]);
//     }
// }

// async function mergeTiktokAdsData(data, tableName) {
//     console.log("Merging data to table: ", tableName);

//     const datasetId = "tiktok_api_us";

//     try {
//         for(const d of data) {
//             await bigquery
//                 .dataset(datasetId)
//                 .table(tableName)
//                 .insert({
//                     date: d.date,
//                     basic_cost: d.basic_cost, 
//                     pgmax_cost: d.pgmax_cost,
//                     lgmax_cost: d.lgmax_cost
//                 });
//         }
//         console.log(`Successfully merged ${data.length} data to ${tableName}`);
//     } catch (e) {
//         console.log("Error merge tiktok ads data on: ", brand, "error: ", e);
//     }
// }

// ver lama
// import { BigQuery } from '@google-cloud/bigquery';
// const bigquery = new BigQuery();

// let tableNameMap = {
//     "Chess": "chess_tiktok_ads",
//     "Cleviant": "cleviant_tiktok_ads",
//     "Dr.Jou": "dr_jou_tiktok_ads",
//     "Evoke": "evoke_tiktok_ads",
//     "G-Belle": "gbelle_tiktok_ads",
//     "Ivy & Lily": "ivy_lily_tiktok_ads",
//     "Naruko": "naruko_tiktok_ads",
//     "Miss Daisy": "miss_daisy_tiktok_ads",
//     "Mirae": "mirae_tiktok_ads",
//     "Mamaway": "mamaway_tiktok_ads",
//     "Mosseru": "mosseru_tiktok_ads",
//     "Nutri & Beyond": "nutri_beyond_tiktok_ads",
//     "Past Nine": "past_nine_tiktok_ads",
//     "Polynia": "polynia_tiktok_ads",
//     "SHRD": "shrd_tiktok_ads",
//     "Swissvita": "swissvita_tiktok_ads",
//     "Eileen Grace": "eileen_grace_tiktok_ads"
// }

// export async function handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand) {
//     console.log(`Handle Tiktok Ads Brand ${brand}`);

//     if (basicAdsData && pgmvMaxData && lgmvMaxData) {
//         // 1. Calculate Yesterday
//         const yesterday = new Date();

//         yesterday.setDate(yesterday.getDate() - 2);

//         const yyyy = yesterday.getFullYear();
//         const mm = String(yesterday.getMonth() + 1).padStart(2, '0');
//         const dd = String(yesterday.getDate()).padStart(2, '0');
//         const yesterdayStr = `${yyyy}-${mm}-${dd}`;

//         // 2. Initialize the single object (No loop needed for 1 day)
//         let dailyData = {
//             "date": yesterdayStr,
//             "basic_cost": 0,
//             "pgmax_cost": 0,
//             "lgmax_cost": 0
//         };

//         // 3. Map Data (Using yesterdayStr directly)
//         // Check basicAdsData
//         const basicMatch = basicAdsData.find((b) => b.date.substring(0, 10) === yesterdayStr);
//         if (basicMatch) dailyData.basic_cost = basicMatch.basic_cost;

//         // Check pgmvMaxData
//         const pgMatch = pgmvMaxData.find((b) => b.date.substring(0, 10) === yesterdayStr);
//         if (pgMatch) dailyData.pgmax_cost = pgMatch.pgmax_cost;

//         // Check lgmvMaxData
//         const lgMatch = lgmvMaxData.find((b) => b.date.substring(0, 10) === yesterdayStr);
//         if (lgMatch) dailyData.lgmax_cost = lgMatch.lgmax_cost;

//         // 4. Merge (Pass brand for logging)
//         // We wrap dailyData in an array [] because insert expects rows
//         await mergeTiktokAdsData([dailyData], tableNameMap[brand], brand);
//     }
// }

// // Updated merge function
// async function mergeTiktokAdsData(data, tableName, brand) {
//     console.log("Merging data to table: ", tableName);
//     const datasetId = "tiktok_api_us";

//     try {
//         // OPTIMIZATION: Insert all rows at once, outside of a loop.
//         // BigQuery accepts an array of objects.
//         await bigquery
//             .dataset(datasetId)
//             .table(tableName)
//             .insert(data);
            
//         console.log(`Successfully merged ${data.length} data to ${tableName}`);
//     } catch (e) {
//         // Now 'brand' is defined here
//         console.log("Error merge tiktok ads data on: ", brand, "error: ", e);
        
//         // Helpful for debugging BigQuery partial failures
//         if (e.name === 'PartialFailureError') {
//              console.log("Partial errors:", JSON.stringify(e.errors, null, 2));
//         }
//     }
// }
```

## File: functions\tiktokRateLimiter.js
```
import Bottleneck from 'bottleneck';
import Redis from 'ioredis';

// Use your Redis Memorystore connection string
const redis = new Redis(process.env.REDIS_URL);

const limiter = new Bottleneck({
  id: 'tiktok-api-global', // Unique ID for this limiter
  minTime: 1200,           // 1.2 seconds between requests (adjust as needed)
  maxConcurrent: 1,        // Only one request at a time
  datastore: 'ioredis',
  clearDatastore: false,
  clientOptions: { client: redis }
});

redis.on('error', (err) => {
  console.error('[RATE-LIMITER] Redis connection error:', err);
});
redis.on('connect', () => {
  console.log('[RATE-LIMITER] Connected to Redis!');
});

// Export a wrapper for your API calls
export function rateLimitedCall(fn, ...args) {
  return limiter.schedule(() => fn(...args));
}
```

## File: functions\walletTransactions.js
```
import axios from 'axios';
import crypto from 'crypto';
import { BigQuery } from '@google-cloud/bigquery';

async function fetchWalletTransaction(brand, partner_id, partner_key, access_token, shop_id) {    
    console.log("Fetch Wallet Transaction of brand: ", brand);
    const HOST = "https://partner.shopeemobile.com";
    const PATH = "/api/v2/payment/get_wallet_transaction_list";

    try {
        const timestamp = Math.floor(Date.now() / 1000);
        const baseString = `${partner_id}${PATH}${timestamp}${access_token}${shop_id}`;
        const sign = crypto.createHmac('sha256', partner_key)
            .update(baseString)
            .digest('hex');
        
        let count = 0;
        let hasMore = true;
        let pageNumber = 0;
        let transactionContainer = [];

        while(hasMore) {
            const createTimeTo = Math.floor(new Date().setDate(new Date().getDate() - 1) / 1000);
            const createTimeFrom = Math.floor(new Date().setDate(new Date().getDate() - 7) / 1000);
            const params = new URLSearchParams({
                partner_id: partner_id,
                timestamp,
                access_token: access_token,
                shop_id: shop_id,
                sign,
                page_size: 40,
                page_no: pageNumber,
                create_time_from: createTimeFrom,
                create_time_to: createTimeTo
            });
            const fullUrl = `${HOST}${PATH}?${params.toString()}`;
            console.log(`Hitting Wallet Trx for ${brand}: `, fullUrl, " - page: ", pageNumber);

            const response = await axios.get(fullUrl, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            let transactionList = response.data.response.transaction_list;
            transactionContainer.push(...transactionList);

            count += transactionList.length;
            hasMore = response.data.response.more;
            pageNumber += 1;
        }
        console.log("[WALLET-TRX] Data count: ", count);
        return transactionContainer;
    } catch (e) {
        console.log("[WALLET-TRX] Error on fetching wallet transaction of brand: ", brand);
        console.log(e);
    }
}

async function transformData(data) {
    let transformed = [];
    data.forEach(d => {
        if(d.status !== "COMPLETED") {
            console.log("Non-completed data: ", d.status);
        }
        let obj = {
            'created_date': new Date(d.create_time * 1000).toISOString().replace('T', ' ').split('.')[0],
            'order_sn': d.order_sn,
            'description': d.description,
            'amount': d.amount,
            'money_flow': d.money_flow,
            'transaction_id': d.transaction_id,
            'status': d.status,
        }
        transformed.push(obj);
    });
    return transformed;
}

const brandTables = {
    "Chess": "chess_wallet_trx",
    "Cleviant": "cleviant_wallet_trx",
    "Dr.Jou": "dr_jou_wallet_trx",
    "Evoke": "evoke_wallet_trx",
    "G-Belle": "gbelle_wallet_trx",
    "Ivy & Lily": "ivy_lily_wallet_trx",
    "Naruko": "naruko_wallet_trx",
    "Miss Daisy": "miss_daisy_wallet_trx",
    "Mirae": "mirae_wallet_trx",
    "Mamaway": "mamaway_wallet_trx",
    "Mosseru": "mosseru_wallet_trx",
    "Nutri & Beyond": "nutri_beyond_wallet_trx",
    "Past Nine": "past_nine_wallet_trx",
    "Polynia": "polynia_wallet_trx",
    "SH-RD": "shrd_wallet_trx",
    "Swissvita": "swissvita_wallet_trx",
    "Eileen Grace": "eileen_grace_wallet_trx",
    "Relove": "relove_wallet_trx",
    "Joey & Roo": "joey_roo_wallet_trx",
    "Enchante": "enchante_wallet_trx",
    "Rocketindo Shop": "rocketindo_shop_wallet_trx",
}

async function mergeData(data, brand) {
    console.log("[WALLET-TRX] Start merging for brand: ", brand);
    const tableName = brandTables[brand];
    const bigquery = new BigQuery();
    const datasetId = 'shopee_api';

    // If no data to merge, exit early to save API calls
    if (!data || data.length === 0) {
        console.log("[WALLET-TRX] No data to merge for", brand);
        return;
    }
    const uniqueMap = new Map();
    data.forEach(item => {
        // We use the transaction_id as the key. 
        // If it already exists, this overwrites it with the latest version.
        uniqueMap.set(String(item.transaction_id), item);
    });
    const uniqueData = Array.from(uniqueMap.values());

    try {
        // SQL: MERGE Statement (The "Upsert" Logic)
        // We match rows based on 'transaction_id'.
        const query = `
            MERGE \`${datasetId}.${tableName}\` T
            USING UNNEST(@sourceData) S
            ON T.transaction_id = S.transaction_id
            
            -- 1. If ID exists: Update the status and refresh the process timestamp
            WHEN MATCHED THEN
                UPDATE SET 
                    status = S.status,
                    process_dttm = CURRENT_DATETIME()
            
            -- 2. If ID is new: Insert the full record
            WHEN NOT MATCHED THEN
                INSERT (
                    transaction_id, 
                    created_date, 
                    order_sn, 
                    description, 
                    amount, 
                    money_flow, 
                    status, 
                    process_dttm
                )
                VALUES (
                    S.transaction_id, 
                    S.created_date, 
                    S.order_sn, 
                    S.description, 
                    S.amount, 
                    S.money_flow, 
                    S.status, 
                    CURRENT_DATETIME()
                )
        `;

        // Map data to ensure clean types for BigQuery
        const sourceData = uniqueData.map(d => ({
            transaction_id: String(d.transaction_id), // Ensure ID is a string
            created_date: d.created_date,
            order_sn: d.order_sn,
            description: d.description,
            amount: parseFloat(d.amount),
            money_flow: d.money_flow,
            status: d.status
        }));

        const options = {
            query,
            params: {
                sourceData: sourceData
            }
        };

        // Run the query
        await bigquery.query(options);
        console.log(`[WALLET-TRX] Successfully merged (upserted) ${sourceData.length} rows for ${brand}`);

    } catch (e) {
        console.log("[WALLET-TRX] Error merging wallet trx on brand: ", brand);
        console.log(e);
    }   
}

export async function handleWalletTransactions(brand, partner_id, partner_key, access_token, shop_id) {
    const transactionContainer = await fetchWalletTransaction(brand, partner_id, partner_key, access_token, shop_id);
    const transformed = await transformData(transactionContainer);
    await mergeData(transformed, brand);
}


```

## File: workers\chess_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchGMVMaxSpending } from '../functions/fetchGMVMaxSpending.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.CLEVIANT_PARTNER_ID);
export const PARTNER_KEY = process.env.CLEVIANT_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.CHESS_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let CHESS_ACCESS_TOKEN;
let CHESS_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: CHESS_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint CHESS: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        CHESS_ACCESS_TOKEN = newAccessToken;
        CHESS_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: CHESS_ACCESS_TOKEN,
            refreshToken: CHESS_REFRESH_TOKEN
        });
    } else {
        console.log("[CHESS] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/chess-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[CHESS] Successfully saved tokens to CHESS Secret Manager: ", parent);
    } catch (e) {
        console.error("[CHESS] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/chess-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[CHESS] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersCHESS() {
    console.log("Starting fetch orders CHESS");
    let brand = "Chess";

    const loadedTokens = await loadTokensFromSecret();
    CHESS_ACCESS_TOKEN = loadedTokens.accessToken;
    CHESS_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, CHESS_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, CHESS_ACCESS_TOKEN, SHOP_ID)
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, CHESS_ACCESS_TOKEN, SHOP_ID);
   
    await fetchAffiliateData(brand, SHOP_ID, 3500);

    let advIdChess = "7374315302508642321";

    // For backfilling
    let advIdMamaway = "7306800699382251521";

    let advertiserId = advIdChess;

    const basicAdsData = await fetchTiktokBasicAds(brand, advertiserId);

    const pgmvMaxData = await fetchProductGMVMax(brand, advertiserId);

    const lgmvMaxData = await fetchLiveGMVMax(brand, advertiserId);

    console.log("[CHESS] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    // For backfilling
    await fetchPGMVMaxBreakdown(brand, advertiserId);
}

```

## File: workers\clev_processor.js
```
import { SecretManagerServiceClient } from "@google-cloud/secret-manager";
import axios from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from "../functions/fetchAdsTotalBalance.js";
import { fetchTiktokBasicAds } from "../functions/fetchTiktokBasicAds.js";
import { fetchProductGMVMax } from "../functions/fetchProductGMVMax.js";
import { fetchLiveGMVMax } from "../functions/fetchLiveGMVMax.js";
import { handleTiktokAdsData } from "../functions/handleTiktokAdsData.js";
import { fetchPGMVMaxBreakdown } from "../functions/fetchPGMVMaxBreakdown.js";
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from "../functions/walletTransactions.js";
import { mainDanaDilepas } from "../functions/escrowProcessor.js";

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.CLEVIANT_PARTNER_ID);
export const PARTNER_KEY = process.env.CLEVIANT_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.CLEVIANT_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";

export const HOST = "https://partner.shopeemobile.com";
const PATH = "/api/v2/order/get_order_list";

export let CLEV_ACCESS_TOKEN;
let CLEV_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: CLEV_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint CLEV: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        CLEV_ACCESS_TOKEN = newAccessToken;
        CLEV_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: CLEV_ACCESS_TOKEN,
            refreshToken: CLEV_REFRESH_TOKEN
        });
    } else {
        console.log("[CLEV] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/clev-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        
        console.log("[CLEV] Successfully saved tokens to CLEV Secret Manager: ", parent);
    } catch (e) {
        console.error("[CLEV] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/clev-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("[CLEV] Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[CLEV] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersCLEV() {
    console.log("[CLEV] Start fetching ads total balance. Calling the function.");
    let brand = "Cleviant";

    const loadedTokens = await loadTokensFromSecret();
    CLEV_ACCESS_TOKEN = loadedTokens.accessToken;
    CLEV_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, CLEV_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, CLEV_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, CLEV_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 4000);

    let advIdClev = "7553576714043965448";
    
    // For backfill
    let advIdMirae = "7306798768821387265";

    let advertiserId = advIdClev;

    const basicAdsData = await fetchTiktokBasicAds(brand, advertiserId);
    const pgmvMaxData = await fetchProductGMVMax(brand, advertiserId);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advertiserId);
    
    console.log("[CLEV] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advertiserId);
}

```

## File: workers\drjou_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.DRJOU_PARTNER_ID);
export const PARTNER_KEY = process.env.DRJOU_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.DRJOU_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let DRJOU_ACCESS_TOKEN;
let DRJOU_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: DRJOU_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint DRJOU: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        DRJOU_ACCESS_TOKEN = newAccessToken;
        DRJOU_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: DRJOU_ACCESS_TOKEN,
            refreshToken: DRJOU_REFRESH_TOKEN
        });
    } else {
        console.log("[DRJOU] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/drjou-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[DRJOU] Successfully saved tokens to DRJOU Secret Manager: ", parent);
    } catch (e) {
        console.error("[DRJOU] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/drjou-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[DRJOU] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersDRJOU() {
    console.log("Starting fetch orders DRJOU");
    let brand = "Dr.Jou";
    let brandTT = "Dr Jou";

    const loadedTokens = await loadTokensFromSecret();
    DRJOU_ACCESS_TOKEN = loadedTokens.accessToken;
    DRJOU_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, DRJOU_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, DRJOU_ACCESS_TOKEN, SHOP_ID)
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, DRJOU_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 6000);

    let advIdDrJou = "7431385339190820880"
    
    // For backfilling
    let advIdEvoke = "7374337917889953808"

    let advertiserId = advIdDrJou;

    const basicAdsData = await fetchTiktokBasicAds(brandTT, advertiserId);
    const pgmvMaxData = await fetchProductGMVMax(brandTT, advertiserId);
    const lgmvMaxData = await fetchLiveGMVMax(brandTT, advertiserId);
    
    console.log("[DRJOU] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    // For backfilling
    await fetchPGMVMaxBreakdown(brandTT, advertiserId);
}

```

## File: workers\evoke_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.SHRD_PARTNER_ID);
export const PARTNER_KEY = process.env.SHRD_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.EVOKE_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let EVOKE_ACCESS_TOKEN;
let EVOKE_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: EVOKE_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint EVOKE: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        EVOKE_ACCESS_TOKEN = newAccessToken;
        EVOKE_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: EVOKE_ACCESS_TOKEN,
            refreshToken: EVOKE_REFRESH_TOKEN
        });
    } else {
        console.log("[EVOKE] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/evoke-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[EVOKE] Successfully saved tokens to EVOKE Secret Manager: ", parent);
    } catch (e) {
        console.error("[EVOKE] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/evoke-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[EVOKE] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersEVOKE() {
    console.log("Starting fetch orders EVOKE");
    let brand = "Evoke";

    const loadedTokens = await loadTokensFromSecret();
    EVOKE_ACCESS_TOKEN = loadedTokens.accessToken;
    EVOKE_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, EVOKE_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, EVOKE_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, EVOKE_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 5500);

    let advIdEvoke = "7374337917889953808"
    const basicAdsData = await fetchTiktokBasicAds(brand, advIdEvoke);
    const pgmvMaxData = await fetchProductGMVMax(brand, advIdEvoke);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advIdEvoke);
    
    console.log("[EVOKE] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advIdEvoke);
}


```

## File: workers\gb_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.MD_PARTNER_ID);
export const PARTNER_KEY = process.env.MD_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.GB_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let GB_ACCESS_TOKEN;
let GB_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: GB_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint GB: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        GB_ACCESS_TOKEN = newAccessToken;
        GB_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: GB_ACCESS_TOKEN,
            refreshToken: GB_REFRESH_TOKEN
        });
    } else {
        console.log("[GBELLE] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/gb-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[GB] Successfully saved tokens to GB Secret Manager: ", parent);
    } catch (e) {
        console.error("[GB] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/gb-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[GB] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersGB() {
    console.log("Starting fetch orders GB");
    let brand = "G-Belle";
    let brandTT = "GBelle";

    const loadedTokens = await loadTokensFromSecret();
    GB_ACCESS_TOKEN = loadedTokens.accessToken;
    GB_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, GB_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, GB_ACCESS_TOKEN, SHOP_ID)
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, GB_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 7500);
    
    let advIdGbelle = "7329483707528691714";
    const basicAdsData = await fetchTiktokBasicAds(brandTT, advIdGbelle);
    const pgmvMaxData = await fetchProductGMVMax(brandTT, advIdGbelle);
    const lgmvMaxData = await fetchLiveGMVMax(brandTT, advIdGbelle);
    
    console.log("[GBELLE] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brandTT, advIdGbelle);
}

```

## File: workers\il_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.PARTNER_ID);
export const PARTNER_KEY = process.env.PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.IL_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let IL_ACCESS_TOKEN;
let IL_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: IL_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint IL: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        IL_ACCESS_TOKEN = newAccessToken;
        IL_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: IL_ACCESS_TOKEN,
            refreshToken: IL_REFRESH_TOKEN
        });
    } else {
        console.log("[IL] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/il-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }

        console.log("[IL] Successfully saved tokens to IL Secret Manager: ", parent);
    } catch (e) {
        console.error("[IL] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/il-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[IL] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersIL() {
    console.log("Starting fetch orders IL");
    let brand = "Ivy & Lily";
    let brandTT = "Ivy Lily";
    let brandNaruko = "Naruko";

    const loadedTokens = await loadTokensFromSecret();
    IL_ACCESS_TOKEN = loadedTokens.accessToken;
    IL_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, IL_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, IL_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, IL_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 9000);
    
    // For backfilling
    let advIdGbelle = "7329483707528691714";
    
    let advIdIvyLily = "7462652500143996929";
    const basicAdsData = await fetchTiktokBasicAds(brandTT, advIdIvyLily);
    const pgmvMaxData = await fetchProductGMVMax(brandTT, advIdIvyLily);
    const lgmvMaxData = await fetchLiveGMVMax(brandTT, advIdIvyLily);
    
    console.log("[IVYLILY] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    let advIdNaruko = "7392579089489608720"
    const basicAdsDataNaruko = await fetchTiktokBasicAds(brandNaruko, advIdNaruko, 19000);
    const pgmvMaxDataNaruko = await fetchProductGMVMax(brandNaruko, advIdNaruko, 20000);
    const lgmvMaxDataNaruko = await fetchLiveGMVMax(brandNaruko, advIdNaruko, 21000);
    
    console.log("[NARUKO] All data on: ", brandNaruko);
    console.log(basicAdsDataNaruko);
    console.log(pgmvMaxDataNaruko);
    console.log(lgmvMaxDataNaruko);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await handleTiktokAdsData(basicAdsDataNaruko, pgmvMaxDataNaruko, lgmvMaxDataNaruko, brandNaruko);

    // For backfilling
    await fetchPGMVMaxBreakdown(brandTT, advIdIvyLily);
    await fetchPGMVMaxBreakdown(brandNaruko, advIdNaruko);
}

```

## File: workers\md_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.MD_PARTNER_ID);
export const PARTNER_KEY = process.env.MD_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.MD_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";

export const HOST = "https://partner.shopeemobile.com";
const PATH = "/api/v2/order/get_order_list";

export let MD_ACCESS_TOKEN;
let MD_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: MD_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint MD: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        MD_ACCESS_TOKEN = newAccessToken;
        MD_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: MD_ACCESS_TOKEN,
            refreshToken: MD_REFRESH_TOKEN
        });
    } else {
        console.log("[MD] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/md-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[MD] Successfully saved tokens to MD Secret Manager: ", parent);
    } catch (e) {
        console.error("[MD] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/md-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[MD] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersMD() {
    console.log("Starting fetch orders MD");
    let brand = "Miss Daisy";

    const loadedTokens = await loadTokensFromSecret();
    MD_ACCESS_TOKEN = loadedTokens.accessToken;
    MD_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, MD_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, MD_ACCESS_TOKEN, SHOP_ID);
    
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, MD_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 2500);

    let advIdMD = "7271210972684451842";
    const basicAdsData = await fetchTiktokBasicAds(brand, advIdMD);
    const pgmvMaxData = await fetchProductGMVMax(brand, advIdMD);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advIdMD);
    
    console.log("[MISSDAISY] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advIdMD);
}

```

## File: workers\mirae_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.DRJOU_PARTNER_ID);
export const PARTNER_KEY = process.env.DRJOU_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.MIRAE_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let MIRAE_ACCESS_TOKEN;
let MIRAE_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: MIRAE_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint MIRAE: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        MIRAE_ACCESS_TOKEN = newAccessToken;
        MIRAE_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: MIRAE_ACCESS_TOKEN,
            refreshToken: MIRAE_REFRESH_TOKEN
        });
    } else {
        console.log("[MIRAE] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/mirae-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }

        console.log("[MIRAE] Successfully saved tokens to MIRAE Secret Manager: ", parent);
    } catch (e) {
        console.error("[MIRAE] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/mirae-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[MIRAE] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersMIRAE() {
    console.log("Starting fetch orders MIRAE");
    let brand = "Mirae";

    const loadedTokens = await loadTokensFromSecret();
    MIRAE_ACCESS_TOKEN = loadedTokens.accessToken;
    MIRAE_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, MIRAE_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, MIRAE_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, MIRAE_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 6500);

    let advIdMirae = "7306798768821387265";
    const basicAdsData = await fetchTiktokBasicAds(brand, advIdMirae);
    const pgmvMaxData = await fetchProductGMVMax(brand, advIdMirae);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advIdMirae);
    
    console.log("[MIRAE] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advIdMirae);
}

```

## File: workers\mmw_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.MOSS_PARTNER_ID);
export const PARTNER_KEY = process.env.MOSS_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.MMW_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let MMW_ACCESS_TOKEN;
let MMW_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: MMW_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint MMW: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        MMW_ACCESS_TOKEN = newAccessToken;
        MMW_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: MMW_ACCESS_TOKEN,
            refreshToken: MMW_REFRESH_TOKEN
        });
    } else {
        console.log("[MMW] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/mmw-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[MMW] Successfully saved tokens to MMW Secret Manager: ", parent);
    } catch (e) {
        console.error("[MMW] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/mmw-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[MMW] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersMMW() {
    console.log("Starting fetch orders MMW");
    let brand = "Mamaway";

    const loadedTokens = await loadTokensFromSecret();
    MMW_ACCESS_TOKEN = loadedTokens.accessToken;
    MMW_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, MMW_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, MMW_ACCESS_TOKEN, SHOP_ID)
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, MMW_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 1500);
    
    let advIdMamaway = "7306800699382251521";
    const basicAdsData = await fetchTiktokBasicAds(brand, advIdMamaway);
    const pgmvMaxData = await fetchProductGMVMax(brand, advIdMamaway);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advIdMamaway);
    
    console.log("[MMW] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advIdMamaway);
}

```

## File: workers\moss_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.MOSS_PARTNER_ID);
export const PARTNER_KEY = process.env.MOSS_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.MOSS_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let MOSS_ACCESS_TOKEN;
let MOSS_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: MOSS_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint MOSS: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        MOSS_ACCESS_TOKEN = newAccessToken;
        MOSS_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: MOSS_ACCESS_TOKEN,
            refreshToken: MOSS_REFRESH_TOKEN
        });
    } else {
        console.log("[MOSS] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/moss-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }

        console.log("[MOSS] Successfully saved tokens to MOSS Secret Manager: ", parent);
    } catch (e) {
        console.error("[MOSS] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/moss-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[MOSS] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersMOSS() {
    console.log("Starting fetch orders MOSS");
    let brand = "Mosseru";

    const loadedTokens = await loadTokensFromSecret();
    MOSS_ACCESS_TOKEN = loadedTokens.accessToken;
    MOSS_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, MOSS_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, MOSS_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, MOSS_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 5000);

    let advIdMoss = "7553574194160746513";
    let advIdMirae = "7306798768821387265";
    let advertiserId = advIdMoss;

    const basicAdsData = await fetchTiktokBasicAds(brand, advertiserId);
    const pgmvMaxData = await fetchProductGMVMax(brand, advertiserId);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advertiserId);
    
    console.log("[MOSS] All data on: ", brand);

    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advertiserId);
}

```

## File: workers\nb_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.PN_PARTNER_ID);
export const PARTNER_KEY = process.env.PN_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.NB_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let NB_ACCESS_TOKEN;
let NB_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: NB_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint NB: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        NB_ACCESS_TOKEN = newAccessToken;
        NB_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: NB_ACCESS_TOKEN,
            refreshToken: NB_REFRESH_TOKEN
        });
    } else {
        console.log("[NB] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/nb-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[NB] Successfully saved tokens to NB Secret Manager: ", parent);
    } catch (e) {
        console.error("[NB] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/nb-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[NB] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersNB() {
    console.log("Starting fetch orders NB");
    let brand = "Nutri & Beyond";
    let brandTT = "Nutri Beyond";

    const loadedTokens = await loadTokensFromSecret();
    NB_ACCESS_TOKEN = loadedTokens.accessToken;
    NB_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, NB_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, NB_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, NB_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 8500);

    let advIdNutriBeyond = "7457040121955729425";
    // For backfilling
    let advIdMamaway = "7306800699382251521";

    let advertiserId = advIdNutriBeyond;

    const basicAdsData = await fetchTiktokBasicAds(brandTT, advertiserId);
    const pgmvMaxData = await fetchProductGMVMax(brandTT, advertiserId);
    const lgmvMaxData = await fetchLiveGMVMax(brandTT, advertiserId);
    
    console.log("[NB] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    // For backfilling
    await fetchPGMVMaxBreakdown(brandTT, advertiserId);
}

```

## File: workers\pn_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.PN_PARTNER_ID);
export const PARTNER_KEY = process.env.PN_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.PN_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let PN_ACCESS_TOKEN;
let PN_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: PN_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint PN: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        PN_ACCESS_TOKEN = newAccessToken;
        PN_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: PN_ACCESS_TOKEN,
            refreshToken: PN_REFRESH_TOKEN
        });
    } else {
        console.log("[PN] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/pn-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }

        console.log("[PN] Successfully saved tokens to PN Secret Manager: ", parent);
    } catch (e) {
        console.error("[PN] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/pn-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[PN] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersPN() {
    console.log("Starting fetch orders PN");
    let brand = "Past Nine";

    const loadedTokens = await loadTokensFromSecret();
    PN_ACCESS_TOKEN = loadedTokens.accessToken;
    PN_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, PN_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, PN_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, PN_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 8000);

    let advIdPastnine = "7443655343483191313";
    
    // For backfilling
    let advIdGbelle = "7329483707528691714";

    let advertiserId = advIdPastnine;

    const basicAdsData = await fetchTiktokBasicAds(brand, advertiserId);
    const pgmvMaxData = await fetchProductGMVMax(brand, advertiserId);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advertiserId);
    
    console.log("[PASTNINE] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    // For backfilling
    await fetchPGMVMaxBreakdown(brand, advertiserId);
}

```

## File: workers\poly_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.POLY_PARTNER_ID);
export const PARTNER_KEY = process.env.POLY_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.POLY_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let POLY_ACCESS_TOKEN;
let POLY_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: POLY_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint POLY: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        POLY_ACCESS_TOKEN = newAccessToken;
        POLY_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: POLY_ACCESS_TOKEN,
            refreshToken: POLY_REFRESH_TOKEN
        });
    } else {
        console.log("[POLY] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/poly-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }

        console.log("[POLY] Successfully saved tokens to POLY Secret Manager: ", parent);
    } catch (e) {
        console.error("[POLY] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/poly-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[POLY] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersPOLY() {
    console.log("Starting fetch orders POLY");
    let brand = "Polynia";

    const loadedTokens = await loadTokensFromSecret();
    POLY_ACCESS_TOKEN = loadedTokens.accessToken;
    POLY_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, POLY_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, POLY_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, POLY_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 7400);

    let advIdPoly = "7275178424493211650";
    const basicAdsData = await fetchTiktokBasicAds(brand, advIdPoly);
    const pgmvMaxData = await fetchProductGMVMax(brand, advIdPoly);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advIdPoly);
    
    console.log("[POLYNIA] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advIdPoly);
}

```

## File: workers\shrd_processor.js
```
import { SecretManagerServiceClient } from "@google-cloud/secret-manager";
import { getEndOfPreviousMonthTimestampWIB, getEndOfYesterdayTimestampWIB, getStartOfMonthTimestampWIB, getStartOfPreviousMonthTimestampWIB } from '../processor.js';
import axios from 'axios';
import crypto from "crypto";
import { fetchAdsTotalBalance } from "../functions/fetchAdsTotalBalance.js";
import { fetchTiktokBasicAds } from "../functions/fetchTiktokBasicAds.js";
import { fetchProductGMVMax } from "../functions/fetchProductGMVMax.js";
import { fetchLiveGMVMax } from "../functions/fetchLiveGMVMax.js";
import { handleTiktokAdsData } from "../functions/handleTiktokAdsData.js";
import { fetchPGMVMaxBreakdown } from "../functions/fetchPGMVMaxBreakdown.js";
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from "../functions/walletTransactions.js";
import { mainDanaDilepas } from "../functions/escrowProcessor.js";

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.SHRD_PARTNER_ID);
export const PARTNER_KEY = process.env.SHRD_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.SHRD_SHOP_ID);
export const SHRD_INITIAL_ACCESS_TOKEN = process.env.SHRD_INITIAL_ACCESS_TOKEN;
export const SHRD_INITIAL_REFRESH_TOKEN = process.env.SHRD_INITIAL_REFRESH_TOKEN;
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";

export const HOST = "https://partner.shopeemobile.com";
const PATH = "/api/v2/order/get_order_list";

export let SHRD_ACCESS_TOKEN;
let SHRD_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: SHRD_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint SHRD: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        SHRD_ACCESS_TOKEN = newAccessToken;
        SHRD_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: SHRD_ACCESS_TOKEN,
            refreshToken: SHRD_REFRESH_TOKEN
        });
    } else {
        console.log("[SHRD] token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/shrd-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[SHRD] Saved tokens to SHRD Secret Manager");
    } catch (e) {
        console.log("[SHRD] Error saving tokens to Secret Manager", )
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/shrd-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("[SHRD] Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.log("[SHRD] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersSHRD() {
    console.log("[SH-RD] Start fetching ads total balance. Calling the function.");
    let brand = "SH-RD";
    let brandTT = "SHRD";

    const loadedTokens = await loadTokensFromSecret();
    SHRD_ACCESS_TOKEN = loadedTokens.accessToken;
    SHRD_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, SHRD_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, SHRD_ACCESS_TOKEN, SHOP_ID)
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, SHRD_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 2000);

    let adsIdSHRD = "7377330420947632145";
    const basicAdsData = await fetchTiktokBasicAds(brandTT, adsIdSHRD);
    const pgmvMaxData = await fetchProductGMVMax(brandTT, adsIdSHRD);
    const lgmvMaxData = await fetchLiveGMVMax(brandTT, adsIdSHRD);
    
    console.log("[SHRD] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brandTT);

    await fetchPGMVMaxBreakdown(brandTT, adsIdSHRD);
}

```

## File: workers\sv_processor.js
```
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';
import axios, { all } from 'axios';
import crypto from 'crypto';
import { fetchAdsTotalBalance } from '../functions/fetchAdsTotalBalance.js';
import { fetchGMVMaxSpending } from '../functions/fetchGMVMaxSpending.js';
import { fetchTiktokBasicAds } from '../functions/fetchTiktokBasicAds.js';
import { fetchProductGMVMax } from '../functions/fetchProductGMVMax.js';
import { fetchLiveGMVMax } from '../functions/fetchLiveGMVMax.js';
import { handleTiktokAdsData } from '../functions/handleTiktokAdsData.js';
import { fetchPGMVMaxBreakdown } from '../functions/fetchPGMVMaxBreakdown.js';
import { fetchAffiliateData } from '../functions/amsProcessor.js';
import { handleWalletTransactions } from '../functions/walletTransactions.js';
import { mainDanaDilepas } from '../functions/escrowProcessor.js';

const secretClient = new SecretManagerServiceClient();

export const PARTNER_ID = parseInt(process.env.SV_PARTNER_ID);
export const PARTNER_KEY = process.env.SV_PARTNER_KEY;
export const SHOP_ID = parseInt(process.env.SV_SHOP_ID);
const REFRESH_ACCESS_TOKEN_URL = "https://partner.shopeemobile.com/api/v2/auth/access_token/get";
export const HOST = "https://partner.shopeemobile.com";

export let SV_ACCESS_TOKEN;
let SV_REFRESH_TOKEN;

async function refreshToken() {
    const path = "/api/v2/auth/access_token/get";
    const timestamp = Math.floor(Date.now() / 1000);
    const baseString = `${PARTNER_ID}${path}${timestamp}`;
    const sign = crypto.createHmac('sha256', PARTNER_KEY)
        .update(baseString)
        .digest('hex');
    
    const fullUrl = `${REFRESH_ACCESS_TOKEN_URL}?partner_id=${PARTNER_ID}&timestamp=${timestamp}&sign=${sign}`;

    const body = {
        refresh_token: SV_REFRESH_TOKEN,
        partner_id: PARTNER_ID,
        shop_id: SHOP_ID
    }

    console.log("Hitting Refresh Token endpoint SV: ", fullUrl);

    const response = await axios.post(fullUrl, body, {
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const newAccessToken = response.data.access_token;
    const newRefreshToken = response.data.refresh_token;

    if(newAccessToken && newRefreshToken) {
        SV_ACCESS_TOKEN = newAccessToken;
        SV_REFRESH_TOKEN = newRefreshToken;

        saveTokensToSecret({
            accessToken: SV_ACCESS_TOKEN,
            refreshToken: SV_REFRESH_TOKEN
        });
    } else {
        console.log("[SV] Token refresh not found :(")
        throw new Error("Tokens dont exist");
    }
}

async function saveTokensToSecret(tokens) {
    const parent = 'projects/231801348950/secrets/sv-shopee-tokens';
    const payload = Buffer.from(JSON.stringify(tokens, null, 2), 'utf-8');

    try {
        const [newVersion] = await secretClient.addSecretVersion({
            parent: parent,
            payload: {
                data: payload,
            }
        });

        console.log("Saved Shopee tokens to Secret Manager");

        // Destroying previous token version
        const [versions] = await secretClient.listSecretVersions({
            parent: parent
        });

        for (const version of versions) {
            if (version.name !== newVersion.name && version.state !== 'DESTROYED') {
                try {
                    await secretClient.destroySecretVersion({
                        name: version.name
                    });
                    console.log(`Destroyed old token version: ${version.name}`);
                } catch (destroyError) {
                    console.error(`Failed to destroy version ${version.name}:`, destroyError);
                }
            }
        }
        console.log("[SV] Successfully saved tokens to SV Secret Manager: ", parent);
    } catch (e) {
        console.error("[SV] Error saving tokens to Secret Manager: ", e);
    }
}

async function loadTokensFromSecret() {
    const secretName = 'projects/231801348950/secrets/sv-shopee-tokens/versions/latest';

    try {
        const [version] = await secretClient.accessSecretVersion({
            name: secretName,
        });
        const data = version.payload.data.toString('UTF-8');
        const tokens = JSON.parse(data);
        console.log("Tokens loaded from Secret Manager: ", tokens);
        return tokens;
    } catch (e) {
        console.error("[SV] Error loading tokens from Secret Manager: ", e);
    }
}

export async function fetchAndProcessOrdersSV() {
    console.log("Starting fetch orders SV");
    let brand = "Swissvita";

    const loadedTokens = await loadTokensFromSecret();
    SV_ACCESS_TOKEN = loadedTokens.accessToken;
    SV_REFRESH_TOKEN = loadedTokens.refreshToken;

    await refreshToken();

    await mainDanaDilepas(brand, PARTNER_ID, PARTNER_KEY, SV_ACCESS_TOKEN, SHOP_ID);
    await handleWalletTransactions(brand, PARTNER_ID, PARTNER_KEY, SV_ACCESS_TOKEN, SHOP_ID);
    await fetchAdsTotalBalance(brand, PARTNER_ID, PARTNER_KEY, SV_ACCESS_TOKEN, SHOP_ID);

    await fetchAffiliateData(brand, SHOP_ID, 7000);

    // For backfilling
    let advIdEvoke = "7374337917889953808"

    let advIdSwissvita = "7431385715176554497"

    let advertiserId = advIdSwissvita;

    const basicAdsData = await fetchTiktokBasicAds(brand, advertiserId);
    const pgmvMaxData = await fetchProductGMVMax(brand, advertiserId);
    const lgmvMaxData = await fetchLiveGMVMax(brand, advertiserId);
    
    console.log("[SWISSVITA] All data on: ", brand);
    console.log(basicAdsData);
    console.log(pgmvMaxData);
    console.log(lgmvMaxData);
    console.log("\n");

    await handleTiktokAdsData(basicAdsData, pgmvMaxData, lgmvMaxData, brand);

    await fetchPGMVMaxBreakdown(brand, advertiserId);
}

```

