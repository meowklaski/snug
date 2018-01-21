import json
import snug
from gentools import reusable, map_yield, map_send, map_return, pipe

add_prefix = snug.http.prefix_adder('https://api.github.com')
add_headers = snug.https.header_adder({
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'my awesome app',
})

class ApiException(Exception):
    """an error from the github API"""

def handle_errors(resp):
    """raise a descriptive exception on a "bad request" response"""
    if resp.status_code == 400:
        raise ApiException(json.loads(resp.data).get('message'))
    return resp

def load_json_content(resp):
    """get the response body as JSON"""
    return json.loads(resp.data)

def follow_redirects(req):
    resp = yield req
    while resp.status_code in (301, 302, 307):
        resp = yield req.replace(url=resp.headers['Location'])
    return resp

def load_repo(jsondata):
    ...  # deserialization logic

@reusable
@pipe(follow_redirects)
@map_return(load_repo)
@map_send(load_json_content, handle_errors)
@map_yield(add_headers, add_prefix, snug.http.GET)
def repo(name: str, owner: str):
    """a repository lookup by owner and name"""
    return (yield f'/repos/{owner}/{name}')

@reusable
@map_send(handle_errors)
@map_yield(add_headers, add_prefix, snug.http.PUT)
def follow_user(name: str):
    """follow a user"""
    return (yield f'/user/following/{name}').status_code == 204
