import db_models
def login_in(username, password):
    try:
        t = db_models.User.query.filter_by(username="%s" % (username), password="%s" % (password) ).first()
        if username == "admin" and password == "admin":
            return 0
        elif t is None:
            return -1
        elif t is not None:
            return 1
    except:
        return -1



if __name__ == '__main__':
    print login_in('peter', 5555555)

