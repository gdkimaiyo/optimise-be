from drf_yasg import openapi

from api.serializers import PostSerializer, UserSerializer


get_posts_data_doc = {
    "method": "get",
    "operation_summary": "Get all posts",
    # "operation_description": "Get all posts while applying caching as an optimiztion technique.",
    "responses": {
        200: openapi.Response(
            "Successful retrieval of posts data", PostSerializer
        ),
        400: "Error while connecting to the server",
    },
}
