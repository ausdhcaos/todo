from typing import Annotated
import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from models.user import User
from models.db_session import get_session
from common.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
)
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
import datetime

router = APIRouter()


@router.post("/users/signup")
async def signup(
    email_address: str, password: str, session: AsyncSession = Depends(get_session)
):
    if (
        await session.scalars(select(User).where(User.email_address == email_address))
    ).first():
        raise HTTPException(status_code=409, detail="User exists")

    salt = bcrypt.gensalt()
    user = User(
        email_address=email_address,
        password=bcrypt.hashpw(password.encode(), salt).decode(),
        password_salt=salt.decode(),
    )
    session.add(user)

    await session.commit()


@router.post("/users/token")
async def get_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: AsyncSession = Depends(get_session),
):
    user = (
        await session.scalars(
            select(User).where(User.email_address == form_data.username)
        )
    ).one_or_none()

    if (
        not user
        or bcrypt.hashpw(
            form_data.password.encode(), user.password_salt.encode()
        ).decode()
        != user.password
    ):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )

    return {
        "access_token": access_token["token"],
        "token_type": "bearer",
        "exp": access_token["exp"],
    }
