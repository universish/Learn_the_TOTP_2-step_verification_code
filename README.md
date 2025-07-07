# Learn_the_TOTP_2-step_verification_code

Step 1.

The pyotp library is required to calculate TOTP. Run the following command in Terminal / Command Prompt:

```
pip install pyotp
```

If pip is not running:

```
python -m pip install pyotp
```


Step 2:

Open Learn_the_TOTP_2-step_verification_code.py file with text editor. -->  Write the TOTP secret key in the Learn_the_TOTP_2-step_verification_code.py file. 

`secret_key = "<Your_TOTP_secret_key>"`

Usually in Base32 format. 
For example:
`secret_key = "JBSWY3DPEHPK3PXP"`

-->  Save and exit.

Step 3:

Open the terminal. Go to the directory where Learn_the_TOTP_2-step_verification_code.py is located:

`cd <directory_folder_name>`

Step 4:

Then paste the code and press Enter to run Python file (Learn_the_TOTP_2-step_verification_code.py).

```
python Learn_the_TOTP_2-step_verification_cod.py
```

The result will look like this:

`The current TOTP 2-step verification code: 123456`


Since the code will be refreshed, you have to run it again to learn each new code.

`python Learn_the_TOTP_2-step_verification_cod.py`
