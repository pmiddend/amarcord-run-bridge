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
from openapi_client.models.json_data_set import JsonDataSet
from openapi_client.models.json_indexing_parameters_with_results import JsonIndexingParametersWithResults
from openapi_client.models.json_run_range import JsonRunRange
from typing import Optional, Set
from typing_extensions import Self

class JsonDataSetWithIndexingResults(BaseModel):
    """
    JsonDataSetWithIndexingResults
    """ # noqa: E501
    data_set: JsonDataSet
    internal_run_ids: List[StrictInt]
    runs: List[JsonRunRange]
    point_group: StrictStr
    space_group: StrictStr
    cell_description: StrictStr
    indexing_results: List[JsonIndexingParametersWithResults]
    __properties: ClassVar[List[str]] = ["data_set", "internal_run_ids", "runs", "point_group", "space_group", "cell_description", "indexing_results"]

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
        """Create an instance of JsonDataSetWithIndexingResults from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data_set
        if self.data_set:
            _dict['data_set'] = self.data_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in runs (list)
        _items = []
        if self.runs:
            for _item_runs in self.runs:
                if _item_runs:
                    _items.append(_item_runs.to_dict())
            _dict['runs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in indexing_results (list)
        _items = []
        if self.indexing_results:
            for _item_indexing_results in self.indexing_results:
                if _item_indexing_results:
                    _items.append(_item_indexing_results.to_dict())
            _dict['indexing_results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonDataSetWithIndexingResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data_set": JsonDataSet.from_dict(obj["data_set"]) if obj.get("data_set") is not None else None,
            "internal_run_ids": obj.get("internal_run_ids"),
            "runs": [JsonRunRange.from_dict(_item) for _item in obj["runs"]] if obj.get("runs") is not None else None,
            "point_group": obj.get("point_group"),
            "space_group": obj.get("space_group"),
            "cell_description": obj.get("cell_description"),
            "indexing_results": [JsonIndexingParametersWithResults.from_dict(_item) for _item in obj["indexing_results"]] if obj.get("indexing_results") is not None else None
        })
        return _obj


