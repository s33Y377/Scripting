from cryptography.fernet import Fernet
import base64
import ast
import sys

cipher_suite = Fernet(b"aILUSO3LVDVDH7DJxsQmqGO15-0E5jIbI4bm6EAGzcw=")
data = "Z0FBQUFBQmN3WVItanh0MHA0U1FNeGJuUVJEZ1RPQS02dV9HMDhKYmVuX25NRmNabENqcUdUZVdtUGhSWlY0UW55Wnk1RDJPc2dTODZqZnBNRE1oN0ZMSDFXbkhHTXYwOW5CeG5icE5MVnFTdWwwcHVYYktneEdBNnRQY1JKV1F2amtfUS1wU2l2YTlzZFd2dkM1RnIwSVQyUVd3dmdfdTJWcDF0WFpJY1o0Sk96ZGdvb0NGOU9rTHY1U01rQ1RzMmdDMEVQN3ZRalRnWk11d1dMN3hFQlhJOW9ueVdqNG44NnNkODdsdW9iYjQzajhxM0pYNUFlQVFqczV3b1pITC14VzB1MjhuUFZuel9MZUptUnhJNFQ2aVRvY1hsZ2h3clUxWUdSMVJKQVpwUjFGV3ItRFlKdGRmcHkzWkhDekJDSkFuTEZGYU5TU2g = : 5cc1847e689441d96fcef9aa: ServiceList: ZVQNWPQiRpUEsc2L: b'13e21ae5d4ee3bcf66f33fbb8a625cbff4b763c07f8fc6c7e86309f577caeca9'"
# print(data)
data = ast.literal_eval(cipher_suite.decrypt(
    base64.b64decode(data)).decode('utf-8'))
print(data)
print(sys.getsizeof(data))
print(type(data))
print(data['agent'])
