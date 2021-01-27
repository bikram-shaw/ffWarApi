from paytmchecksum import PaytmChecksum

# Generate Checksum via Hash/Array
# initialize an Hash/Array
paytmParams = {}
def GenerateChecksum(mid,oid):
    paytmParams["MID"] = mid
    paytmParams["ORDERID"] = oid
    paytmChecksum = PaytmChecksum.generateSignature(paytmParams, "E%mbk4m&7y6QOXvE")
    return str(paytmChecksum)

def VarifyChecksum(paytmChecksum):
    verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "E%mbk4m&7y6QOXvE",paytmChecksum)
    return str(verifyChecksum)



