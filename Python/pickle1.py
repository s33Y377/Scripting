import pickle


def storedata():
    omkar = {"key": "Omkar", "name": "Omkar Pathak", "age": 21, "pay": 40000}
    jagdish = {"key": "Jagdish", "name": "Jagdish Pathak", "age": 50, "pay": 50000}
    db = {}
    db["Omkar"] = omkar
    db["Jagdish"] = jagdish
    dbfile = open("examplePickle", "ab")
    pickle.dump(db, dbfile)
    dbfile.close()


def loaddata():
    dbfile = open("examplePickle", "rb")
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, "=>", db[keys])
    dbfile.close()


if __name__ == "__main__":
    storedata()
    loaddata()
