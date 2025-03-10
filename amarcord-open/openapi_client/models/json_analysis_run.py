# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from openapi_client.models.json_attributo_value import JsonAttributoValue
from openapi_client.models.json_run_file import JsonRunFile
from typing import Optional, Set
from typing_extensions import Self

class JsonAnalysisRun(BaseModel):
    """
    JsonAnalysisRun
    """ # noqa: E501
    id: StrictInt
    external_id: StrictInt
    attributi: List[JsonAttributoValue]
    file_paths: List[JsonRunFile]
    __properties: ClassVar[List[str]] = ["id", "external_id", "attributi", "file_paths"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of JsonAnalysisRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in attributi (list)
        _items = []
        if self.attributi:
            for _item_attributi in self.attributi:
                if _item_attributi:
                    _items.append(_item_attributi.to_dict())
            _dict['attributi'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in file_paths (list)
        _items = []
        if self.file_paths:
            for _item_file_paths in self.file_paths:
                if _item_file_paths:
                    _items.append(_item_file_paths.to_dict())
            _dict['file_paths'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonAnalysisRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "external_id": obj.get("external_id"),
            "attributi": [JsonAttributoValue.from_dict(_item) for _item in obj["attributi"]] if obj.get("attributi") is not None else None,
            "file_paths": [JsonRunFile.from_dict(_item) for _item in obj["file_paths"]] if obj.get("file_paths") is not None else None
        })
        return _obj


