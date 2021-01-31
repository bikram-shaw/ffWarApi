from paytmchecksum import PaytmChecksum
import json
# Generate Checksum via Hash/Array
# initialize an Hash/Array
paytmParams = dict()
def GenerateChecksum(oid):

        
    paytmParams["body"] = {
       "requestType": "Payment",
       "mid": "eVExLv25221231925149",
       "websiteName": "WEBSTAGING",
       "orderId": oid,
       "callbackUrl": "https://merchant.com/callback",
       "userInfo": {
           "custId": "0154214"

    },
    }
    checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "E%mbk4m&7y6QOXvE")

    return str(checksum)

def VarifyChecksum(paytmChecksum):
    #verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "E%mbk4m&7y6QOXvE",paytmChecksum)
    #return str(verifyChecksum)
    pass



