import json
import boto3
# import csv

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
    
    text = '''  I live in a house near the mountains. 
                I have two brothers and one sister, and I was born last. 
                My father teaches mathematics, and my mother is a nurse at a big hospital. 
                My brothers are very smart and work hard in school. 
                My sister is a nervous girl, but she is very kind. 
                My grandmother also lives with us. 
                She came from Italy when I was two years old. 
                She has grown old, but she is still very strong. 
                She cooks the best food!
                
                My family is very important to me. 
                We do lots of things together. 
                My brothers and I like to go on long walks in the mountains. 
                My sister likes to cook with my grandmother. 
                On the weekends we all play board games together. 
                We laugh and always have a good time. 
                I love my family very much.    '''
    
    
    
    res = comp.detect_dominant_language(Text=text)
    maxx = 0
    for lang in res["Languages"]:
        if lang["Score"] > maxx:
            maxx = lang["Score"]
            dom = lang["LanguageCode"]
    print("---------------------------------------------------")
    print("Text: ", text)
    print('DominantLanguage: ')
    print(langs[dom])
    print(round(maxx*100, 2))
    result = comp.detect_key_phrases(Text = text, LanguageCode = dom)
    # print(json.dumps(result, indent = 3))
    print("KeyPhrases: ")
    i = 0
    for key in result["KeyPhrases"]:
        i += 1
        # print(key["Text"] + "\t", round(key["Score"]*100, 2))
        print("{: >20} {: >20} {: >20}".format(i, key["Text"], round(key["Score"]*100, 2)))
    # print("hello: " + dom)
    print("---------------------------------------------------")
    
# "errorMessage": "An error occurred (ValidationException) when calling the DetectKeyPhrases operation: 
#                   1 validation error detected: Value at 'languageCode' failed to satisfy constraint: 
#                       Member must satisfy enum value set: [hi, de, zh-TW, ko, pt, en, it, fr, zh, es, ar, ja]"    
    
    
    
    
    # text = ''' 
    #             Entrevista amb el portaveu d'Amazon, Jeff Barr, que explica que ja pot fer presentacions des del món virtual Second Life i no li cal fer-les presencialment. 
    #             Barr no s'ha mullat sobre la possibilitat que Amazon faci servir el català.
    #         '''
    # text = " Barr no s'ha mullat "
    # text = " Ninte per enthuva? "

    # result = translate_client.translate_text(Text=text, SourceLanguageCode="ml", TargetLanguageCode="en")
    # print('TranslatedText: ' + result.get('TranslatedText'))
    
