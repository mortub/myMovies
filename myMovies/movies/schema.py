from .graphql.movies.queries import Query
import graphene


class RootQuery(Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery)
