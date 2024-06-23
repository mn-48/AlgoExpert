# O(n) Time | O(n) Space

def caesarCipherEncryptor(string, key):
    return "".join([chr(((ord(c)-97 + key)%26)+97)for c in string])


if __name__=="__main__":
    ans = caesarCipherEncryptor("xyz", 2)
    print(ans)