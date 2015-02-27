from blog.application.database import db
from blog.application.database import service
from blog.application import modules

# article = modules.Articles(uuid=None, author_id="wfefwewf", title="wxfweferfer", markdown="cdjoqwdmm", html="cefwefw",
# publish_time=None, update_time=None)
# tag_names = ["1", "2", "3"]
#
# service.save_or_update(article, tag_names)

# update_article = modules.Articles(uuid="02baa64f19014fc7b5740e9d76243e62", author_id="wfefdwewf", title="wfwedferfer",
#                                   markdown="cdjoqwddmm", html="cefwdefw",
#                                   publish_time="2015-02-27T11:37:21", update_time=None)
#
# tag_names = ["1", "2", "3", "4"]
#
# service.save_or_update(update_article, tag_names)

service.delete_by_ids(["02baa64f19014fc7b5740e9d76243e62"])
