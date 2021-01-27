from paytmchecksum import PaytmChecksum

# Generate Checksum via Hash/Array
# initialize an Hash/Array
paytmParams = {}
def GenerateChecksum(mid,oid):
    paytmParams["MID"] = mid
    paytmParams["ORDERID"] = oid
    paytmChecksum = PaytmChecksum.generateSignature(paytmParams, "&PeD53l7mtZaDnx!")
    return str(paytmChecksum)

def VarifyChecksum(paytmChecksum):
    verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "&PeD53l7mtZaDnx!",paytmChecksum)
    return str(verifyChecksum)



