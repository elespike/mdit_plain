import unittest

from json import load
from pathlib import Path
from re import compile

from markdown_it import MarkdownIt
from mdit_plain.renderer import HTMLTextRenderer, RendererPlain


class TestRendererPlain(unittest.TestCase):
    def test_commonmark(self):
        # https://spec.commonmark.org/0.30/spec.json
        with open(F"{Path(__file__).parent.resolve()}/spec_0.30.json") as f:
            cm_tests = load(f)

        parser = MarkdownIt('commonmark', renderer_cls=RendererPlain)
        htmlparser = HTMLTextRenderer()
        whitespace = compile('\s+')

        # These exclusions were manually tested.
        exclusions = [171, 516, 519, 530, 596, 615, 629]
        cm_tests = [
            t for t in cm_tests
            # Skipping image tests because the "alt" attribute
            # is displayed as text, but does not count as HTML text.
            if t['section'] != 'Images'
            and t['example'] not in exclusions
        ]

        for test in cm_tests:
            print(F"Example {test['example']}... ", end='', flush=True)
            rendered_md = parser.render(test['markdown'])
            rendered_html = htmlparser.render(test['html']).strip()
            self.assertEqual(
                # Normalize spaces because some HTML tags (like <p>) have implicit spacing.
                whitespace.sub(' ', rendered_md),
                whitespace.sub(' ', rendered_html)
            )
            print(F"OK: {repr(rendered_md)}")

