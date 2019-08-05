"""
Learn about bytes.
Bytes are similar to str type, but they are a sequence
of bytes insteas of Unicode code points.

Use for raw binary data, fixed-width, single-byte encoding: ASCII

Use the byte() constructor
"""

d = b'data'
print(d,type(d))


info= b'some bytes here'
#split the bytes using the split() method

print(info.split())

# Encoding
message = "Vamos a1 zoológioo"
print(message)
data = message.encode("utf-8")
print(data)
dcoded = data.decode("utf-8")
print(dcoded)