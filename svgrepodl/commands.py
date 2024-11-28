import sys
import click
from .Url import Url
from .Message import Message
from .utils import downloader
from os.path import expanduser

def getUserDocumentPath():
	"""Locate Personal User document folder
	Returns:
		[string] -- Return destination download path
	"""
	return expanduser("~") + "/Documents/icons/"

@click.command()
@click.option('--path', '-p', default=getUserDocumentPath(), help="Change download destination path.")
@click.argument('url')
def cli(path, url):
	"""
 	SVG-REPO-DL

   	Description:	SVG image collection downloader
    			(fetches from svgrepo.com)
	
	Decorators:
		click.command
		click.option
		click.argument
	Arguments:
		path {[string]} -- Destination download path
		url {[string]} -- URL of SVGREPO Collection
	"""
	urlHelpers = Url(url) 
	if not urlHelpers.checker():
		Message.error('😱 Oops URL provided not match!')
		Message.info('💡 Your URL should look like this : https://svgrepo/collection/[id]')
		sys.exit()

	if(urlHelpers.httpGetResponse() != 404):
		Message.info('📣 Download will start for %s pack !' % urlHelpers.collectionName())
		downloader(url, path)
	else:
		Message.error("😱 Cannot get this URL!")
		sys.exit()
