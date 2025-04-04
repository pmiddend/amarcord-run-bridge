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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from amarcord_open.models.json_merge_result_outer_shell import JsonMergeResultOuterShell
from typing import Optional, Set
from typing_extensions import Self

class JsonMergeResultFom(BaseModel):
    """
    JsonMergeResultFom
    """ # noqa: E501
    snr: Union[StrictFloat, StrictInt]
    wilson: Optional[Union[StrictFloat, StrictInt]] = None
    ln_k: Optional[Union[StrictFloat, StrictInt]] = None
    discarded_reflections: StrictInt
    one_over_d_from: Union[StrictFloat, StrictInt]
    one_over_d_to: Union[StrictFloat, StrictInt]
    redundancy: Union[StrictFloat, StrictInt]
    completeness: Union[StrictFloat, StrictInt]
    measurements_total: StrictInt
    reflections_total: StrictInt
    reflections_possible: StrictInt
    r_split: Union[StrictFloat, StrictInt]
    r1i: Union[StrictFloat, StrictInt]
    r2: Union[StrictFloat, StrictInt]
    cc: Union[StrictFloat, StrictInt]
    ccstar: Union[StrictFloat, StrictInt]
    ccano: Optional[Union[StrictFloat, StrictInt]] = None
    crdano: Optional[Union[StrictFloat, StrictInt]] = None
    rano: Optional[Union[StrictFloat, StrictInt]] = None
    rano_over_r_split: Optional[Union[StrictFloat, StrictInt]] = None
    d1sig: Union[StrictFloat, StrictInt]
    d2sig: Union[StrictFloat, StrictInt]
    outer_shell: JsonMergeResultOuterShell
    __properties: ClassVar[List[str]] = ["snr", "wilson", "ln_k", "discarded_reflections", "one_over_d_from", "one_over_d_to", "redundancy", "completeness", "measurements_total", "reflections_total", "reflections_possible", "r_split", "r1i", "r2", "cc", "ccstar", "ccano", "crdano", "rano", "rano_over_r_split", "d1sig", "d2sig", "outer_shell"]

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
        """Create an instance of JsonMergeResultFom from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of outer_shell
        if self.outer_shell:
            _dict['outer_shell'] = self.outer_shell.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonMergeResultFom from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "snr": obj.get("snr"),
            "wilson": obj.get("wilson"),
            "ln_k": obj.get("ln_k"),
            "discarded_reflections": obj.get("discarded_reflections"),
            "one_over_d_from": obj.get("one_over_d_from"),
            "one_over_d_to": obj.get("one_over_d_to"),
            "redundancy": obj.get("redundancy"),
            "completeness": obj.get("completeness"),
            "measurements_total": obj.get("measurements_total"),
            "reflections_total": obj.get("reflections_total"),
            "reflections_possible": obj.get("reflections_possible"),
            "r_split": obj.get("r_split"),
            "r1i": obj.get("r1i"),
            "r2": obj.get("r2"),
            "cc": obj.get("cc"),
            "ccstar": obj.get("ccstar"),
            "ccano": obj.get("ccano"),
            "crdano": obj.get("crdano"),
            "rano": obj.get("rano"),
            "rano_over_r_split": obj.get("rano_over_r_split"),
            "d1sig": obj.get("d1sig"),
            "d2sig": obj.get("d2sig"),
            "outer_shell": JsonMergeResultOuterShell.from_dict(obj["outer_shell"]) if obj.get("outer_shell") is not None else None
        })
        return _obj


