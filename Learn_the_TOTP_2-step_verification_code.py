import pyotp
import time

# TOTP Secret Key (Usually in Base32 format, e.g.: “JBSWY3DPEHPK3PXP”)
secret_key = "<Your_TOTP_secret_key>"

# Create a TOTP object
totp = pyotp.TOTP(secret_key)

# Get the current TOTP 2-step verification code
current_code = totp.now()
print("The current TOTP 2-step verification code:", current_code)