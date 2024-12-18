from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app.models import Base, BlogPost
from app.schemas import BlogPostCreate

# Initialize the database
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="app/templates")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home page - Display all blogs
@app.get("/")
def read_blogs(request: Request, db: Session = Depends(get_db)):
    blogs = db.query(BlogPost).all()
    return templates.TemplateResponse("index.html", {"request": request, "blogs": blogs})

# Create blog page - Display the form
@app.get("/create")
def create_blog_form(request: Request):
    return templates.TemplateResponse("create_post.html", {"request": request})

# Create blog - Handle form submission
@app.post("/create")
def create_blog(title: str = Form(...), author: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    new_blog = BlogPost(title=title, author=author, content=content)
    db.add(new_blog)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
