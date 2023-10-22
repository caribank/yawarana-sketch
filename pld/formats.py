from pylingdocs.formats import MkDocs
from pylingdocs.config import config
from pylingdocs.helpers import Enumerator
import re

class MkDocsOwn(MkDocs):

    name = "mkdocs"

    def postprocess(cls, content, metadata=None):
        content = re.sub(r"(?P<content>‘(.*?)) \(auto\)’", r"<span style='color: #BF616A'>[\g<content>’]{Machine-translated from Spanish.}</span>", content)
        metadata = metadata or {}
        if config["output"]["layout"] == "article":
            enm = Enumerator()
            out = []
            i = 1
            for line in content.split("\n"):
                if line.startswith("#"):
                    out.append(line.replace("# ", f"## {enm.parse(line)} "))
                    if line.startswith("# "):
                        i += 1
                else:
                    out.append(line)
            content = "#" + metadata["title"] + "\n\n" + "\n".join(out)
        return content

formats = []