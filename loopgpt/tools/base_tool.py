from typing import *
import json
import re


def camel_case_split(str):
    return re.findall(r"[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))", str)


class BaseTool:
    @property
    def id(self) -> str:
        return "_".join(camel_case_split(self.__class__.__name__)).lower()

    @property
    def desc(self) -> str:
        return " ".join(camel_case_split(self.__class__.__name__))

    @property
    def args(self) -> Dict[str, str]:
        raise NotImplementedError()

    def run(**kwrags) -> str:
        raise NotImplementedError()

    @property
    def resp(self) -> Dict[str, str]:
        raise NotImplementedError()

    def prompt(self):
        return f"{self.id}: " + json.dumps(
            {"name": self.id, "args": self.args, "response_format": self.resp}
        )
