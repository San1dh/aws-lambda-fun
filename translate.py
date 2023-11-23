import json
import boto3

translate_client = boto3.client('translate')

def lambda_handler(event, context):
    # TODO implement
    
    text = ''' 
                Entrevista amb el portaveu d'Amazon, Jeff Barr, que explica que ja pot fer presentacions des del món virtual Second Life i no li cal fer-les presencialment. 
                Barr no s'ha mullat sobre la possibilitat que Amazon faci servir el català.
            '''

    result = translate_client.translate_text(Text=text, SourceLanguageCode="ml", TargetLanguageCode="en")
    print('TranslatedText: ' + result.get('TranslatedText'))

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
