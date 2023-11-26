from fastapi import FastAPI, Request, Depends, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates
from pathlib import Path
from module_10 import call_api_github, save_data, get_json_user, get_json_all

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@app.post("/api/posts/{username}", status_code=201)
def create_post_username(username: str):
    save_data(username)
    post_new = call_api_github(username)
    return post_new


@app.get("/api/get/{username}")
def get_username(username: str):
    info_username = get_json_user(username)
    return info_username


@app.get("/api/getall")
def get_username():
    info_users = get_json_all()
    return info_users


@app.get("/", response_class=HTMLResponse)
async def get_main(request: Request):
    """
    Переход на станицу логина
    """
    context = {
        "info": '',
        "request": request,
    }
    return templates.TemplateResponse(
        "index.html", context
    )


@app.post("/", response_class=HTMLResponse)
async def post_main(request: Request, username=Form()):
    """
    Переход на станицу логина
    """

    if username:
        post_new = call_api_github(username)
        context = {
            "info": post_new,
            "request": request,
        }
    else:
        context = {
            "info": '',
            "request": request,
        }
    return templates.TemplateResponse(
        "index.html", context
    )
