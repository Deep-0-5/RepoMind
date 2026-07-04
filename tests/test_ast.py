# import ast

# code = """
# def login():
#     print("Login")

# class User:
#     pass

# def logout():
#     print("Logout")
# """

# tree = ast.parse(code)

# for node in tree.body:
#     print(type(node).__name__, getattr(node, "name", None))

import ast

code = """
def login():
    print("Login")

class User:
    pass

def logout():
    print("Logout")
"""

tree = ast.parse(code)

for node in tree.body:
    source = ast.get_source_segment(code, node)

    print("=" * 40)
    print(type(node).__name__)
    print(source)