# -*- coding: utf-8 -*-
import codecs
from sphinx.builders.text import TextBuilder
from writers.rst import ReSTWriter
from docutils.io import StringOutput
from os import path, linesep

from sphinx.util.osutil import ensuredir, os_path, ustrftime
class ReSTBuilder(TextBuilder):
    name = 'rst'
    format = 'text'
    out_suffix = '.rst'
    allow_parallel = True
    categories = {
      'welcome' : u"ようこそ,物理の世界へ",
      'mathInPhys': u"物理数学",
      'mechanics': u"力学",
      'algebra': u"代数学",
      'differentialforms': u"微分形式",
      'vectoranalysis': u"ベクトル解析",
      'fourieralysis': u"フーリエ解析",
      'elemag': u"電磁気学",
      'thermo': u"熱力学",
      'wave': u"波と振動",
      'elastic': u"弾性体力学",
      'fluid': u"流体力学",
      'flightDynamics': u"飛行力学",
      'statistical': u"統計力学",
      'analytic': u"解析力学",
      'quantum': u"量子力学",
      'relativity': u"相対論",
      'solid': u"固体物理学",
      'astronomy': u"天文学",
      'computPhys': u"計算物理学",
      'energy': u"エネルギーのもんだい",
      'nocategory': u"その他",
      'bbs': u"掲示板",
      'info': u"案内",
      'sandbox': u"サンドボックス"
    }
    def prepare_writing(self, docnames):
        self.writer = ReSTWriter(self)
    def write_doc(self, docname, doctree):
        self.current_docname = docname
        destination = StringOutput(encoding='utf-8')
        self.writer.write(doctree, destination)
        outfilename = path.join(self.outdir, os_path(docname) + self.out_suffix)
        ensuredir(path.dirname(outfilename))
        try:
            f = codecs.open(outfilename, 'w', 'utf-8')
            try:
		f.write("#rst2hooktail_source" + (linesep*2))
		for link in self.writer.links:
		  f.write(".. _%s: %s%s" % (link.children[0].astext(), link['refuri'], linesep))
                f.write(linesep)

                f.write(self.writer.output)
		f.write("@@author:%s@@%s" % (self.config.copyright[6:], linesep))
		f.write("@@accept:%s@@%s" % (ustrftime("%Y-%m-%d"), linesep))
		relations = self.env.collect_relations().get(docname)
		if relations and relations[0] and relations[0] != "index":
		  f.write("@@category:%s@@%s" % (self.categories[relations[0]], linesep))
		f.write("@@id:%s@@%s" % (docname.replace('/', '_'), linesep))
            finally:
                f.close()
        except (IOError, OSError) as err:
            self.warn("error writing file %s: %s" % (outfilename, err))


