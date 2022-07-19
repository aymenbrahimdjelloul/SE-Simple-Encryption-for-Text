""" 
@author : Aymen Brahim Djelloul
date : 2022.06.27

// this project is still demo so if you face any bugs please you can tell us

"""

import SE
import time


def test():

    # define text to encrypt and the password 'encryption KEY'
    plain_text = 'this is a plaintext to test this encryption algorithm'
    password = "1234567890"

    """================= encryption ================="""
    # encrypt hello world
    start_time = time.perf_counter()

    encryption_object = SE.new(password)
    cipher = encryption_object.encrypt(plain_text)

    end_time = time.perf_counter()

    # print the encryption duration
    print(f'The Encryption : {cipher}	|	Finish in {round(end_time - start_time, 5)} Second')
    del encryption_object, start_time, end_time

    """================= decryption ================="""

    # now we will decrypt hello world after encryption
    start_time = time.perf_counter()


    encryption_object = SE.new(password)
    print(f'The Decryption : {encryption_object.decrypt(cipher)}	|	Finish in {round(time.perf_counter() - start_time, 5)} Second')


if __name__ == "__main__":
    test()
