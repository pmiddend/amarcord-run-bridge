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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from amarcord_open.models.json_beamtime import JsonBeamtime
from amarcord_open.models.json_experiment_type import JsonExperimentType
from typing import Optional, Set
from typing_extensions import Self

class JsonExperimentTypeWithBeamtimeInformation(BaseModel):
    """
    JsonExperimentTypeWithBeamtimeInformation
    """ # noqa: E501
    experiment_type: JsonExperimentType
    beamtime: JsonBeamtime
    __properties: ClassVar[List[str]] = ["experiment_type", "beamtime"]

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
        """Create an instance of JsonExperimentTypeWithBeamtimeInformation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of experiment_type
        if self.experiment_type:
            _dict['experiment_type'] = self.experiment_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of beamtime
        if self.beamtime:
            _dict['beamtime'] = self.beamtime.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonExperimentTypeWithBeamtimeInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "experiment_type": JsonExperimentType.from_dict(obj["experiment_type"]) if obj.get("experiment_type") is not None else None,
            "beamtime": JsonBeamtime.from_dict(obj["beamtime"]) if obj.get("beamtime") is not None else None
        })
        return _obj


