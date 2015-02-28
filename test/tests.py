from application.database import db
from application.database import service
from application import modules
from application.utils import Utils




# article = modules.Articles(uuid=None, author_id="wfefwewf", title="wxfweferfer", markdown="cdjoqwdmm", html="cefwefw",
# publish_time=None, update_time=None)
# tag_names = ["1", "2", "3"]
#
# service.save_or_update(article, tag_names)

# update_article = modules.Articles(uuid="02baa64f19014fc7b5740e9d76243e62", author_id="wfefdwewf", title="wfwedferfer",
# markdown="cdjoqwddmm", html="cefwdefw",
# publish_time="2015-02-27T11:37:21", update_time=None)
#
# tag_names = ["1", "2", "3", "4"]
#
# service.save_or_update(update_article, tag_names)

# service.delete_by_ids(["02baa64f19014fc7b5740e9d76243e62"])

# import qrcode
#
#
# qr = qrcode.QRCode(
# version=1,
#     box_size=10,
#     border=4,
# )
# qr.add_data('test data1')
# qr.make(fit=True)
# img = qr.make_image()
# img.save('C:\\Users\\meng\\Documents\\code\\www\\blog\\test\\testpng.png')

author = modules.Authors(uuid=str(Utils.md5_pass("test")), author="test", email="test@root.com",
                         passwd=str(Utils.md5_pass("root")))

sql = modules.authors.insert().values(id=author.id, author=author.author, email=author.email, passwd=author.passwd)

db.run(sql)

# print(Utils.md5_pass("root"))