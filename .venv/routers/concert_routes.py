from fastapi import APIRouter, Depends
from dependencies import get_current_user
from schemas import User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/me", summary="Get current user info")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "status": "authenticated"}