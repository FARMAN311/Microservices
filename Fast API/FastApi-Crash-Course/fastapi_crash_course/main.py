from fastapi import FastAPI


from api import courses,sections,users
from Database.db_setup import engine
from Database.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)

