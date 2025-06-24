from fastapi import APIRouter, Depends, HTTPException

from schemas.movie import MovieRequest, MovieResponse
from services.ai_service import AIService

router = APIRouter(prefix="/chat/completions", tags=["Movies"])


def get_ai_service() -> AIService:
    """
    Dependency injection for AIService.

    Returns:
        AIService: AIService instance to interact with Google Gemini API.
    """
    return AIService()


@router.post("/movie", response_model=MovieResponse)
async def get_movie_info(
    request: MovieRequest, ai_service: AIService = Depends(get_ai_service)
) -> MovieResponse:
    """
    Get movie information by its title.

    Args:
        request (MovieRequest): Request containing the movie title.
        ai_service (AIService): AI service injected as dependency.

    Returns:
        MovieResponse: JSON with movie information including release date, box office and synopsis.

    Raises:
        HTTPException: Error when processing request or getting movie information.
    """
    try:
        movie_info = ai_service.get_movie_info(request.title)
        return movie_info
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error getting movie information: {str(e)}"
        )
