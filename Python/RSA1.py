from wolfcrypt.ciphers import RsaPrivate, RsaPublic
from wolfcrypt.utils import h2b

private = ("3082025C02010002818100BC730EA849F374A2A9EF18A5DA559921F9C8ECB36D" +
           "48E53535757737ECD161905F3ED9E4D5DF94CAC1A9D719DA86C9E84DC4613682" +
           "FEABAD7E7725BB8D11A5BC623AA838CC39A20466B4F7F7F3AADA4D020EBB5E8D" +
           "6948DC77C9280E22E96BA426BA4CE8C1FD4A6F2B1FEF8AAEF69062E5641EEB2B" +
           "3C67C8DC2700F6916865A902030100010281801397EAE8387825A25C04CE0D40" +
           "7C31E5C470CD9B823B5809863B665FDC3190F14FD5DB15DDDED73B9593311831" +
           "0E5EA3D6A21A716E81481C4BCFDB8E7A866132DCFB55C1166D279224458BF1B8" +
           "48B14B1DACDEDADD8E2FC291FBA5A96EF83A6AF1FD5018EF9FE7C3CA78EA56D3" +
           "D3725B96DD4E064E3AC3D9BE72B66507074C01024100FA47D47A7C923C55EF81" +
           "F041302DA3CF8F1CE6872705700DDF9835D6F18B382F24B5D084B6794F712994" +
           "5AF0646AACE772C6ED4D59983E673AF3742CF9611769024100C0C1820D0CEBC6" +
           "2FDC92F99D821A31E9E9F74BF282871CEE166AD11D188270F3C0B62FF6F3F71D" +
           "F18623C84EEB8F568E8FF5BFF1F72BB5CC3DC657390C1B54410241009D7E05DE" +
           "EDF4B7B2FBFC304B551DE32F0147966905CD0E2E2CBD8363B6AB7CB76DCA5B64" +
           "A7CEBE86DF3B53DE61D21EEBA5F637EDACAB78D94CE755FBD71199C102401898" +
           "1829E61E2739702168AC0A2FA172C121869538C65890A0579CBAE3A7B115C8DE" +
           "F61BC2612376EFB09D1C44BE1343396717C89DCAFBF545648B38822CF2810240" +
           "3989E59C195530BAB7488C48140EF49F7E779743E1B419353123759C3B44AD69" +
           "1256EE0061641666D37C742B15B4A2FEBF086B1A5D3F9012B105863129DBD9E2")

public = (
    "30819F300D06092A864886F70D010101050003818D0030818902818100BC730E" +
    "A849F374A2A9EF18A5DA559921F9C8ECB36D48E53535757737ECD161905F3ED9" +
    "E4D5DF94CAC1A9D719DA86C9E84DC4613682FEABAD7E7725BB8D11A5BC623AA8" +
    "38CC39A20466B4F7F7F3AADA4D020EBB5E8D6948DC77C9280E22E96BA426BA4C" +
    "E8C1FD4A6F2B1FEF8AAEF69062E5641EEB2B3C67C8DC2700F6916865A90203010001")

prv = RsaPrivate(h2b(private))
pub = RsaPublic(h2b(public))

plaintext = "AgentBlueServer: :GetActiveHosts:JU13Tm0jqU1V2YAs:e9a7d3a0b6381315900b6539078a106e966c14c14e3006912260aa6572110d0a"
ciphertext = pub.encrypt(plaintext)
deciphertext = prv.decrypt(ciphertext)
print(deciphertext.decode("utf-8"), end="\n\n")

print(deciphertext.hex(), end="\n\n")
print(bytes.fromhex(deciphertext.hex()).decode("utf-8"), end="\n\n")

# signature = prv.sign(plaintext)

# print(signature, end='\n\n')
# print(signature.hex(), end='\n\n')
# print(bytes.fromhex(signature.hex()), end='\n\n')
# print(pub.verify(signature), end='\n\n'))
print(
    deciphertext.decode("utf-8") == bytes.fromhex(deciphertext.hex()).decode(
        "utf-8"))
