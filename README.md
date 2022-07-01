<!-- 模板文件 -->


## 运行服务

```shell
export FLASK_APP=service

python -m flask run -p 5000 -h 0.0.0.0
```

## 生成短链接

### `POST` **/short_url**

> Headers:

名称           | 必须   |  说明
--            | :--:   |  --
Content-Type  |  y     |  application/json

> Json Parameters:

参数名     |   必须   |  说明
--        |   :--:   |  --
url       |    y     |  url地址 

> Request:
        
    {
        "short_url": "https://github.com/xionzhi"
    }


> Response:

    {
        "short_url": "https://xxx.com/qaM"
    }
