from fastapi import HTTPException, APIRouter
import httpx

router = APIRouter()
url: str = 'http://api-nd.allcare.com.br/getip/ip'
@router.get('/meuip')
async def get_ip():
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)

        if response.status_code!= 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )
        return response.text

