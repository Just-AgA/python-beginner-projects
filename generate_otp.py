#Generate 6 digit random secure OTP

#We import the secrets module
import secrets

#Generate a class instance of the secrets class
gen_num = secrets.SystemRandom()

#Generate the OTP by using the randrange() method of the above object
otp = gen_num.randrange(100000, 999999)

print(otp)