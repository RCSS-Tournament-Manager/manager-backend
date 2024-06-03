from drf_spectacular.types import OpenApiTypes
# from drf_spectacular.utils import extend_schema, OpenApiExample

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.throttling import AnonRateThrottle
# from rest_framework.decorators import throttle_classes
# from rest_framework.decorators import (
#     api_view,
#     permission_classes,
# )
# from rest_framework_simplejwt.tokens import RefreshToken


# from django.utils.translation import gettext_lazy as _
# from django.utils.decorators import method_decorator
# from django.views.decorators.debug import sensitive_post_parameters

# from dj_rest_auth.serializers import JWTSerializer
# from dj_rest_auth.utils import jwt_encode


# from .utils import (
#     check_register_code,
# )
# from .response_models import (
#     CreatedResponse,
#     BadRequestResponse
# )
# from .serializers import (
#     RegistrationRequestSerializer,
#     RegisterWithCodeSerializer,
#     PhoneVerificationSendCodeSerializer,
#     PhoneVerifyCodeSerializer,
#     EmailVerificationSendCodeSerializer,
#     EmailVerifyCodeSerializer,
# )
# from .rate_limit import (
#     SendVerificationCodeThrottle,
#     VerifyCodeThrottle,
# )
# from .models import (
#     CustomUser,
#     RegistrationRequest,
#     InviteKey
# )
# from .helpers.registration_helpers import (
#     perform_create,
# )


# sensitive_post_parameters_m = method_decorator(sensitive_post_parameters('password'))


# @extend_schema(
#     request=RegistrationRequestSerializer,
#     responses={
#         status.HTTP_201_CREATED: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Your request has been submitted and is pending approval.'
#                 }
#             }
#         },
#         status.HTTP_400_BAD_REQUEST: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Invalid or expired registration key.'
#                 }
#             }
#         }
#     },
#     description="""
#     Submit a registration request.
    
#     Providing `key` or `message` is required. Both at same time is also allowed.
#     Providing `email` or `phone_number` is required. Both at same time is also allowed.
#     `email` or `phone_number` must be unique.
#     `email` `phone_number` will later be used for informing the user about the registration status.
    

#     - **parameters**:
#         - `email`: The email address for the user or registration request.
#         - `phone_number`: The phone number for the user or registration request.
#         - `key`: (Optional) A registration key if available.
#         - `message`: (Optional) A message to the admin regarding the registration request.
#     """,
#     summary="Request for registration.",
#     tags=['Registration'],
#     parameters=[],
#     examples=[
#         OpenApiExample(
#             'With email and message',
#             summary='',
#             value={
#                 'email': 'test@test.com',
#                 'message': 'I want to use the app.',
#             }
#         ),
#         OpenApiExample(
#             'With key',
#             summary='',
#             value={
#                 'email': 'test@test.com',
#                 'key': 'test',
#             },
#             request_only=True
#         ),
#     ],
#     auth=[],
# )
# @api_view(['POST'])
# @throttle_classes([AnonRateThrottle])
# @permission_classes([AllowAny])
# def registration_request_api(request):
#     serializer = RegistrationRequestSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     email = serializer.validated_data.get('email')
#     phone_number = serializer.validated_data.get('phone_number')
#     key = serializer.validated_data.get('key')
#     message = serializer.validated_data.get('message')

#     if key:
#         try:
#             invite_key = InviteKey.objects.get(key=key)
#             if invite_key.used >= invite_key.max_use:
#                 return Response({'detail': _('This registration key has already been used.')},
#                                 status=status.HTTP_400_BAD_REQUEST)

#             RegistrationRequest.objects.create(
#                 email=email,
#                 phone_number=phone_number,
#                 message=message,
#                 key=key,
#                 is_approved=False
#             )
#             invite_key.use()
#             return CreatedResponse(_('Your request has been submitted and is pending approval.'))
#         except InviteKey.DoesNotExist:
#             return BadRequestResponse(_('Invalid or expired registration key.'))

#     RegistrationRequest.objects.create(
#         email=email,
#         phone_number=phone_number,
#         message=message,
#         is_approved=False
#     )

#     return CreatedResponse(_('Your request has been submitted and is pending approval.'))


# @extend_schema(
#     request=RegisterWithCodeSerializer,
#     summary="Register with a registration code.",
#     description="""
#     Register a new account with an optional registration key or a message for the admin.
    
#     Providing `email` or `phone_number` is required. Both at same time is also allowed.
    
#     - **parameters**:
#         - `email`: The email address for the user or registration request.
#         - `phone_number`: The phone number for the user or registration request.
#         - `password`: The password for the user.
#         - `first_name`: The first name for the user.
#         - `last_name`: The last name for the user.
#         - `code`: A registration code if available.
#     """,
#     responses={
#         status.HTTP_201_CREATED: JWTSerializer,
#         status.HTTP_400_BAD_REQUEST: OpenApiTypes.OBJECT
#     },
#     examples=[
#         OpenApiExample(
#             'a normal request',
#             summary='',
#             value={
#                 'email': 'test@test.com',
#                 'phone_number': '+989123456789',
#                 'password': 'Testtest123!',
#                 'first_name': 'test',
#                 'last_name': 'test',
#                 'code': 'test',
#             },
#             request_only=True
#         ),
#     ],
#     tags=['Registration'],
#     auth=[],
# )
# @api_view(['POST'])
# @throttle_classes([AnonRateThrottle])
# @permission_classes([AllowAny])
# def register_with_code_api(request):
#     data = request.data.copy()

#     serializer = RegisterWithCodeSerializer(data=data)
#     serializer.is_valid(raise_exception=True)

#     # check if the code is valid
#     check_register_code(serializer.validated_data.get('code'))
#     user = perform_create(serializer)
#     token = jwt_encode(user)
#     out_data = {
#         'refresh': str(token[0]),
#         'access': str(token[1]),
#         'detail': _('Your account has been created.')
#     }
#     return Response(out_data, status=status.HTTP_201_CREATED)


# @extend_schema(
#     request=PhoneVerificationSendCodeSerializer,
#     summary="Send verification code to phone number.",
#     description="""
#     Send a verification code to the user's phone number.
#     The use must be authenticated.
#     Rate limit: 1/minute
#     If the phone number is different from the one in the user's profile, the phone number in the user's profile will be updated.
#     If the phone is already verified, the request will be ignored.
#     The phone number must be unique.
    
#     - **parameters**:
#         - `phone_number`: The phone number for the user, it could be null if user provided it before.
#             or it could be different from the one in the user's profile.
#     """,
#     responses={
#         status.HTTP_201_CREATED: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Verification code sent.'
#                 }
#             }
#         },
#         status.HTTP_400_BAD_REQUEST: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Invalid phone number.'
#                 }
#             }
#         }
#     },
#     examples=[
#         OpenApiExample(
#             'a normal request',
#             summary='',
#             value={
#                 'phone_number': '+989123456789',
#             },
#             request_only=True
#         ),
#     ],
#     tags=['Registration'],
#     auth=[],
# )
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @throttle_classes([SendVerificationCodeThrottle])
# def phone_code_send_api(request):
#     serializer = PhoneVerificationSendCodeSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
    
#     # if the phone number is already verified, return error
#     # if user phone_number is not provided, user must has phone number else return error
#     # if user phone_number is different from the one in the user's profile, update the phone number
#     # check if user has a verify code, if yes, remove it and create a new one
#     # create one verify code for the user
#     # send code to user phone number
#     pass


# @extend_schema(
#     request=PhoneVerifyCodeSerializer,
#     summary="Verify code to phone number.",
#     description="""
#     Verify a code sent to the user's phone number.
#     The use must be authenticated.
#     Rate limit: 10/minute
#     The code needed to be same as the one sent to the user's phone number and phone of the user.
#     """,
#     responses={
#         status.HTTP_201_CREATED: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Verification code sent.'
#                 }
#             }
#         },
#         status.HTTP_400_BAD_REQUEST: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Invalid phone number.'
#                 }
#             }
#         }
#     },
#     examples=[
#         OpenApiExample(
#             'a normal request',
#             summary='',
#             value={
#                 'code': '123456',
#             },
#             request_only=True
#         ),
#     ],
#     tags=['Registration'],
#     auth=[],
# )
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @throttle_classes([VerifyCodeThrottle])
# def phone_verify_code_api(request):
#     serializer = PhoneVerifyCodeSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
    
#     # find the latest user's verification code on db
#     # check if the code is expired, if yes return error
#     # check if the code's phone number is same as the user's phone number, if not return error
#     # make the user's phone number verified   
#     # remove the code from db
#     # return success
#     pass



# @extend_schema(
#     request=EmailVerificationSendCodeSerializer,
#     summary="Send verification code to email address.",
#     description="""
#     Send a verification code to the user's email address.
#     The user must be authenticated.
#     Rate limit: 1/minute
#     If the email address is different from the one in the user's profile, the email address in the user's profile will be updated.
#     If the email is already verified, the request will be ignored.
#     The email address must be unique.
    
#     - **parameters**:
#         - `email_address`: The email address for the user, it could be null if the user provided it before or it could be different from the one in the user's profile.
#     """,
#     responses={
#         status.HTTP_201_CREATED: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Verification code sent.'
#                 }
#             }
#         },
#         status.HTTP_400_BAD_REQUEST: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Invalid email address.'
#                 }
#             }
#         }
#     },
#     examples=[
#         OpenApiExample(
#             'a normal request',
#             summary='',
#             value={
#                 'email_address': 'example@example.com',
#             },
#             request_only=True
#         ),
#     ],
#     tags=['Registration'],
#     auth=[],
# )
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @throttle_classes([SendVerificationCodeThrottle])
# def email_code_send_api(request):
#     serializer = EmailVerificationSendCodeSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
    
#     # if the email address is already verified, return error
#     # if user email_address is not provided, user must have an email address else return error
#     # if user email_address is different from the one in the user's profile, update the email address
#     # check if user has a verify code, if yes, remove it and create a new one
#     # create a new verification code for the user
#     # send the code to the user's email address
#     pass


# @extend_schema(
#     request=EmailVerifyCodeSerializer,
#     summary="Verify the code at email.",
#     description="""
#     Verify a code sent to the user's email address.
#     The user must be authenticated.
#     Rate limit: 10/minute
#     The code needed to be same as the one sent to the user's email address and email of the user.
#     """,
#     responses={
#         status.HTTP_201_CREATED: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Verification code sent.'
#                 }
#             }
#         },
#         status.HTTP_400_BAD_REQUEST: {
#             'type': 'object',
#             'properties': {
#                 'detail': {
#                     'type': 'string',
#                     'description': 'A message to the user.',
#                     'example': 'Invalid email address.'
#                 }
#             }
#         }
#     },
#     examples=[
#         OpenApiExample(
#             'a normal request',
#             summary='',
#             value={
#                 'code': '123456',
#             },
#             request_only=True
#         ),
#     ],
#     tags=['Registration'],
#     auth=[],
# )
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @throttle_classes([VerifyCodeThrottle])
# def email_verify_code_api(request):
    serializer = EmailVerifyCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # find the latest user's verification code in the database
    # check if the code is expired, if yes return an error
    # check if the code's email address is the same as the user's email address, if not return an error
    # mark the user's email address as verified   
    # remove the code from the database
    # return success
    pass