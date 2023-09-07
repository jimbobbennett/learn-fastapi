import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "streaming",
        "description": "Streaming content like movies and series.",
    }
]

app = FastAPI(
    servers=[

        {"url": "http://na.exciting.soda", "description": "Prod"},
        {"url": "http://eu.exciting.soda", "description": "EU"}
    ],
    contact={
        "name": "JimBobBennett",
        "url": "https://jimbobbennett.dev"
    },
    description="A test API for LibLab",
    openapi_tags=tags_metadata
)


class Series(BaseModel):
    id: str
    series_name: str
    cast: list[str]
    episodes: list[str]


class Movie(BaseModel):
    id: str
    movie_name: str
    cast: list[str]


@app.get("/movie", tags=["streaming"], summary="Get a list of movies", operation_id="getMovies")
async def get_all_movies() -> list[Movie]:
    '''
    Returns a list of movies
    '''
    return [
        {
            "id": 1,
            "movie_name": "Star Wars Episode IV: a new hope",
            "cast": [
                "Mark Hamil",
                "Harrison Ford",
                "Carrie Fisher",
                "Peter Cushing",
                "Alec Guinness",
                "Anthony Daniels",
                "Kenny Baker",
                "Peter Mayhew",
                "David Prowse",
                "James Earl Jones"
            ]
        },
        {
            "id": 2,
            "movie_name": "Star Wars Episode V: the Empire strikes back",
            "cast": [
                "Mark Hamil",
                "Harrison Ford",
                "Carrie Fisher",
                "Billy Dee Williams",
                "Alec Guinness",
                "Anthony Daniels",
                "Kenny Baker",
                "Peter Mayhew",
                "David Prowse",
                "James Earl Jones"
            ]
        },
        {
            "id": 3,
            "movie_name": "Star Wars Episode VI: Return of the Jedi",
            "cast": [
                "Mark Hamil",
                "Harrison Ford",
                "Carrie Fisher",
                "Billy Dee Williams",
                "Warwick Davis",
                "Ian McDiarmid",
                "Alec Guinness",
                "Anthony Daniels",
                "Kenny Baker",
                "Peter Mayhew",
                "David Prowse",
                "James Earl Jones"
            ]
        }
    ]


@app.get("/movie/{id}", tags=["streaming"], summary="Get a movie by id", operation_id="getMovieById")
async def get_movie_by_id(id: str) -> Movie:
    '''
    Returns a movie by Id
    '''
    return {
        "id": id,
        "movie_name": "Star Wars Episode IV: a new hope",
        "cast": [
            "Mark Hamil",
            "Harrison Ford",
            "Carrie Fisher",
            "Peter Cushing",
            "Alec Guinness",
            "Anthony Daniels",
            "Kenny Baker",
            "Peter Mayhew",
            "David Prowse",
            "James Earl Jones"
        ]
    }


@app.get("/series", tags=["streaming"], summary="Get a list of series", operation_id="getSeries")
async def get_all_series() -> list[Series]:
    '''
    Returns a list of series
    '''
    return [
        {
            "id": 1,
            "series_name": "Star Wars: the Clone Wars",
            "cast": [
                "Matt Lanter",
                "James Arnold Taylor",
                "Ashley Eckstein",
                "Dee Bradley Baker"
            ],
            "episodes": [
                "Ambush",
                "Rising Malevolence",
                "Shadow of Malevolence",
                "Destroy Malevolence",
                "Rookies",
                "Downfall of a Droid"
            ]
        },
        {
            "id": 2,
            "series_name": "Star Wars: Rebels",
            "cast": [
                "Freddie Prinze Jr.",
                "Taylor Gray",
                "Vanessa Marshall",
                "Tiya Sircar"
            ],
            "episodes": [
                "Spark of Rebellion",
                "Droids in Distress",
                "Fighter Flight",
                "Rise of the Old Masters"
            ]
        }
    ]


@app.get("/series/{id}", tags=["streaming"], summary="Get a series by id", operation_id="getSeriesById")
async def get_series_by_id(id: str) -> Series:
    '''
    Returns a series by Id
    '''
    return {
        "id": id,
        "series_name": "Star Wars: the Clone Wars",
        "cast": [
            "Matt Lanter",
            "James Arnold Taylor",
            "Ashley Eckstein",
            "Dee Bradley Baker"
        ],
        "episodes": [
            "Ambush",
            "Rising Malevolence",
            "Shadow of Malevolence",
            "Destroy Malevolence",
            "Rookies",
            "Downfall of a Droid"
        ]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
