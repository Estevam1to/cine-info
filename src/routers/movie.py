from fastapi import APIRouter, Depends, HTTPException

from schemas.movie import MovieRequest, MovieResponse
from services.ai_service import AIService

router = APIRouter(prefix="/chat/completions", tags=["Movies"])


def get_ai_service() -> AIService:
    """
    Injeção de dependência para AIService.

    Returns:
        AIService: Instância do AIService para interagir com a API do Google Gemini.
    """
    return AIService()


@router.post("/movie", response_model=MovieResponse)
async def get_movie_info(
    request: MovieRequest, ai_service: AIService = Depends(get_ai_service)
) -> MovieResponse:
    """
    Obtém informações sobre um filme pelo seu título.

    Args:
        request (MovieRequest): Requisição contendo o título do filme.
        ai_service (AIService): Serviço de IA injetado como dependência.

    Returns:
        MovieResponse: JSON com informações do filme incluindo data de lançamento, bilheteria e sinopse.

    Raises:
        HTTPException: Erro ao processar a requisição ou obter informações do filme.
    """
    try:
        movie_info = ai_service.get_movie_info(request.title)
        return movie_info
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao obter informações do filme: {str(e)}"
        )
