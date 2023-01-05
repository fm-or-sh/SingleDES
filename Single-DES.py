from Crypto.Cipher import DES #import Crypto library
from Crypto.Util.Padding import pad, unpad # import pad and unpad for matching upoto block size
import os
import argparse #importing libray for handling input parameter
BLOCK_SIZE = 8 # Declaring block size for DES required
parser = argparse.ArgumentParser(prefix_chars='-') # Declaring how in parameters will be identified
parser.add_argument('-k', '--key',dest='key',help='Key to encrypt or decrypt. It should be 8 byte value.') # Setting parameter for key
parser.add_argument('-f', '--file',dest='file',help='File to encrypt or decrypt') # Setting parameter for file input
parser.add_argument('-a', '--action',dest='action',help='Action whether user want to encrypt or decrypt Example: e or d') # Setting parameter for action

args = parser.parse_args()
key_length=len(args.key)


if key_length != 8 or os.path.exists(args.file) == False:
    print("\n-------------------Prepared by----------------------\n---------------------FM-or-SH----------------------\n\n*For help type -h or --help as command line argument*\n")
else :
    key = args.key.encode() # Encoding key parameter value
    des = DES.new(key, DES.MODE_ECB) # Creating new object for Single DES encryption by passing the key value
    print("\n-------------------Prepared by----------------------\n---------------------FM-or-SH----------------------\n\n*For help type -h or --help as command line argument*\n")
    def encrypt_data() :
        open_plaintext_file = open(args.file,'r') # Opening the plaintext file as read mode
        plaintext_read=open_plaintext_file.read()
        open_plaintext_file.close()
        print(f'-------------Plain text to be encrypted-------------\n\n{plaintext_read}\n')
        print(f'-------------Key used to encrypt: {args.key}--------\n')
                
        padded_text = pad(plaintext_read.encode(), BLOCK_SIZE) #Paddign the data collected from plain text file to match to block size
        ciphertext = des.encrypt(padded_text) # Encrypting data
        open_cipher_text_file = open('cipher.txt','wb') 
        open_cipher_text_file.write(ciphertext)    # Writing Encrypting data to file (in byte)
        
        
        open_cipher_text_file.close()
        print(f'-------------Cipher text (as Byte) after encryption------------\n\n{ciphertext}\n')

    def decrypt_data():
        open_cipher_text_file = open(args.file,'rb')
        ciphertext_read=open_cipher_text_file.read()
        open_cipher_text_file.close()
        print(f'-------------Cipher text (as Byte) to be decrypted------\n\n{ciphertext_read}\n')
        print(f'-------------Key used to decrypt: {args.key}------------\n')
        plaintext_unpad = des.decrypt(ciphertext_read)
        plaintext=unpad(plaintext_unpad,BLOCK_SIZE).decode() # Unpaddign the data collected from plain text output after decryption 
        open_plaintext_file = open('plain.txt','w')
        open_plaintext_file.write(str(plaintext)) # Writing plaintext data to file
        open_plaintext_file.close()
        print(f'-------------Plain text after decryption-------------\n\n{plaintext}\n')


    if args.action == 'e':  # Depending on action value
        encrypt_data()
    elif args.action == 'd':
        decrypt_data()
    