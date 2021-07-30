#project on OTP Generator
#Generate a 8 character OTP

import random as r
import string
length = 8
otp = ' '
characters = string.ascii_letters + string.digits

for i in range(length):
	 otp = otp + r.choice(characters)
print('your OTP is', otp)	 