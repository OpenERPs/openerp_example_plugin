from fastapi import FastAPI, Request, HTTPException, APIRouter

title = "Example Plugin"
description = "This is an example plugin for OpenERP."
author = "Rudransh"
version = "0.1.0"
available_resources = ["res_example"]
data_scopes = ["example_data"]

app = FastAPI(title=title, description=description, version=version)

api_router = APIRouter()


@api_router.get("/example/")
async def read_example(request: Request):
    if not request.state.has_permission('read', 'res_example'):
        raise HTTPException(status_code=403, detail="Permission denied")

    return {"message": "This is an example read endpoint", "user": request.state.user_name}


@api_router.post("/example/")
async def create_example(request: Request):
    if not request.state.has_permission('create', 'res_example'):
        raise HTTPException(status_code=403, detail="Permission denied")

    return {"message": "This is an example create endpoint", "user": request.state.user_name}


@api_router.put("/example/")
async def update_example(request: Request):
    if not request.state.has_permission('update', 'res_example'):
        raise HTTPException(status_code=403, detail="Permission denied")

    return {"message": "This is an example update endpoint", "user": request.state.user_name}


@api_router.delete("/example/")
async def delete_example(request: Request):
    if not request.state.has_permission('delete', 'res_example'):
        raise HTTPException(status_code=403, detail="Permission denied")

    return {"message": "This is an example delete endpoint", "user": request.state.user_name}


app.include_router(api_router)
