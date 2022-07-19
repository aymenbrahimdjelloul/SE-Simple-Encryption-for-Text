"""
@author : Aymen Brahim Djelloul
version : 0.1 demo
date : 2022.06.27


// 'SE' or 'SES' stand for Standard Encryption System //
Standard encryption system is a simple block cipher used for symmetric-key encryption.
it can be used with key or password

the way SE algorithm to work is to take values from the key or the password given with applying
mathematical ops than use those values on ciphering the plaintext was given.
the ciphering process apply in 16 rounds or great each round has a different ciphering values and it is by order.
so if you miss one order you will get a corrupted output does not match with the original data.

"""

import sys
import SHA_HASH


class new:

    def __init__(self, key, rounds=16):

        self.key = key
        self.rounds = rounds


    def encrypt(self, plaintext):
        """ this method will encrypt the given plaintext.
        using the given indexes in 16 round for each character
        """

        cipher_text = ""
        index_to_apply = self.get_cipher_indexes()
        x = 0

        for char in plaintext:
            rounds_counter = 0
            while rounds_counter != self.rounds:

                x = ord(char)

                x += index_to_apply[rounds_counter]

                rounds_counter += 1
            char = chr(x)
            cipher_text = cipher_text + char
        # clear variables
        del index_to_apply, x, char, plaintext, rounds_counter
        cipher_text = f'{self.get_password_hash()}{cipher_text}'

        return cipher_text


    def decrypt(self, ciphertext):
        """ this method will decrypt the given ciphertext"""

        # first calling the password verify method
        self.verify_authentication_key(ciphertext)

        plaintext = ''
        ciphertext = ciphertext[64:len(ciphertext)]
        index_to_apply = self.get_cipher_indexes()
        x = 0

        for cipher in ciphertext:
            rounds_counter = 0
            while rounds_counter != self.rounds:

                x = ord(cipher)
                x -= index_to_apply[rounds_counter]

                rounds_counter += 1

            char = chr(x)
            plaintext = plaintext + char
        # clear variables
        del cipher, ciphertext, x, rounds_counter, char

        return plaintext


    def get_cipher_indexes(self):
        """ this method will get index values for the ciphering process for 32 rounds"""

        indexes = []

        # get values from the key
        key_values = []
        for i in self.key: x = ord(i); key_values.append(x)

        # calculate p and q for the index value processing
        # than calculate the ciphering index
        y = 0

        round_index = 0
        while round_index != self.rounds:
            round_index += 1

            for i in key_values:
                y += (i - 1) ** (i - 1)
                y = (y - round_index) % (i * round_index)


            indexes.append(y)
        # clear memory from vars
        del round_index, i, key_values, y, x

        return indexes


    def get_password_hash(self):
        """ this method is for get the hashable password to use it in the encryption"""
        return SHA_HASH.SHA_256(self.key.encode('utf-8')).hex()


    def verify_authentication_key(self, content):
        """ this method is for verify the authentication of the given password and the byte of hash in the encrypted content"""

        password_hash = content[0:64]
        key_hashing = SHA_HASH.SHA_256(self.key.encode()).hex()

        if key_hashing == password_hash:
            pass
        elif self.key != password_hash:
            raise ValueError('Key Authentication Failed !')




if __name__ == "__main__":
    sys.exit()
