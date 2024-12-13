from fastapi import APIRouter

router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)


@router.get('/all')
def get_all_blogs():
    return [
        {'id': 1, 'title': 'karan'},
        {'id': 2, 'title': 'arsh'},
        {'id': 3, 'title': 'something'}
    ]


@router.get('/{id}', description='Get a specific blog')
def get_specific_blog(id: int, available: bool):
    if available:
        return {'id': id, 'title': 'yoyo'}
    else:
        return {'id': id, 'title': 'yoyo2'}
