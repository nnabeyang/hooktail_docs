# -*- coding: utf-8 -*-
from writers.hooktail import HTMLTranslator, \
     SmartyPantsHTMLTranslator
from sphinx.builders.html import StandaloneHTMLBuilder
import mathjax
class HooktailBuilder(StandaloneHTMLBuilder):
    name = 'hooktail'
    def __init__(self, app):
        StandaloneHTMLBuilder.__init__(self, app)
    def init_translator_class(self):
        if self.config.html_translator_class:
            self.translator_class = self.app.import_object(
                self.config.html_translator_class,
                'html_translator_class setting')
        elif self.config.html_use_smartypants:
            self.translator_class = SmartyPantsHTMLTranslator
        else:
            self.translator_class = HTMLTranslator
    def write_doc(self, docname, doctree):
        mathjax.counter = mathjax.ExpressionNumbers()
        StandaloneHTMLBuilder.write_doc(self, docname, doctree)
