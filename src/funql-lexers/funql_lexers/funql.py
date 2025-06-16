"""A Pygments lexer for FunQL."""
from pygments.lexer import RegexLexer, bygroups, include, using
from pygments.token import *
from pygments.lexers.data import JsonLexer

__all__ = ("FunQLLexer",)


class FunQLLexer(RegexLexer):

    """
    Simple lexer to highlight a specific format. For example:

        year(field: DateTime): Integer
    
    See https://pygments.org/docs/lexerdevelopment/
    See https://pygments.org/docs/tokens/
    See https://squidfunk.github.io/mkdocs-material/reference/code-blocks/
    """

    name = 'FunQL'
    aliases = ['funql']
    filenames = ['*.funql']
    mimetypes = ['text/funql']

    tokens = {
        'comments': [
            (r'//.*?$', Comment.Single)
        ],
        'function': [
            # Function start is defined with 'function('
            (r'([a-zA-Z][a-zA-Z0-9]*)(\()', bygroups(Name.Function, Punctuation), 'functionBody'),
            # Function may define return type with ': Type'
            (r'(\))(?=:)', Punctuation, 'type'),
        ],
        'functionBody': [
            include('comments'),
            # Function may have nested functions
            include('function'),
            # Special JSON keywords should come before fields
            (r'true|false|null', using(JsonLexer)),
            # Fields (field | field.nested | field["nested"]), must come before JSON array, otherwise field bracket 
            # notation ('["field"]') may be parsed as JSON array
            (r'(?:[a-zA-Z][a-zA-Z0-9]*(?:\["([^"\\]|\\.)*"\])*\.*)+', Name.Variable),
            # JSON object
            (r'\{.+?\}', using(JsonLexer)),
            # JSON array
            (r'\[.+?\]', using(JsonLexer)),
            # JSON string (with support for escaped quotes '\"')
            (r'"([^"\\]|\\.)*"', using(JsonLexer)),
            # JSON number
            (r'\d*\.?\d+', using(JsonLexer)),
            include('type'),
            (r'\s', Whitespace),
            (r',', Punctuation),
            (r'\)', Punctuation, '#pop')
        ],
        'type': [
            # Types are defined with ': Type'
            (r'(:)(\s*)([A-Z][a-zA-Z0-9]*)', bygroups(Punctuation, Whitespace, Keyword.Type)),
            # Union types are defined with '| Type'
            (r'(\|)(\s*)([A-Z][a-zA-Z0-9]*)', bygroups(Punctuation, Whitespace, Keyword.Type))
        ],
        'root': [
            include('comments'),
            include('function'),
            (r'\s', Whitespace)
        ],
    }
