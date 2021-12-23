from fastapi import APIRouter

router = APIRouter(
    prefix='/manga',
)


@router.get('/')
def get_manga():
    return []
