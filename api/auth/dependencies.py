from fastapi import Request
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from jose import jwt, jwk
import requests

from api.core.config import Config
from api.errors import (
    InvalidToken,
    UserNotFound
)

security = HTTPBearer(scheme_name='Authorization')


def get_jwks():
    response = requests.get(Config.CLERK_JWK_URL)
    return response.json()


def get_public_key(kid):
    jwks = get_jwks()
    for key in jwks['keys']:
        if key['kid'] == kid:
            return jwk.construct(key)
    raise InvalidToken()


def decode_token(token: str):
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']
    public_key = get_public_key(kid)
    return jwt.decode(token, public_key.to_pem().decode('utf-8'), algorithms=['RS256'])


class CurrUserBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        token = creds.credentials
        try:
            token_data = decode_token(token)
            token_data.update({'is_authenticated': True})
        except:
            raise InvalidToken()

        if not token_data.get('sub'):
            raise UserNotFound()
        return token_data


# async def get_current_user(
#     token_details: dict = Depends(AccessTokenBearer()),
#     session: AsyncSession = Depends(get_session),
# ):
#     user_email = token_details["user"]["email"]

#     # user = await user_service.get_user_by_email(user_email, session)

#     # return user


# class RoleChecker:
#     def __init__(self, allowed_roles: List[str]) -> None:
#         self.allowed_roles = allowed_roles

#     def __call__(self, current_user: User = Depends(get_current_user)) -> Any:
#         if not current_user.is_verified:
#             raise AccountNotVerified()
#         if current_user.role in self.allowed_roles:
#             return True

#         raise InsufficientPermission()
