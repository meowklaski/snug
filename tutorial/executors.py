import json
from gentools import reusable
import snug

@reusable
def repo(name: str, owner: str):
    """a repo lookup by owner and name"""
    request = snug.GET(f'https://api.github.com/repos/{owner}/{name}')
    response = yield request
    return json.loads(response.data)

@reusable
def follow(username: str):
    """follow another user"""
    request = snug.PUT(
        f'https://api.github.com/user/following/{username}')
    response = yield request
    return response.status_code == 204
