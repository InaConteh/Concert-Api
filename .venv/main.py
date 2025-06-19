from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from routers import Play_route, Actors_route, Directors_route, customers_route, showtime_route, concert_routes, auth_routes
from fastapi import Depends

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(Play_route.router)
app.include_router(Actors_route.router)
app.include_router(Directors_route.router)
app.include_router(customers_route.router)
app.include_router(showtime_route.router)
app.include_router(auth_routes.router)
app.include_router(concert_routes.router)


@app.get("/")
def root():
    return {"message": " Welcome my concert API"}


@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    # Optionally decode/verify token here
    return {"msg": "You are authenticated"}



