import reprlib
import operator
from datetime import datetime

import snug
from snug.utils import partial, compose

parse_datetime = partial(datetime.strptime, ..., '%Y-%m-%dT%H:%M:%SZ')

_repr = reprlib.Repr()
_repr.maxstring = 45


class Issue(snug.Resource):
    number = snug.Field()
    title = snug.Field()
    body = snug.Field()
    state = snug.Field()

    def __str__(self):
        return self.title

    @staticmethod
    def filtered_request(filters):
        return snug.Request('issues', params=filters)

    @staticmethod
    def node_request(key):
        owner, repo, number = key
        return snug.Request(f'repos/{owner}/{repo}/issues/{number}')


Issue.ASSIGNED = snug.Set(
    list_load=compose(list, partial(map, Issue.obj_load)),
    request=snug.Request('issues')
)


class Repo(snug.Resource):

    name = snug.Field()
    archive_url = snug.Field()
    assignees_url = snug.Field()
    blobs_url = snug.Field()
    branches_url = snug.Field()
    clone_url = snug.Field()
    collaborators_url = snug.Field()
    comments_url = snug.Field()
    commits_url = snug.Field()
    compare_url = snug.Field()
    contents_url = snug.Field()
    contributors_url = snug.Field()
    created_at = snug.Field(load=parse_datetime)
    default_branch = snug.Field()
    deployments_url = snug.Field()
    description = snug.Field()
    downloads_url = snug.Field()
    events_url = snug.Field()
    fork = snug.Field()
    forks = snug.Field()
    forks_count = snug.Field()
    forks_url = snug.Field()
    full_name = snug.Field()
    git_commits_url = snug.Field()
    git_refs_url = snug.Field()
    git_tags_url = snug.Field()
    git_url = snug.Field()
    has_downloads = snug.Field()
    has_issues = snug.Field()
    has_pages = snug.Field()
    has_projects = snug.Field()
    has_wiki = snug.Field()
    homepage = snug.Field()
    hooks_url = snug.Field()
    html_url = snug.Field()
    id = snug.Field()
    issue_comment_url = snug.Field()
    issue_events_url = snug.Field()
    issues_url = snug.Field()
    keys_url = snug.Field()
    labels_url = snug.Field()
    language = snug.Field()
    languages_url = snug.Field()
    merges_url = snug.Field()
    milestones_url = snug.Field()
    mirror_url = snug.Field()
    name = snug.Field()
    notifications_url = snug.Field()
    open_issues = snug.Field()
    open_issues_count = snug.Field()
    owner = snug.Field()
    permissions = snug.Field()
    private = snug.Field()
    pulls_url = snug.Field()
    pushed_at = snug.Field()
    releases_url = snug.Field()
    size = snug.Field()
    ssh_url = snug.Field()
    stargazers_count = snug.Field()
    stargazers_url = snug.Field()
    statuses_url = snug.Field()
    subscribers_url = snug.Field()
    subscription_url = snug.Field()
    svn_url = snug.Field()
    tags_url = snug.Field()
    teams_url = snug.Field()
    trees_url = snug.Field()
    updated_at = snug.Field()
    url = snug.Field()
    watchers = snug.Field()
    watchers_count = snug.Field()

    def __str__(self):
        return '{} - {}'.format(
            self.name, _repr.repr(self.description))

    @staticmethod
    def filtered_request(filters):
        return snug.Request('repositories', params=filters)

    @staticmethod
    def node_request(key):
        owner, name = key
        return snug.Request(f'repos/{owner}/{name}')


class Organization(snug.Resource):
    avatar_url = snug.Field()
    blog = snug.Field()
    company = snug.Field()
    created_at = snug.Field(load=parse_datetime)
    description = snug.Field()
    email = snug.Field()
    events_url = snug.Field()
    followers = snug.Field()
    following = snug.Field()
    has_organization_projects = snug.Field()
    has_repository_projects = snug.Field()
    hooks_url = snug.Field()
    html_url = snug.Field()
    id = snug.Field()
    issues_url = snug.Field()
    location = snug.Field()
    login = snug.Field()
    members_url = snug.Field()
    name = snug.Field()
    public_gists = snug.Field()
    public_members_url = snug.Field()
    public_repos = snug.Field()
    repos_url = snug.Field()
    type = snug.Field()

    def __str__(self):
        try:
            return self.name
        except KeyError:
            return self.login

    @staticmethod
    def filtered_request(filters):
        return snug.Request('organizations', params=filters)

    @staticmethod
    def node_request(key):
        return snug.Request(f'orgs/{key}')


api = snug.Api(prefix='https://api.github.com/',
               headers={'Accept': 'application/vnd.github.v3+json'},
               parse_response=operator.methodcaller('json'),
               resources={Organization, Repo})
