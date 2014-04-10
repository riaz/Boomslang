Boomslang
=========

Boomslang Web Crawler implemented using Python

Gragger:
 Given a  url form the url queue, the grabbers actually grabs information pertained to the given
 link like : meta data, keywords,contents, etc.
     Initially a single base url is provided in the file : Boomslang.py

Note 1: If the initial seed , doesn't contain any link to another site/s , the usage
of the web crawler is diminished as the url_queue is certain to run out of url
to collect data.

Note 2: Always choose a seed url that is divergant in nature , so to have huge
informatin collected over time.You can set the seed url in the file Boomslang.py

 
Parser:
    Parser takes the content_url and tries to filter thr url from rest of the
contents, the visited links are stored in the database, so the parser checks if the
url currently parsed out, is among the one's already stored in the db, if no, meaning
new links so we append those links to the url_queue , consumable by the grabber,
if the link was already visited simply discard it.

Boomslang:
    This is the one that starts the deamon to being the Grabbing and the Parsing
    activity.Also, we set the base url to initiate the crawling here

Warning: The web crawler needs to respect the robot.txt file of respected sites
to have info of what it is authorized for, defaulting in this space may result into
banning of the ip for from access their site.





 
