from collections import Mapping, MutableSequence

json_data = {
    "glossary": {
        "title": "example glossary",
        "answer": 42,
        "boolean": True,
        "nada": None,
        "GlossDiv": {
            "GlossList": {
                "GlossEntry": {
                    "GlossDef": {
                        "GlossSeeAlso": ["GML", "XML"],
                        "para":
                        "A meta-markup language, used to create markup "
                        "languages such as DocBook."
                    },
                    "GlossSee": "markup",
                    "Acronym": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "SortAs": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "ID": "SGML"
                }
            },
            "title": "S"
        }
    }
}


def count_leaves(json_obj):
    def leaf_iterator(json_obj):
        if isinstance(json_obj, Mapping):
            for v in json_obj.values():
                for obj in leaf_iterator(v):
                    print(obj)
                    yield (obj)
        elif isinstance(json_obj, MutableSequence):
            for v in json_obj:
                for obj in leaf_iterator(v):
                    yield obj
        else:
            yield json_obj

    return sum(1 for leaf in leaf_iterator(json_obj))


leaf_count = count_leaves(json_data)
print('leaf count: {}'.format(leaf_count))  # -> leaf_count: 14
