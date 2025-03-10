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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.json_polarisation import JsonPolarisation
from openapi_client.models.merge_model import MergeModel
from openapi_client.models.merge_negative_handling import MergeNegativeHandling
from openapi_client.models.scale_intensities import ScaleIntensities
from typing import Optional, Set
from typing_extensions import Self

class JsonMergeParameters(BaseModel):
    """
    JsonMergeParameters
    """ # noqa: E501
    point_group: StrictStr
    space_group: Optional[StrictStr] = None
    cell_description: StrictStr
    negative_handling: Optional[MergeNegativeHandling] = None
    merge_model: MergeModel
    scale_intensities: ScaleIntensities
    post_refinement: StrictBool
    iterations: StrictInt
    polarisation: Optional[JsonPolarisation] = None
    start_after: Optional[StrictInt] = None
    stop_after: Optional[StrictInt] = None
    rel_b: Union[StrictFloat, StrictInt]
    no_pr: StrictBool
    force_bandwidth: Optional[Union[StrictFloat, StrictInt]] = None
    force_radius: Optional[Union[StrictFloat, StrictInt]] = None
    force_lambda: Optional[Union[StrictFloat, StrictInt]] = None
    no_delta_cc_half: StrictBool
    max_adu: Optional[Union[StrictFloat, StrictInt]] = None
    min_measurements: StrictInt
    logs: StrictBool
    min_res: Optional[Union[StrictFloat, StrictInt]] = None
    push_res: Optional[Union[StrictFloat, StrictInt]] = None
    w: Optional[StrictStr] = None
    ambigator_command_line: StrictStr
    __properties: ClassVar[List[str]] = ["point_group", "space_group", "cell_description", "negative_handling", "merge_model", "scale_intensities", "post_refinement", "iterations", "polarisation", "start_after", "stop_after", "rel_b", "no_pr", "force_bandwidth", "force_radius", "force_lambda", "no_delta_cc_half", "max_adu", "min_measurements", "logs", "min_res", "push_res", "w", "ambigator_command_line"]

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
        """Create an instance of JsonMergeParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of polarisation
        if self.polarisation:
            _dict['polarisation'] = self.polarisation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonMergeParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "point_group": obj.get("point_group"),
            "space_group": obj.get("space_group"),
            "cell_description": obj.get("cell_description"),
            "negative_handling": obj.get("negative_handling"),
            "merge_model": obj.get("merge_model"),
            "scale_intensities": obj.get("scale_intensities"),
            "post_refinement": obj.get("post_refinement"),
            "iterations": obj.get("iterations"),
            "polarisation": JsonPolarisation.from_dict(obj["polarisation"]) if obj.get("polarisation") is not None else None,
            "start_after": obj.get("start_after"),
            "stop_after": obj.get("stop_after"),
            "rel_b": obj.get("rel_b"),
            "no_pr": obj.get("no_pr"),
            "force_bandwidth": obj.get("force_bandwidth"),
            "force_radius": obj.get("force_radius"),
            "force_lambda": obj.get("force_lambda"),
            "no_delta_cc_half": obj.get("no_delta_cc_half"),
            "max_adu": obj.get("max_adu"),
            "min_measurements": obj.get("min_measurements"),
            "logs": obj.get("logs"),
            "min_res": obj.get("min_res"),
            "push_res": obj.get("push_res"),
            "w": obj.get("w"),
            "ambigator_command_line": obj.get("ambigator_command_line")
        })
        return _obj


