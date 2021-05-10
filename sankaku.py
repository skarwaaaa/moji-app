#関数化。デフォルトは日本語。
def transcribe_file(speech_file, lang='日本語'):#第2引数で言語設定。
  lang_code = {
      '英語':'en-US',
      '日本語':'ja-JP'
  }
  client = speech.SpeechClient()

  with io.open(speech_file, 'rb') as f:
    content = f.read()

  audio = speech.RecognitionAudio(content=content)
  config = speech.RecognitionConfig(
      encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
      #sample_rate_hertz=16000,
      language_code=lang_code[lang]
  )

  response = client.recognize(config=config, audio=audio)

  for result in response.results:
      print(result)#変換の精度を出力
      print("文字出力: {}".format(result.alternatives[0].transcript))