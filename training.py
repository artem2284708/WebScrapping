import codecs

text = '[\\xd0\\x9f\\xd1\\x80\\xd0\\xb8\\xd0\\xbf\\xd0\\xb5\\xd0\\xb2: KDDK & Fetty Wap]'
decoded_text = codecs.escape_decode(text.encode('latin-1'))[0].decode('utf-8')
print(decoded_text)

"""string = '[\\xd0\\x9f\\xd1\\x80\\xd0\\xb8\\xd0\\xbf\\xd0\\xb5\\xd0\\xb2: KDDK & Fetty Wap]'

string = string.encode().decode('utf-8')
res = "b'" + string + "'"
print(res)
dec = res.encode().decode('utf-8')
print(dec)"""
