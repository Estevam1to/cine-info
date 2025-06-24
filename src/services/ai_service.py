import json
from http import HTTPStatus

from fastapi import HTTPException
from google.genai import Client, types

from config.logs import logger
from config.settings import settings
from schemas.movie import LLmMovieResponse


class AIService:
    """
    Serviço para interagir com a API do Google Gemini para obter informações sobre filmes.
    """

    def _clean_markdown_response(self, response: str) -> str:
        """
        Remove markdown formatting da resposta da API.

        Args:
            response (str): Resposta bruta da API.

        Returns:
            str: Resposta limpa sem markdown.
        """
        json_str = response.strip()
        if json_str.startswith("```json"):
            json_str = json_str.replace("```json", "").replace("```", "").strip()
        elif json_str.startswith("```"):
            json_str = json_str.replace("```", "").strip()
        return json_str

    def generate_response(self, text: str) -> LLmMovieResponse:
        """
        Gera uma resposta usando a API do Google Gemini.

        Args:
            text (str): O texto de entrada para gerar a resposta.

        Returns:
            str: A resposta gerada pela API.

        Exceptions:
            HTTPException: Erro interno do servidor ao gerar resposta.
        """
        try:
            client = Client(api_key=settings.GOOGLE_API_KEY)

            retrieval_tool = types.Tool(
                google_search_retrieval=types.GoogleSearchRetrieval(
                    dynamic_retrieval_config=types.DynamicRetrievalConfig(
                        mode=types.DynamicRetrievalConfigMode.MODE_DYNAMIC,
                        dynamic_threshold=0.3,
                    )
                )
            )

            config = types.GenerateContentConfig(tools=[retrieval_tool])

            contents = [
                types.Content(parts=[types.Part(text=text)], role="user"),
            ]

            response = client.models.generate_content(
                model=settings.GOOGLE_API_MODEL,
                contents=contents,
                config=config,
            )

            return response.text
        except Exception as e:
            logger.error(f"Erro ao gerar resposta: {str(e)}")
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"Erro ao gerar resposta: {str(e)}",
            )

    def get_movie_info(
        self,
        title: str,
    ) -> LLmMovieResponse:
        """
        Obtém informações sobre um filme usando a API do Google Gemini.

        Args:
            title (str, optional): O título do filme.

        Returns:
            LLmMovieResponse: Informações do filme, incluindo título, data de lançamento, bilheteria e sinopse.

        Exceptions:
            HTTPException: Erro interno do servidor ao obter informações do filme.
        """
        logger.info(f"Obtendo informações do filme: {title}")
        try:
            input_text = (
                f"Por favor, forneça informações detalhadas sobre o filme '{title}'. "
                f"Responda com um objeto JSON contendo os seguintes campos: "
                f"'title' (string), 'release_date' (string), 'box_office' (string), 'synopsis' (string). "
                f"Certifique-se de que a resposta contenha apenas o JSON válido, sem texto ou explicações adicionais. "
                f"Responda em português."
            )

            response = self.generate_response(text=input_text)
            logger.info(f"Resposta recebida: {response}")

            json_str = self._clean_markdown_response(response)
            movie_data = json.loads(json_str)

            if isinstance(movie_data.get("box_office"), (int, float)):
                movie_data["box_office"] = str(movie_data["box_office"])

            return LLmMovieResponse(**movie_data)

        except json.JSONDecodeError as e:
            logger.error(f"Erro ao decodificar JSON: {str(e)}")
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"Erro ao processar resposta da API: {str(e)}",
            )
        except Exception as e:
            logger.error(f"Erro ao obter informações do filme: {str(e)}")
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"Erro ao obter informações do filme: {str(e)}",
            )
