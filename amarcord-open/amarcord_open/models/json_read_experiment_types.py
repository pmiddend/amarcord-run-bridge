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
from typing import Any, ClassVar, Dict, List, Optional
from amarcord_open.models.json_attributo import JsonAttributo
from amarcord_open.models.json_experiment_type import JsonExperimentType
from amarcord_open.models.json_experiment_type_and_runs import JsonExperimentTypeAndRuns
from typing import Optional, Set
from typing_extensions import Self

class JsonReadExperimentTypes(BaseModel):
    """
    JsonReadExperimentTypes
    """ # noqa: E501
    experiment_types: List[JsonExperimentType]
    attributi: List[JsonAttributo]
    experiment_type_id_to_run: List[JsonExperimentTypeAndRuns]
    current_experiment_type_id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["experiment_types", "attributi", "experiment_type_id_to_run", "current_experiment_type_id"]

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
        """Create an instance of JsonReadExperimentTypes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in experiment_types (list)
        _items = []
        if self.experiment_types:
            for _item_experiment_types in self.experiment_types:
                if _item_experiment_types:
                    _items.append(_item_experiment_types.to_dict())
            _dict['experiment_types'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attributi (list)
        _items = []
        if self.attributi:
            for _item_attributi in self.attributi:
                if _item_attributi:
                    _items.append(_item_attributi.to_dict())
            _dict['attributi'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in experiment_type_id_to_run (list)
        _items = []
        if self.experiment_type_id_to_run:
            for _item_experiment_type_id_to_run in self.experiment_type_id_to_run:
                if _item_experiment_type_id_to_run:
                    _items.append(_item_experiment_type_id_to_run.to_dict())
            _dict['experiment_type_id_to_run'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonReadExperimentTypes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "experiment_types": [JsonExperimentType.from_dict(_item) for _item in obj["experiment_types"]] if obj.get("experiment_types") is not None else None,
            "attributi": [JsonAttributo.from_dict(_item) for _item in obj["attributi"]] if obj.get("attributi") is not None else None,
            "experiment_type_id_to_run": [JsonExperimentTypeAndRuns.from_dict(_item) for _item in obj["experiment_type_id_to_run"]] if obj.get("experiment_type_id_to_run") is not None else None,
            "current_experiment_type_id": obj.get("current_experiment_type_id")
        })
        return _obj


