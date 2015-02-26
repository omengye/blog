import sqlalchemy as sa

metadata = sa.MetaData()

articles = sa.Table(
    "articles", metadata,
    sa.Column("id", sa.String(32), primary_key=True),
    sa.Column("author_id", sa.String(32), nullable=False),
    sa.Column("title", sa.String(512), nullable=False),
    sa.Column("markdown", sa.UnicodeText(), nullable=False),
    sa.Column("html", sa.UnicodeText(), nullable=False),
    sa.Column("publish_time", sa.String(19), nullable=False),
    sa.Column("update_time", sa.String(19), nullable=True)
)

authors = sa.Table(
    "authors", metadata,
    sa.Column("id", sa.String(32), primary_key=True),
    sa.Column("author", sa.String(512), nullable=False),
    sa.Column("email", sa.String(512), nullable=True),
    sa.Column("passwd", sa.String(512), nullable=False)
)

tags = sa.Table(
    "tags", metadata,
    sa.Column("id", sa.String(32), primary_key=True),
    sa.Column("tag_name", sa.String(512), nullable=True),
    sa.Column("article_id", sa.String(32), nullable=True)
)


class Articles(object):
    def __init__(self, uuid, author_id, title, markdown, html, publish_time, update_time):
        self.id = uuid
        self.author_id = author_id
        self.title = title
        self.markdown = markdown
        self.html = html
        self.publish_time = publish_time
        self.update_time = update_time


class Authors(object):
    def __init__(self, uuid, author, email, passwd):
        self.id = uuid
        self.author = author
        self.email = email
        self.passwd = passwd


class Tags(object):
    def __init__(self, uuid, tag_name, article_id):
        self.id = uuid
        self.tag_name = tag_name
        self.article_id = article_id
