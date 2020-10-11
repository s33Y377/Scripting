import random

URLDict = dict()
alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
alnum = list(alphabets + alphabets.upper() + numbers)


def createShortURL():
    shortURL = ""
    while shortURL == "":
        while len(shortURL) < 6:
            shortURL += random.choice(alnum)
        if shortURL in URLDict.keys():
            shortURL = ""
    return shortURL


def shortenNonRedundant(newLongURL):
    for shortURL in URLDict.keys():
        if URLDict[shortURL] == newLongURL:
            return shortURL
    newShortURL = createShortURL()
    URLDict[newShortURL] = newLongURL
    return newShortURL


def shortenRedundant(newLongURL):
    newShortURL = createShortURL()
    URLDict[newShortURL] = newLongURL
    print(URLDict)
    return newShortURL


def restore(shortURL):
    if shortURL in URLDict.keys():
        return URLDict[shortURL]
    else:
        return None


def main():
    URLs = ["www.facebook.com", "www.google.com", "www.facebook.com"]

    print("Non-redundant Shortening:")
    for URL in URLs:
        shortURL = shortenNonRedundant(URL)
        print(shortURL, "-", restore(shortURL))

    print("\nRedundant Shortening:")
    for URL in URLs:
        shortURL = shortenRedundant(URL)
        print(shortURL, "-", restore(shortURL))


if __name__ == "__main__":
    main()
