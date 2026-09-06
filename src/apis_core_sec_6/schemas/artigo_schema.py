from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl

class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: str
    usuario_id: Optional[int] = None

    model_config = ConfigDict(
        from_attributes = True
    )