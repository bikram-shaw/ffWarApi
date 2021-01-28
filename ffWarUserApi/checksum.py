from paytmchecksum import PaytmChecksum
import json
# Generate Checksum via Hash/Array
# initialize an Hash/Array

def GenerateChecksum(oid):
    paytmParams = dict()
        
    paytmParams["body"] = {
       "requestType": "Payment",
       "mid": "eVExLv25221231925149",
       "websiteName": "DEFAULT",
       "orderId": oid,
       "callbackUrl": "https://securegw.paytm.in/theia/paytmCallback?ORDER_ID="+oid,
       "userInfo": {
           "custId": "0154214"

    },
    }
    paytmChecksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "E%mbk4m&7y6QOXvE")

    return str(paytmChecksum)

def VarifyChecksum(paytmChecksum):
    #verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "E%mbk4m&7y6QOXvE",paytmChecksum)
    #return str(verifyChecksum)
    pass



