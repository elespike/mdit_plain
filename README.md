# Why?
To facilitate Natural Language Processing of markdown documents by converting them to plain text documents.

# Installation
```shell
# Requires Python 3.7 or higher
python3 -m pip install mdit_plain
```

# Usage
```
>>> from markdown_it import MarkdownIt  # python3 -m pip install markdown-it-py
>>> from mdit_plain.renderer import RendererPlain
>>> parser = MarkdownIt(renderer_cls=RendererPlain)
>>> print(parser.render(
... """
... # Lots of markdown
... **Quite** a *lot*!
... > oh yeah...
... """
... ))
Lots of markdown

Quite a lot!

oh yeah...
```

# Development and Testing
```shell
# Requires Python 3.7 or higher
git clone https://github.com/elespike/mdit_plain
cd mdit_plain
python3 -m pip install .[test]
python3 -m unittest
```

