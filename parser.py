from readability import ParserClient
import json
token = open('readability_token','r')
parser_client = ParserClient(token.read())
sources = 'sources/'
articles = 'articles/'

def main():
    from optparse import OptionParser
    parser = OptionParser(usage="%prog: [options] [file]")
    parser.add_option('-v', '--verbose', action='store_true')
    parser.add_option('-u', '--url', default=None, help="use URL instead of a local file")
    #parser.add_option('-p', '--positive-keywords', default=None, help="positive keywords (separated with comma)", action='store')
    #parser.add_option('-n', '--negative-keywords', default=None, help="negative keywords (separated with comma)", action='store')
    (options, args) = parser.parse_args()

    if not (len(args) == 1 or options.url):
        parser.print_help()
        sys.exit(1)

    file = None
    if options.url:
        #import urllib
        #file = urllib.urlopen(options.url)
        parser_response = parser_client.get_article_content(options.url)
    #else:
    #    file = open(args[0], 'rt')
    #enc = sys.__stdout__.encoding or 'utf-8' # XXX: this hack could not always work, better to set PYTHONIOENCODING
    try:
      fname = parser_response.content['url'];
      fname = fname.replace('/','_')
      fname = fname.replace(':','')
      fhtml = open(articles + fname + '.html', 'wb')
      fhtml.write(parser_response.content['content'])
      fjson = open(sources + fname + '.json', 'wb')
      fjson.write(json.dumps(parser_response.content))
    finally:
        fhtml.close()
        fjson.close()
if __name__ == '__main__':
    main()