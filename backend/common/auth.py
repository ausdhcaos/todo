# Ref: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-token-path-operation

from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from sqlalchemy import select
from models.user import User
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from models.db_session import get_session

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.PRIVATE_KEY, algorithm=ALGORITHM)
    return {"token": encoded_jwt, "exp": expire}


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.PRIVATE_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
    except InvalidTokenError:
        raise credentials_exception

    user = (await session.scalars(select(User).where(User.id == user_id))).one_or_none()

    if not user:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )

    return user
