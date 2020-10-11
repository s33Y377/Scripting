from dictdiffer import diff  # , patch, swap, revert

result = diff({"a": "b"}, {"a": "c"})
print(list(result))

# first = {
#     "title": "hello",
#     "fork_count": 20,
#     "stargazers": ["/users/20", "/users/30"],
#     "settings": {
#         "assignees": [100, 101, 201],
#     }
# }
#
# second = {
#     "title": "hellooo",
#     "fork_count": 20,
#     "stargazers": ["/users/20", "/users/30", "/users/40"],
#     "settings": {
#         "assignees": [100, 101, 202],
#     }
# }
#
# result = diff(first, second)
# for x in result:
#     print(x)
