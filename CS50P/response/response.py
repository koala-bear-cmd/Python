import validators

email = input("please enter your email:").strip()

if validators.email(email):
  print('valid')
else:
  print('invalid')
