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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class JsonIndexingResultStillRunning(BaseModel):
    """
    JsonIndexingResultStillRunning
    """ # noqa: E501
    workload_manager_job_id: StrictInt
    stream_file: StrictStr
    frames: StrictInt
    hits: StrictInt
    indexed_frames: StrictInt
    indexed_crystals: StrictInt
    detector_shift_x_mm: Optional[Union[StrictFloat, StrictInt]] = None
    detector_shift_y_mm: Optional[Union[StrictFloat, StrictInt]] = None
    geometry_file: StrictStr
    geometry_hash: StrictStr
    job_started: Optional[StrictInt] = None
    latest_log: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["workload_manager_job_id", "stream_file", "frames", "hits", "indexed_frames", "indexed_crystals", "detector_shift_x_mm", "detector_shift_y_mm", "geometry_file", "geometry_hash", "job_started", "latest_log"]

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
        """Create an instance of JsonIndexingResultStillRunning from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonIndexingResultStillRunning from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workload_manager_job_id": obj.get("workload_manager_job_id"),
            "stream_file": obj.get("stream_file"),
            "frames": obj.get("frames"),
            "hits": obj.get("hits"),
            "indexed_frames": obj.get("indexed_frames"),
            "indexed_crystals": obj.get("indexed_crystals"),
            "detector_shift_x_mm": obj.get("detector_shift_x_mm"),
            "detector_shift_y_mm": obj.get("detector_shift_y_mm"),
            "geometry_file": obj.get("geometry_file"),
            "geometry_hash": obj.get("geometry_hash"),
            "job_started": obj.get("job_started"),
            "latest_log": obj.get("latest_log")
        })
        return _obj


