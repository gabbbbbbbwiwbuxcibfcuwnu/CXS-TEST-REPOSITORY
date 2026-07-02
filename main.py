from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def home():
    return Titled(
        "CXS",
        H1("Welcome to CXS!"),
        P("Your FastHTML app is working.")
    )
