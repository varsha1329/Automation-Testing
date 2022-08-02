from re import sub

def camel_abc(y):
  y = sub(r"(_|-)+", " ", y).title().replace(" ", "")
  return ''.join([y[0].lower(), y[1:]])
print(camel_abc('JavaScript'))
print(camel_abc('Foo-Bar'))
print(camel_abc('foo_bar'))
print(camel_abc('--foo.bar'))
print(camel_abc('Foo-BAR'))
print(camel_abc('fooBAR'))
print(camel_abc('foo bar'))