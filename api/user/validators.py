import re

from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, CommonPasswordValidator, \
    NumericPasswordValidator
from django.core.exceptions import ValidationError


def get_username_validators():
    validators = [
        # ASCIIUsernameValidator(),
        CustomLengthValidator(1, 16),
    ]
    return validators


# def validate_username(username):
#     validators = get_username_validators()
#     errors = []
#     for validator in validators:
#         try:
#             validator.validate(username)
#         except ValidationError as error:
#             errors.append(error)
#     if errors:
#         raise ValidationError(errors)


def get_password_validators():
    validators = [
        CustomLengthValidator(8, 16),
        CommonPasswordValidator(),
        NumericPasswordValidator(),
    ]
    return validators


def validate_password(password):
    validators = get_password_validators()
    errors = []
    for validator in validators:
        try:
            validator.validate(password)
        except ValidationError as error:
            errors.append(error)
    if errors:
        raise ValidationError(errors)
    else:
        return True


# class ASCIIUsernameValidator:
#     def __init__(self):
#         regex = r'^[\w]+\Z'
#         self.p = re.compile(regex, re.ASCII)
#
#     def validate(self, username):
#         if not self.p.match(username):
#             msg = '영문, 숫자, 밑줄만 가능합니다.'
#             raise ValidationError(msg)


def string_trim_validator(username):
    length = len(username.strip())
    if length == 0:
        raise ValidationError({'msg': '문자를 입력해주세요.'})


def ascii_username_validator(username):
    regex = re.compile('^[\w.+-]+\Z')
    if not regex.match(username):
        raise ValidationError({'msg': '아이디는 영문, 숫자, "-", "_", "." 만으로 이루어져야 합니다.'})


def custom_length_validator(min_length, max_length, username):
    name_length = len(username)
    if name_length < min_length or name_length > max_length:
        msg = f'아이디는 최소 {min_length}, 최대 {max_length} 문자여야 합니다.'
        raise ValidationError({"msg": msg})


def email_verifier(username):
    regex = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if regex.match(username):
        return True
    return False


class CustomLengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, fields, user=None):
        if len(fields) < self.min_length:
            msg = f'최소 {self.min_length} 문자를 입력해주세요.'
            raise ValidationError(msg)
        if len(fields) > self.max_length:
            msg = f'최대 {self.max_length} 문자를 입력해주세요.'
            raise ValidationError(msg)