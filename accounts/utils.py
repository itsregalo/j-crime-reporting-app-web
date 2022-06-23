from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
import random

class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active)+text_type(user.pk)+text_type(timestamp))
    
token_gen = AppTokenGenerator()



# generate random 6 int digit code
def generate_code():
    code = ''
    for i in range(6):
        code += str(random.randint(0, 9))
    return code
