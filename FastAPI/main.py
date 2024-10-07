from fastapi import FastAPI, Request, Depends, Form
from sqlalchemy import insert
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from models import *
from database import engine, session_local
from schemes import *
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()

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
                author: str = Form(), name_father_Author: str = Form(), title: str = Form(), publisher: str = Form(), city: str = Form(), year: int = Form(), pages: int = Form()):
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
        return RedirectResponse('/book_final')


@app.get('/book_final')
def book_final_page(request: Request, db: Annotated[Session, Depends(get_db)]):
    book = Book.query.order_by(Book.id).desc().first()
    return templates.TemplateResponse('book_final.html', {'request': request,'book': book})


@app.get('/conf')
async def conf_page(request: Request):
    return templates.TemplateResponse('conf.html', {'request': request})

@app.get('/journal')
async def journal_page(request: Request):
    return templates.TemplateResponse('journal.html', {'request': request})

@app.get('/descript')
async def journal_page(request: Request):
    return templates.TemplateResponse('descript.html', {'request': request})