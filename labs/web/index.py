from pyroutes import route
from pyroutes.http.response import Response
from pyroutes.template import TemplateRenderer

import simplejson
import urllib2
import memcache

cache = memcache.Client(['127.0.0.1:11211'])

tr = TemplateRenderer("labs/templates/base.xml")

@route('/')
def index(request):
    projects = None #cache.get('above_labs_projects')
    if not projects:
        projects = {'#projects': [], 'title': 'Labs Above'}
        for user in ['klette', 'jodal', 'adamcik', 'xim', 'frsk', 'eide', 'jorabra']:
            for project in get_github_repositories(user):
                projects['#projects'].append({'#project':
                    {'#project_title': unicode(project[0]),
                     '#project_maintainer': u'Maintained by %s' % user,
                     '#project_link/href': u'http://www.github.com/%s/%s' % (user, project[0]),
                     '#project_desc': unicode(project[1])}})
        cache.set('above_labs_projects', projects)
    return Response(tr.render('labs/templates/index.xml', projects))

def get_github_repositories(username):
    json = urllib2.urlopen('http://github.com/api/v2/json/repos/show/%s' % username).read()
    data = simplejson.loads(json)
    for repo in data.get('repositories'):
        if repo['fork']:
            continue
        yield (repo['name'], repo['description'])
