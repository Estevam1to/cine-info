from pydantic import BaseModel, Field


class MovieRequest(BaseModel):
    """
    Modelo Pydantic para requisição de informações de filme.
    """

    title: str = Field(
        description="Titulo do filme que deseja obter informações",
        examples=["Interstellar", "The Matrix", "Inception", "Titanic"],
    )


class MovieResponse(BaseModel):
    """
    Modelo Pydantic para resposta de informações de filme.
    """

    title: str = Field(
        description="Título do filme",
        examples=["Interstellar"],
    )
    release_date: str = Field(
        description="Data de lançamento do filme",
        examples=["2014-11-07"],
    )
    box_office: str = Field(
        description="Bilheteira do filme",
        examples=["$677,471,339"],
    )
    synopsis: str = Field(
        description="Sinopse do filme",
        examples=[
            "Um grupo de exploradores viaja através de um buraco de minhoca próximo a Saturno em uma missão para garantir a sobrevivência da humanidade."
        ],
    )


class LLmMovieResponse(BaseModel):
    """
    Modelo Pydantic para resposta de informações de filme.
    """

    title: str
    release_date: str
    box_office: str
    synopsis: str
