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


def process_docs_o_m(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        prompt = "请根据以下场景，你认为" + doc["角度"] + "应该怎么做？请选出最恰当的选项。"
        content = prompt + doc['问题'][7:] + "行为A：" +doc['选项A'].replace("你",doc["角度"]) +"行为B：" + doc['选项B'].replace("你",doc["角度"]) + "行为C：" + doc['选项C'].replace("你",doc["角度"])
        out_doc = {
            "query": content,
            "choices": [doc["选项A"],doc["选项B"],doc["选项C"]],
            "gold": int(ord(doc['正确答案'])-ord('A')),
        }
        # pdb.set_trace()
        # print(out_doc)
        # return out_doc
        doc["query"] = out_doc["query"]
        doc["choices"] = out_doc["choices"]
        doc["gold"] = out_doc["gold"]
        return doc

    return dataset.map(_process_doc)


def process_docs_no_m(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        prompt = "请根据以下场景，你认为" + doc["角度"] + "应该怎么做？请选出最恰当的选项。"
        content = prompt + doc['问题'] + "行为A：" +doc['选项A'] +"行为B：" + doc['选项B'] + "行为C：" + doc['选项C']
        out_doc = {
            "query": content,
            "choices": [doc["选项A"],doc["选项B"],doc["选项C"]],
            "gold": int(ord(doc['正确答案'])-ord('A')),
        }
        # pdb.set_trace()
        # print(out_doc)
        # return out_doc
        doc["query"] = out_doc["query"]
        doc["choices"] = out_doc["choices"]
        doc["gold"] = out_doc["gold"]
        return doc

    return dataset.map(_process_doc)

def process_docs_o_nm(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        prompt = "请根据以下场景，你认为" + doc["角度"] + "不应该怎么做？请选出最恰当的选项。"
        content = prompt + doc['问题'][7:] + "行为A：" +doc['选项A'].replace("你",doc["角度"]) +"行为B：" + doc['选项B'].replace("你",doc["角度"]) + "行为C：" + doc['选项C'].replace("你",doc["角度"])
        out_doc = {
            "query": content,
            "choices": [doc["选项A"],doc["选项B"],doc["选项C"]],
            "gold": int(ord(doc['错误答案'])-ord('A')),
        }
        # pdb.set_trace()
        # print(out_doc)
        # return out_doc
        doc["query"] = out_doc["query"]
        doc["choices"] = out_doc["choices"]
        doc["gold"] = out_doc["gold"]
        return doc

    return dataset.map(_process_doc)


def process_docs_no_nm(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        prompt = "请根据以下场景，你认为" + doc["角度"] + "不应该怎么做？请选出最恰当的选项。"
        content = prompt + doc['问题'] + "行为A：" +doc['选项A'] +"行为B：" + doc['选项B'] + "行为C：" + doc['选项C']
        out_doc = {
            "query": content,
            "choices": [doc["选项A"],doc["选项B"],doc["选项C"]],
            "gold": int(ord(doc['错误答案'])-ord('A')),
        }
        # pdb.set_trace()
        # print(out_doc)
        # return out_doc
        doc["query"] = out_doc["query"]
        doc["choices"] = out_doc["choices"]
        doc["gold"] = out_doc["gold"]
        return doc

    return dataset.map(_process_doc)
