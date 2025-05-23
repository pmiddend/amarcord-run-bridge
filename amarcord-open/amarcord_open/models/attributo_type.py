# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from amarcord_open.models.json_schema_array import JSONSchemaArray
from amarcord_open.models.json_schema_boolean import JSONSchemaBoolean
from amarcord_open.models.json_schema_integer import JSONSchemaInteger
from amarcord_open.models.json_schema_number import JSONSchemaNumber
from amarcord_open.models.json_schema_string import JSONSchemaString
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ATTRIBUTOTYPE_ONE_OF_SCHEMAS = ["JSONSchemaArray", "JSONSchemaBoolean", "JSONSchemaInteger", "JSONSchemaNumber", "JSONSchemaString"]

class AttributoType(BaseModel):
    """
    AttributoType
    """
    # data type: JSONSchemaInteger
    oneof_schema_1_validator: Optional[JSONSchemaInteger] = None
    # data type: JSONSchemaNumber
    oneof_schema_2_validator: Optional[JSONSchemaNumber] = None
    # data type: JSONSchemaString
    oneof_schema_3_validator: Optional[JSONSchemaString] = None
    # data type: JSONSchemaArray
    oneof_schema_4_validator: Optional[JSONSchemaArray] = None
    # data type: JSONSchemaBoolean
    oneof_schema_5_validator: Optional[JSONSchemaBoolean] = None
    actual_instance: Optional[Union[JSONSchemaArray, JSONSchemaBoolean, JSONSchemaInteger, JSONSchemaNumber, JSONSchemaString]] = None
    one_of_schemas: Set[str] = { "JSONSchemaArray", "JSONSchemaBoolean", "JSONSchemaInteger", "JSONSchemaNumber", "JSONSchemaString" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = AttributoType.model_construct()
        error_messages = []
        match = 0
        # validate data type: JSONSchemaInteger
        if not isinstance(v, JSONSchemaInteger):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JSONSchemaInteger`")
        else:
            match += 1
        # validate data type: JSONSchemaNumber
        if not isinstance(v, JSONSchemaNumber):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JSONSchemaNumber`")
        else:
            match += 1
        # validate data type: JSONSchemaString
        if not isinstance(v, JSONSchemaString):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JSONSchemaString`")
        else:
            match += 1
        # validate data type: JSONSchemaArray
        if not isinstance(v, JSONSchemaArray):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JSONSchemaArray`")
        else:
            match += 1
        # validate data type: JSONSchemaBoolean
        if not isinstance(v, JSONSchemaBoolean):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JSONSchemaBoolean`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in AttributoType with oneOf schemas: JSONSchemaArray, JSONSchemaBoolean, JSONSchemaInteger, JSONSchemaNumber, JSONSchemaString. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in AttributoType with oneOf schemas: JSONSchemaArray, JSONSchemaBoolean, JSONSchemaInteger, JSONSchemaNumber, JSONSchemaString. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into JSONSchemaInteger
        try:
            instance.actual_instance = JSONSchemaInteger.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into JSONSchemaNumber
        try:
            instance.actual_instance = JSONSchemaNumber.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into JSONSchemaString
        try:
            instance.actual_instance = JSONSchemaString.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into JSONSchemaArray
        try:
            instance.actual_instance = JSONSchemaArray.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into JSONSchemaBoolean
        try:
            instance.actual_instance = JSONSchemaBoolean.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into AttributoType with oneOf schemas: JSONSchemaArray, JSONSchemaBoolean, JSONSchemaInteger, JSONSchemaNumber, JSONSchemaString. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AttributoType with oneOf schemas: JSONSchemaArray, JSONSchemaBoolean, JSONSchemaInteger, JSONSchemaNumber, JSONSchemaString. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], JSONSchemaArray, JSONSchemaBoolean, JSONSchemaInteger, JSONSchemaNumber, JSONSchemaString]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


