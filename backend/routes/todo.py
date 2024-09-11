from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.auth import get_current_user
from models.db_session import get_session
from models.todo import ToDo
from models.user import User


router = APIRouter()


@router.get("/todos/{id}")
async def get_todo(
    id: int,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    todo = (
        await session.scalars(
            select(ToDo).where(ToDo.id == id and ToDo.user_id == user.id)
        )
    ).one_or_none()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@router.get("/todos")
async def get_todos(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    todos = (await session.scalars(select(ToDo).where(ToDo.user_id == user.id))).all()

    return todos


@router.post("/todos")
async def create_todo(
    description: str,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    todo = ToDo(description=description, status="pending", user_id=user.id)
    session.add(todo)
    await session.commit()

    return todo

@router.put("/todos/{id}")
async def update_todo(
    id: int,
    status: str | None = None,
    description: str | None = None,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    todo = (
        await session.scalars(
            select(ToDo).where(ToDo.id == id and ToDo.user_id == user.id)
        )
    ).one_or_none()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    if status is not None:
        todo.status = status
    if description is not None:
        todo.description = description

    await session.commit()

    return todo

@router.delete("/todos/{id}")
async def delete_todo(
    id: int,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    todo = (
        await session.scalars(
            select(ToDo).where(ToDo.id == id and ToDo.user_id == user.id)
        )
    ).one_or_none()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    await session.delete(todo)
    await session.commit()

    return todo