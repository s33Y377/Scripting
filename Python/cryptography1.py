from cryptography.fernet import Fernet
import base64
import ast

cipher_suite = Fernet(b"aILUSO3LVDVDH7DJxsQmqGO15-0E5jIbI4bm6EAGzcw=")
a = "{'agent': 'NII-LT-410', 'query': 'ServiceList', 'passphrase': b'dc00a3a9b8973c3ada34338217515a9a43f949d0eb64b21eb99803c0a31355f9', 'secret_key': '3NNhDUlWq3oH02E4'}"
cipher_text = base64.b64encode(cipher_suite.encrypt(a.encode("utf-8")))
# print("cipher_text", cipher_suite.encrypt(a.encode('utf-8')))
print("cipher_text_base64", cipher_text, end="\n\n")
print(
    "plain_text",
    ast.literal_eval(
        cipher_suite.decrypt(base64.b64decode(cipher_text)).decode("utf-8")
    ),
)
# print("plain_text", type(ast.literal_eval(plain_text.decode('utf-8'))))
