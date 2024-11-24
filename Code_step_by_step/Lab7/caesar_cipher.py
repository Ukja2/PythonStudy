"""
Caesar 암호(또는 회전 암호)를 구현하는 프로그램을 작성히시오 
사용자가 메시지와 암호화 키(문자를 몇 자리 이동할지)를 입력하면, 해당 키만큼 문자를 이동시켜 암호화된 메시지를 출력한다.

출력 예시:
Your message? Attack zerg at dawn
Encoding key? 3
DWWDFN CHUJ DW GDZQ

Your message? DWWDFN CHUJ DW GDZQ
Encoding key? -3
ATTACK ZERG AT DAWN
"""
def caesar_cipher(message, key):
    result = ""
    message = message.upper()  

    for i in message:
        if 'A' <= i <= 'Z':  
            shift = ord(i) + key  
            if shift > ord('Z'):  
                shift = shift - 26
            elif shift < ord('A'):
                shift = shift + 26
            result += chr(shift)  
        else:
            result += i

    return result


message = input("Your message? ")
key = int(input("Encoding key? "))


print(caesar_cipher(message, key))
