from pydantic import BaseModel, Field


class MovieRequest(BaseModel):
    """
    Pydantic model for movie information request.
    """

    title: str = Field(
        description="Movie title to get information about",
        examples=["Interstellar", "The Matrix", "Inception", "Titanic"],
    )


class MovieResponse(BaseModel):
    """
    Pydantic model for movie information response.
    """

    title: str = Field(
        description="Movie title",
        examples=["Interstellar"],
    )
    release_date: str = Field(
        description="Movie release date",
        examples=["2014-11-07"],
    )
    box_office: str = Field(
        description="Movie box office earnings",
        examples=["$677,471,339"],
    )
    synopsis: str = Field(
        description="Movie synopsis",
        examples=[
            "A group of explorers travels through a wormhole near Saturn on a mission to ensure humanity's survival."
        ],
    )


class LLmMovieResponse(BaseModel):
    """
    Pydantic model for LLM movie information response.
    """

    title: str
    release_date: str
    box_office: str
    synopsis: str
