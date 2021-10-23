

from hargrave_base.database.db import * 


class time:

    def html():
        pass

    def edit_html():
        pass

    def backend():
        pass

    def db_columns():
        Column('id', DateTime, primary_key=True),
        *(Column(wordCol, Unicode(255)) for wordCol in wordColumns)

    def __init__():
        # register_hook 
        pass