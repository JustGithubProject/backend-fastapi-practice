from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(password, hash_password):
    return pwd_context.verify(password, hash_password)