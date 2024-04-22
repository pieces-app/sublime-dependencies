# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema


class ConversationGrounding(BaseModel):
    """
    This is the context used for grounding the ml models with reguard to a conversation.  # noqa: E501
    """

    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    messages: Optional[FlattenedConversationMessages] = None
    __properties = ["schema", "messages"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConversationGrounding:
        """Create an instance of ConversationGrounding from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict["schema"] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict["messages"] = self.messages.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConversationGrounding:
        """Create an instance of ConversationGrounding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConversationGrounding.parse_obj(obj)

        _obj = ConversationGrounding.parse_obj(
            {
                "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema"))
                if obj.get("schema") is not None
                else None,
                "messages": FlattenedConversationMessages.from_dict(obj.get("messages"))
                if obj.get("messages") is not None
                else None,
            }
        )
        return _obj


from pieces_os_client.models.flattened_conversation_messages import (
    FlattenedConversationMessages,
)

# ConversationGrounding.update_forward_refs()
