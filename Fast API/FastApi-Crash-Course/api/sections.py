import fastapi

router = fastapi.APIRouter()


@router.get('/sections/{id}')
async def read_section():
    return {"course":[]}

@router.get('/sections/{id}/content-blocks')
async def read_section_content_block():
    return {"courses":[]}

@router.get('/content-block/{id}')
async def read_content_block():
    return {"courses":[]}