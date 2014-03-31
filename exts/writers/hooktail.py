from sphinx.writers.html import HTMLTranslator as BaseTranslator,\
		   SmartyPantsHTMLTranslator as BaseSmartyTranslator
def depart_title(self, node):
  BaseTranslator.depart_title(self, node)
  h_level = self.section_level + self.initial_header_level - 1
  if h_level == 1: del self.body[1:]
class HTMLTranslator(BaseTranslator): pass
class SmartyPantsHTMLTranslator(BaseSmartyTranslator): pass
setattr(HTMLTranslator           , 'depart_title', depart_title)
setattr(SmartyPantsHTMLTranslator, 'depart_title', depart_title)
