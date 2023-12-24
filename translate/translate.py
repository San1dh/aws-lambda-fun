import json
import boto3

translate_client = boto3.client('translate')

langs = {'af' : 'Afrikaans',
'sq'    : 'Albanian',
'am'    : 'Amharic',
'ar'    : 'Arabic',
'hy'    : 'Armenian',
'az'    : 'Azerbaijani',
'bn'    : 'Bengali',
'bs'    : 'Bosnian',
'bg'    : 'Bulgarian',
'ca'    : 'Catalan',
'zh'    : 'Chinese (Simplified)',
'zh-TW' : 'Chinese (Traditional)',
'hr'    : 'Croatian',
'cs'    : 'Czech',
'da'    : 'Danish',
'fa-AF' : 'Dari',
'nl'    : 'Dutch',
'en'    : 'English',
'et'    : 'Estonian',
'fa'    : 'Farsi (Persian)',
'tl'    : 'Filipino Tagalog',
'fi'    : 'Finnish',
'fr'    : 'French',
'fr-CA' : 'French (Canada)',
'ka'    : 'Georgian',
'de'    : 'German',
'el'    : 'Greek',
'gu'    : 'Gujarati',
'ht'    : 'Haitian Creole',
'ha'    : 'Hausa',
'he'    : 'Hebrew',
'hi'    : 'Hindi',
'hu'    : 'Hungarian',
'is'    : 'Icelandic',
'id'    : 'Indonesian',
'ga'    : 'Irish',
'it'    : 'Italian',
'ja'    : 'Japanese',
'kn'    : 'Kannada',
'kk'    : 'Kazakh',
'ko'    : 'Korean',
'lv'    : 'Latvian',
'lt'    : 'Lithuanian',
'mk'    : 'Macedonian',
'ms'    : 'Malay',
'ml'    : 'Malayalam',
'mt'    : 'Maltese',
'mr'    : 'Marathi',
'mn'    : 'Mongolian',
'no'    : 'Norwegian (Bokmål)',
'ps'    : 'Pashto',
'pl'    : 'Polish',
'pt'    : 'Portuguese (Brazil)',
'pt-PT' : 'Portuguese (Portugal)',
'pa'    : 'Punjabi',
'ro'    : 'Romanian',
'ru'    : 'Russian',
'sr'    : 'Serbian',
'si'    : 'Sinhala',
'sk'    : 'Slovak',
'sl'    : 'Slovenian',
'so'    : 'Somali',
'es'    : 'Spanish',
'es-MX' : 'Spanish (Mexico)',
'sw'    : 'Swahili',
'sv'    : 'Swedish',
'ta'    : 'Tamil',
'te'    : 'Telugu',
'th'    : 'Thai',
'tr'    : 'Turkish',
'uk'    : 'Ukrainian',
'ur'    : 'Urdu',
'uz'    : 'Uzbek',
'vi'    : 'Vietnamese',
'cy'    : 'Welsh'}

comp = boto3.client('comprehend')

def lambda_handler(event, context):
    # TODO implement
    
    text = '''  Es un buen día.'''
    # text = input()
    
    res = comp.detect_dominant_language(Text=text)
    maxx = 0
    for lang in res["Languages"]:
        if lang["Score"] > maxx:
            maxx = lang["Score"]
            dom = lang["LanguageCode"]
    # print(json.dumps(lang, indent = 1))
    # print('Dominant Language: ' + dom + " " + str(maxx))
    print("---------------------")
    print("Text: ", text)
    print('DominantLanguage: ')
    print(langs[dom])
    print(round(maxx*100, 2))
    result = comp.detect_sentiment(Text = text, LanguageCode = dom)
    # print(json.dumps(result, indent = 3))
    print("Sentiment: ")
    # print(result["Sentiment"])
    x = result["Sentiment"]
    x = x.lower()
    x = x.capitalize()
    print(x)
    print(round(result["SentimentScore"][x]*100, 2))
    # print("hello: " + dom)
    result = translate_client.translate_text(Text=text, SourceLanguageCode="ml", TargetLanguageCode="en")
    print('TranslatedText: ' + result.get('TranslatedText'))
    print("---------------------")

# o/p
# ---------------------
# Text:    Es un buen día.
# DominantLanguage: 
# Spanish
# 99.97
# Sentiment: 
# Positive
# 99.66
# TranslatedText: It's a good day.
# ---------------------

    # text = ''' 
    #             Entrevista amb el portaveu d'Amazon, Jeff Barr, que explica que ja pot fer presentacions des del món virtual Second Life i no li cal fer-les presencialment. 
    #             Barr no s'ha mullat sobre la possibilitat que Amazon faci servir el català.
    #         '''

    # result = translate_client.translate_text(Text=text, SourceLanguageCode="ml", TargetLanguageCode="en")
    # print('TranslatedText: ' + result.get('TranslatedText'))

# o/p
# TranslatedText:  
# Interview with Amazon spokesman Jeff Barr, who explains that he can now make presentations from the Second Life virtual world and does not need to do them in person. 
# Barr hasn't gotten wet on the possibility of Amazon using Catalan.




  
# Language	        Language code

# Afrikaans	            af
# Albanian	            sq
# Amharic	            am
# Arabic	            ar
# Armenian	            hy
# Azerbaijani	        az
# Bengali	            bn
# Bosnian	            bs
# Bulgarian	            bg
# Catalan	            ca
# Chinese (Simplified)	zh
# Chinese (Traditional)	zh-TW
# Croatian	            hr
# Czech	                cs
# Danish	            da
# Dari	                fa-AF
# Dutch	                nl
# English	            en
# Estonian	            et
# Farsi (Persian)	    fa
# Filipino, Tagalog	    tl
# Finnish	            fi
# French	            fr
# French (Canada)	    fr-CA
# Georgian	            ka
# German	            de
# Greek	                el
# Gujarati	            gu
# Haitian Creole	    ht
# Hausa	                ha
# Hebrew	            he
# Hindi	                hi
# Hungarian	            hu
# Icelandic	            is
# Indonesian	        id
# Irish	                ga
# Italian	            it
# Japanese	            ja
# Kannada	            kn
# Kazakh	            kk
# Korean	            ko
# Latvian	            lv
# Lithuanian	        lt
# Macedonian	        mk
# Malay	                ms
# Malayalam	            ml
# Maltese	            mt
# Marathi	            mr
# Mongolian	            mn
# Norwegian (Bokmål)	no
# Pashto	            ps
# Polish	            pl
# Portuguese (Brazil)	pt
# Portuguese (Portugal)	pt-PT
# Punjabi	            pa
# Romanian	            ro
# Russian	            ru
# Serbian	            sr
# Sinhala	            si
# Slovak	            sk
# Slovenian	            sl
# Somali	            so
# Spanish	            es
# Spanish (Mexico)	    es-MX
# Swahili	            sw
# Swedish	            sv
# Tamil	                ta
# Telugu	            te
# Thai	                th
# Turkish	            tr
# Ukrainian	            uk
# Urdu	                ur
# Uzbek	                uz
# Vietnamese	        vi
# Welsh	                cy
