# -*- coding: utf-8 -*-
from docutils import nodes
from sphinx.application import ExtensionError
from sphinx.ext.mathbase import setup_math as mathbase_setup,\
		                math, displaymath, eqref
import re
class ExpressionNumbers(object):
    def __init__(self, start=1):
        self.count = start - 1
    def __call__(self, match):
        self.count += 1
        return "\\tag{%d}" % self.count
counter = ExpressionNumbers()
tagRegex = re.compile(re.escape("\\tag{##}"), re.S | re.M)
def html_visit_math(self, node):
    self.body.append(self.starttag(node, 'span', '', CLASS='math'))
    self.body.append(self.builder.config.mathjax_inline[0] +
                     self.encode(node['latex']) +
                     self.builder.config.mathjax_inline[1] + '</span>')
    raise nodes.SkipNode
def html_visit_displaymath(self, node):
    node['latex'] = re.sub(tagRegex, counter, node['latex'])
    self.body.append(self.starttag(node, 'div', CLASS='math'))
    if node['nowrap']:
        self.body.append(self.builder.config.mathjax_display[0] +
                         node['latex'] +
                         self.builder.config.mathjax_display[1])
        self.body.append('</div>')
        raise nodes.SkipNode

    parts = [prt for prt in node['latex'].split('\n\n') if prt.strip()]
    for i, part in enumerate(parts):
        part = self.encode(part)
        if i == 0:
            # necessary to e.g. set the id property correctly
            if node['number']:
                self.body.append('<span class="eqno">(%s)</span>' %
                                 node['number'])
        if '&' in part or '\\\\' in part:
            self.body.append(self.builder.config.mathjax_display[0] +
                             '\\begin{align*}' + part + '\\end{align*}' +
                             self.builder.config.mathjax_display[1])
        else:
            self.body.append(self.builder.config.mathjax_display[0] + part +
                             self.builder.config.mathjax_display[1])
    self.body.append('</div>\n')
    raise nodes.SkipNode

def builder_inited(app):
    if not app.config.mathjax_path:
        raise ExtensionError('mathjax_path config value must be set for the '
                             'mathjax extension to work')
    app.add_javascript(app.config.mathjax_path)

def html_page_context(app, pagename, templatename, context, doctree):
    if app.config.mathjax_preamble and 'body' in context:
        preamble = ''.join(['<div id="preamble" style="display:none">',
                            app.config.mathjax_inline[0],
                            app.config.mathjax_preamble,
                            app.config.mathjax_inline[1], '</div>\n'])
        context['body'] = preamble + context['body']

def setup(app):
    mathbase_setup(app, (html_visit_math, None), (html_visit_displaymath, None))
    app.add_config_value('mathjax_path',
                         'http://cdn.mathjax.org/mathjax/latest/MathJax.js?'
                         'config=TeX-AMS-MML_HTMLorMML', False)
    app.add_config_value('mathjax_preamble', False, 'html')
    app.add_config_value('mathjax_inline', [r'\(', r'\)'], 'html')
    app.add_config_value('mathjax_display', [r'\[', r'\]'], 'html')
    app.connect('builder-inited', builder_inited)
    app.connect('html-page-context', html_page_context)
