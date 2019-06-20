def extract_language(project):
    '''
    Project distribution in % is as follows:
        en.wikipedia.org         16.618986
        ja.wikipedia.org         14.084225
        de.wikipedia.org         12.785479
        fr.wikipedia.org         12.271909
        zh.wikipedia.org         11.876909
        ru.wikipedia.org         10.355501
        es.wikipedia.org          9.698545
        commons.wikimedia.org     7.276149
        www.mediawiki.org         5.032296
    '''
    if 'media' in project:
        return 'media'
    return project.split('.')[0]