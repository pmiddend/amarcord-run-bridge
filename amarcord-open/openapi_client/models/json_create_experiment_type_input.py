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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_client.models.json_attributi_id_and_role import JsonAttributiIdAndRole
from typing import Optional, Set
from typing_extensions import Self

class JsonCreateExperimentTypeInput(BaseModel):
    """
    JsonCreateExperimentTypeInput
    """ # noqa: E501
    name: StrictStr
    beamtime_id: StrictInt
    attributi: List[JsonAttributiIdAndRole]
    __properties: ClassVar[List[str]] = ["name", "beamtime_id", "attributi"]

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
        """Create an instance of JsonCreateExperimentTypeInput from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonCreateExperimentTypeInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "beamtime_id": obj.get("beamtime_id"),
            "attributi": [JsonAttributiIdAndRole.from_dict(_item) for _item in obj["attributi"]] if obj.get("attributi") is not None else None
        })
        return _obj


