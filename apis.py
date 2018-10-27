from collections import OrderedDict

## actual order...
#[('crypto/keygenerator', ['generateKey']), ('activitymanager', ['restartpackage']), ('assetmanager', ['getassets']), ('audiorecord', ['startrecording']), ('android/provider/contacts', ['NONE']), ('uuid', ['tostring']), ('audiomanager', ['setvibratesetting', 'setringermode']), ('gsm/smsmanager', ['sendtextmessage', 'createfrompdu', 'getdisplaymessagebody']), ('system', ['load', 'loadlibrary']), ('dexclassloader', ['loadclass']), ('environment', ['getexternalstoragedirectory', 'getexternalstoragestate']), ('smsmanager', ['getdefault', 'sendtextmessage', 'createfrompdu', 'getdisplaymessagebody', 'getmessagebody', 'getoriginatingaddress', 'getuserdata']), ('pendingintent', ['getbroadcast', 'abortbroadcast']), ('deviceadminreceiver', ['NONE']), ('zipoutputstream', ['close']), ('urlconnection', ['getinputstream', 'getoutputstream']), ('string', ['equalsignorecase', 'split']), ('jsonobject', ['put']), ('reflect/accessibleobject', ['setaccessible']), ('secureclassloader', ['NONE']), ('android/provider/calllog$calls', ['NONE']), ('client/defaulthttpclient', ['execute']), ('crypto/cipher', ['dofinal', 'getinstance']), ('mediarecorder', ['start', 'stop']), ('/browser$', ['NONE']), ('telephony/itelephony', ['endcall']), ('client/httpclient', ['execute']), ('wifimanager', ['getconnectioninfo', 'getwifistate']), ('wifiinfo', ['getmacaddress']), ('devicepolicymanager', ['isadminactive', 'locknow']), ('telephonymanager', ['getdeviceid', 'getline1number', 'getnetworkoperator', 'getsimoperatorname', 'getsimserialnumber', 'getsubscriberid', 'getcallstate']), ('audio/media', ['getcontenturiforpath']), ('fileoutputstream', ['NONE']), ('httpurlconnection', ['getoutputstream']), ('urlclassloader', ['NONE']), ('locationmanager', ['getlastknownlocation', 'requestlocationupdates']), ('secretkeyspec', ['NONE']), ('video$media', ['getcontenturi', 'getcontentresolver']), ('sslhttpsurlconnection', ['getoutputstream']), ('images$media', ['getcontenturi', 'insertimage', 'getbitmap']), ('contentresolver', ['query', 'delete']), ('android/provider/contacts$phones', ['NONE']), ('class', ['getdeclaredmethod']), ('runtime', ['exec', 'getruntime']), ('android/provider/contactscontract$commondatakinds$phone', ['NONE']), ('uri', ['parse']), ('context', ['getsystemservice']), ('packagemanager', ['setcomponentenabledsetting'])]
#

suspicious_api_dict = OrderedDict({
    'telephonymanager':[
        'getdeviceid', 'getline1number','getnetworkoperator','getsimoperatorname',
        'getsimserialnumber','getsubscriberid','getcallstate'
    ],
    'uuid':['tostring'],
    'wifiinfo':['getmacaddress'],
    'wifimanager':['getconnectioninfo','getwifistate'],
    'locationmanager':['getlastknownlocation','requestlocationupdates'],
    'contentresolver':['query','delete'],
    '/browser$':['NONE'],
    'android/provider/calllog$calls':['NONE'],
    'android/provider/contacts$phones':['NONE'],
    'android/provider/contactscontract$commondatakinds$phone':['NONE'],
    'android/provider/contacts':['NONE'],
    'audio/media':['getcontenturiforpath'],
    'images$media':['getcontenturi','insertimage','getbitmap'],
    'video$media':['getcontenturi','getcontentresolver'],
    'uri':['parse'],
    'smsmanager':[
        'getdefault','sendtextmessage','createfrompdu','getdisplaymessagebody',
        'getmessagebody','getoriginatingaddress','getuserdata'
    ],
    'gsm/smsmanager':['sendtextmessage','createfrompdu','getdisplaymessagebody'],
    'telephony/itelephony':['endcall'],
    'audiorecord':['startrecording'],
    'mediarecorder':['start','stop'],
    'httpurlconnection':['getoutputstream'],
    'urlconnection':['getinputstream','getoutputstream'],
    'sslhttpsurlconnection':['getoutputstream'],
    'client/httpclient':['execute'],
    'client/defaulthttpclient':['execute'],
    'jsonobject':['put'],
    'devicepolicymanager':['isadminactive','locknow'],
    'deviceadminreceiver':['NONE'],
    'assetmanager':['getassets'],
    'dexclassloader':['loadclass'],
    'secureclassloader':['NONE'],
    'urlclassloader':['NONE'],
    'runtime':['exec','getruntime'],
    'system':['load','loadlibrary'],
    'crypto/cipher':['dofinal','getinstance'],
    'crypto/keygenerator':['generateKey'],
    'secretkeyspec':['NONE'],
    'class':['getdeclaredmethod'],
    'reflect/accessibleobject':['setaccessible'],
    'pendingintent':['getbroadcast','abortbroadcast'],
    'fileoutputstream':['NONE'],
    'zipoutputstream':['close'],
    'packagemanager':['setcomponentenabledsetting'],
    'environment':['getexternalstoragedirectory','getexternalstoragestate'],
    'string':['equalsignorecase','split'],
    'activitymanager':['restartpackage'],
    'audiomanager':['setvibratesetting','setringermode'],
    'context':['getsystemservice'],
})
