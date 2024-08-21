from enum import Enum

from fastapi import FastAPI


class SocialMedia(Enum):
    facebook = "facebook"
    instagram = "instagram"
    tiktok = "tiktok"


app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/hello/")
async def say_hello():
    return {"message": f"Hello dude!"}


@app.get("/hello/{name}/")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/social-media/{name}/")
async def social_media(name: SocialMedia):
    if name == SocialMedia.facebook:
        return {"message": "Facebook"}

    if name == SocialMedia.instagram:
        return {"message": "Instagram"}

    if name == SocialMedia.tiktok:
        return {"message": "TikTok"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):

    return {"message": file_path}
