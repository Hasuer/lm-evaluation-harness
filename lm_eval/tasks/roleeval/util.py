import pdb
import datasets
import re


def preprocess(text):
    text = text.strip()
    # NOTE: Brackets are artifacts of the WikiHow dataset portion of HellaSwag.
    text = text.replace(" [title]", ". ")
    text = re.sub("\\[.*?\\]", "", text)
    text = text.replace("  ", " ")
    return text


def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    mapping = {
        "anime_and_comics": "动漫角色",
        "celebrities": "名人",
        "fiction": "小说人物",
        "games": "游戏角色",
        "movies_and_TV_series": "影视角色"
    }
    def _process_doc(doc):
        prompt = "以下是关于" + mapping[doc["topic"]] + "的单项选择题，请选出其中的正确答案。"
        content = prompt + "\n\n" + doc['问题'] + "\n" + "A. " +doc['A'] + "\n" + "B. " + doc['B'] + "\n" + "C. " + doc['C'] + "\n" + "D. " + doc['D'] + "\n" + "答案："
        out_doc = {
            "query": content,
            "choices": ["A", "B", "C", "D"],
            "gold": int(ord(doc['正确答案'])-ord('A')),
        }
        doc["query"] = out_doc["query"]
        doc["choices"] = out_doc["choices"]
        doc["gold"] = out_doc["gold"]
        return doc

    return dataset.map(_process_doc)
