from ..models import Posts
from ..serializers import PostsSerializer

def create_post_service(user, data):
    data['user'] = user.id
    serializer = PostsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, True
    return serializer.errors, False

def list_user_posts_service(user):
    posts = Posts.objects.filter(user=user)
    serializer = PostsSerializer(posts, many=True)
    return serializer.data