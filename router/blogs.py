from fastapi import APIRouter, Query, Path, Body, Depends
from models.blogs import BlogModel
from typing import Optional
from sample_dep.req_func import required_functionality

router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)


@router.get('/all')
def get_all_blogs(some_dep: str = Depends(required_functionality)):
    return [
        {'id': 1, 'title': 'karan', 'comment': some_dep},
        {'id': 2, 'title': 'arsh', 'comment': some_dep},
        {'id': 3, 'title': 'something', 'comment': some_dep}
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
def create_blog(blog: BlogModel,
                # content: str = Body(Ellipsis)
                # content: str = Body('hi this is content')
                content: str = Body(..., min_length=2,
                                    max_length=100, regex='^[a-z\s]*$'),
                tags: Optional[list[str]] = Query(None)
                ):
    return {'blog': blog, 'content': content, 'tags': tags}
