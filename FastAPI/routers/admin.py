from fastapi import APIRouter, Depends, status, HTTPException, Request
from sqlalchemy.orm import Session
from typing import Annotated
from models import Book, Conf, Jour
from sqlalchemy import select, delete, func
from fastapi.templating import Jinja2Templates
from database import session_local

router = APIRouter(prefix='/admin', tags=['admin'])

templates = Jinja2Templates(directory='templates')


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
async def main_page(request: Request):
    return templates.TemplateResponse('admin.html', {'request': request})


@router.get('/book')
async def all_book(db: Annotated[Session, Depends(get_db)]):
    book = db.scalars(select(Book)).all()
    return book


@router.get('/jour')
async def all_jour(db: Annotated[Session, Depends(get_db)]):
    jour = db.scalars(select(Jour)).all()
    return jour


@router.get('/conf')
async def all_conf(db: Annotated[Session, Depends(get_db)]):
    conf = db.scalars(select(Conf)).all()
    return conf


@router.get('/book/{id}')
async def book_by_id(db: Annotated[Session, Depends(get_db)], id: int):
    book = db.scalars(select(Book).where(Book.id == id))
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book was not found')

    return book


@router.get('/jour/{id}')
async def jour_by_id(db: Annotated[Session, Depends(get_db)], id: int):
    jour = db.scalars(select(Jour).where(Conf.id == id))
    if jour is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='jour was not found')
    return jour


@router.get('/conf/{id}')
async def conf_by_id(db: Annotated[Session, Depends(get_db)], id: int):
    conf = db.scalars(select(Conf).where(Conf.id == id))
    if conf is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='conf was not found')
    return conf


@router.delete('/delete_book/{id}')
async def delete_book(db: Annotated[Session, Depends(get_db)], id: int):
    book = db.scalars(select(Book).where(Book.id == id))
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book was not found')

    db.execute(delete(Book).where(Book.id == id))
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'Book delete is successful!'
    }


@router.delete('/delete_jour/{id}')
async def delete_jour(db: Annotated[Session, Depends(get_db)], id: int):
    jour = db.scalars(select(Jour).where(Jour.id == id))
    if jour is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='journ was not found')

    db.execute(delete(Jour).where(Jour.id == id))
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'Journ delete is successful!'
    }


@router.delete('/delete_conf/{id}')
async def delete_conf(db: Annotated[Session, Depends(get_db)], id: int):
    conf = db.scalars(select(Conf).where(Conf.id == id))
    if conf is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Conf was not found')

    db.execute(delete(Conf).where(Conf.id == id))
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'Journ delete is successful!'
    }


@router.delete('/delete_book')
async def delete_book(db: Annotated[Session, Depends(get_db)]):
    db.execute(delete(Book)).all()
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'Books delete is successful!'
    }


@router.delete('/delete_jour')
async def delete_jour(db: Annotated[Session, Depends(get_db)]):
    db.execute(delete(Jour)).all()
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'Journals delete is successful!'
    }


@router.delete('/delete_conf')
async def delete_jour(db: Annotated[Session, Depends(get_db)]):
    db.execute(delete(Conf)).all()
    db.commit()
    return {
        'statys_code': status.HTTP_200_OK,
        'translation': 'Conf`s delete is successful!'
    }


@router.get('/stats')
async def get_stats(db: Annotated[Session, Depends(get_db)]):
    book_count = db.scalar(select(func.count(Book.id)))
    journal_count = db.scalar(select(func.count(Jour.id)))
    conference_count = db.scalar(select(func.count(Conf.id)))

    stats = {
        'total_books': book_count,
        'total_journals': journal_count,
        'total_conferences': conference_count,
    }

    return stats


@router.get('/search/book')
async def search_books(db: Annotated[Session, Depends(get_db)], author: str):
    books = db.scalars(select(Book).where(Book.author.ilike(f'%{author}%'))).all()
    return books


@router.get('/search/jour')
async def search_journals(db: Annotated[Session, Depends(get_db)], author: str):
    journals = db.scalars(select(Jour).where(Jour.author.ilike(f'%{author}%'))).all()
    return journals


@router.get('/search/conf')
async def search_conferences(db: Annotated[Session, Depends(get_db)], author: str):
    conferences = db.scalars(select(Conf).where(Conf.author.ilike(f'%{author}%'))).all()
    return conferences
