from graphene import ObjectType, String, ID, Field


class Movie(ObjectType):
    title = String()
    id = ID()


class Query(ObjectType):
    movie = Field(Movie)

    def resolve_movie():
        return Movie
