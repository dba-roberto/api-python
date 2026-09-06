from typing import Optional
from typing import List

from pydantic import BaseModel, ConfigDict

from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: str
    eh_admin: bool = False

    model_config = ConfigDict(
        from_attributes = True
    )

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    id: Optional[int] = None
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[str]
    senha: Optional[str]
    eh_admin: Optional[bool]

