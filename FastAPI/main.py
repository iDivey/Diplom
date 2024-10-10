from datetime import datetime
from fastapi import FastAPI, Request, Depends, Form
from sqlalchemy import insert, desc
from sqlalchemy.orm import Session
from models import *
from database import engine, session_local
from fastapi.templating import Jinja2Templates
from typing import Annotated
from routers import admin

app = FastAPI()

app.include_router(admin.router)

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory='templates')


@app.get('/')
async def main_page(request: Request):
    return templates.TemplateResponse('main.html', {'request': request})


@app.get('/book')
async def book_page(request: Request):
    return templates.TemplateResponse('book.html', {'request': request})


@app.post('/book')
async def book_result(request: Request, db: Annotated[Session, Depends(get_db)],
                      author: str = Form(), name_father_Author: str = Form(), title: str = Form(),
                      publisher: str = Form(), city: str = Form(), year: int = Form(), pages: int = Form()):
    db.execute(insert(Book).values(
        author=author,
        name_father_Author=name_father_Author,
        title=title,
        publisher=publisher,
        city=city,
        year=year,
        pages=pages
    ))
    db.commit()
    book = db.query(Book).order_by(desc(Book.id)).first()
    return templates.TemplateResponse('book_final.html', {'request': request, 'book': book})


@app.get('/conf')
async def conf_page(request: Request):
    return templates.TemplateResponse('conf.html', {'request': request})


@app.post('/conf')
async def conf_result(request: Request, db: Annotated[Session, Depends(get_db)],
                      author: str = Form(), name_father_Author: str = Form(), title: str = Form(),
                      publisher: str = Form(), place: str = Form(), date: datetime = Form(), city: str = Form(),
                      year: int = Form(), page_start: int = Form(), page_end: int = Form()):
    db.execute(insert(Conf).values(
        author=author,
        name_father_Author=name_father_Author,
        title=title,
        publisher=publisher,
        city=city,
        place=place,
        date=date,
        year=year,
        page_start=page_start,
        page_end=page_end
    ))
    db.commit()
    conf = db.query(Conf).order_by(desc(Conf.id)).first()
    return templates.TemplateResponse('conf_final.html', {'request': request, 'conf': conf})


@app.get('/journal')
async def journal_page(request: Request):
    return templates.TemplateResponse('journal.html', {'request': request})


@app.post('/journal')
async def journal_result(request: Request, db: Annotated[Session, Depends(get_db)],
                         author: str = Form(), name_father_Author: str = Form(), title: str = Form(),
                         publisher: str = Form(), number_tom: int = Form(), year: int = Form(),
                         page_start: int = Form(), page_end: int = Form()):
    db.execute(insert(Jour).values(
        author=author,
        name_father_Author=name_father_Author,
        title=title,
        publisher=publisher,
        number_tom=number_tom,
        year=year,
        page_start=page_start,
        page_end=page_end
    ))
    db.commit()
    journal = db.query(Jour).order_by(desc(Jour.id)).first()
    return templates.TemplateResponse('journal_final.html', {'request': request, 'journal': journal})


@app.get('/descript')
async def journal_page(request: Request):
    return templates.TemplateResponse('descript.html', {'request': request})



