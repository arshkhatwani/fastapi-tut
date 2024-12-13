from fastapi import APIRouter, Query, Path
from models.blogs import BlogModel

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
def get_specific_blog(id: int = Path(title='Id of the blog',
                                     description='Important part of blog'),
                      available: bool = Query(None, title='Availability of the blog',
                                              description='Important factor of blog')):
    if available:
        return {'id': id, 'title': 'yoyo'}
    else:
        return {'id': id, 'title': 'yoyo2'}


@router.post('/')
def create_blog(blog: BlogModel):
    return blog
