# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = predict_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Image:
    id: str
    content: str

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        content = from_str(obj.get("content"))
        return Image(id, content)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["content"] = from_str(self.content)
        return result


@dataclass
class Predict:
    id_client: str
    images: List[Image]
    models: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Predict':
        assert isinstance(obj, dict)
        id_client = from_str(obj.get("id_client"))
        images = from_list(Image.from_dict, obj.get("images"))
        models = from_list(from_str, obj.get("models"))
        return Predict(id_client, images, models)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id_client"] = from_str(self.id_client)
        result["images"] = from_list(lambda x: to_class(Image, x), self.images)
        result["models"] = from_list(from_str, self.models)
        return result


def predict_from_dict(s: Any) -> Predict:
    return Predict.from_dict(s)


def predict_to_dict(x: Predict) -> Any:
    return to_class(Predict, x)
