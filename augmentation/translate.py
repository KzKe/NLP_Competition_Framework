class Translate:

  def __init__(self, df, secretKey=None, appid=None):
    self.df = df
    # self.text_col = text_col
    self.secretKey = secretKey
    self.appid = appid

  def translate_forward(self, fromLang, toLang, text_col):
      tranlated = []
      httpClient = None
      myurl = '/api/trans/vip/translate'
      salt = random.randint(32768, 65536)
      
      for q in self.df[text_col]:
          # print(q)
          sign = appid + q + str(salt) + secretKey
          sign = hashlib.md5(sign.encode()).hexdigest()
          myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
          salt) + '&sign=' + sign

          try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            # print(result)

            temp = str(result['trans_result'][0]['dst'])
            # print(temp)
            tranlated.append(temp)

          except Exception as e:
              print (e)
          finally:
              if httpClient:
                  httpClient.close()
        
      return tranlated


  def translate(self, fromLang, toLang, text_col):
      tranlated = self.translate_forward(fromLang, toLang, text_col)
      self.df['tranlated'] = tranlated
      back_tranlated = self.translate_forward(toLang, fromLang, 'tranlated')
      self.df['back_tranlated'] = back_tranlated
      
      return self.df


# baidu api: https://fanyi-api.baidu.com/api/trans/product/desktop?req=detail
appid = ''  # 填写你的appid
secretKey = ''  # 填写你的密钥

trans = Translate(df=new_data, 
                  # text_col='comment',
                  secretKey = secretKey, 
                  appid=appid)



result = trans.translate(fromLang='zh', toLang='en', text_col='comment')