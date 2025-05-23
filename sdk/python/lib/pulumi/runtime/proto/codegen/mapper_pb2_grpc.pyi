"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2016-2023, Pulumi Corporation.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import abc
import grpc
import pulumi.codegen.mapper_pb2

class MapperStub:
    """Mapper is a service for getting mappings from other ecosystems to Pulumi.
    This is currently unstable and experimental.

    Mapper provides methods for retrieving mappings that describe how to map names in some source "provider" (e.g. a
    Terraform provider, if we are converting from Terraform) to names in appropriate Pulumi packages. So when converting
    a Terraform program containing code like `resource "aws_s3_bucket" "b" {}`, for instance, we need to know (among
    other things) that the `aws_s3_bucket` Terraform resource type corresponds to the Pulumi type `aws:s3/bucket:Bucket`,
    and thus lives in the `aws` package. This is the kind of information that a Mapper provides.
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    GetMapping: grpc.UnaryUnaryMultiCallable[
        pulumi.codegen.mapper_pb2.GetMappingRequest,
        pulumi.codegen.mapper_pb2.GetMappingResponse,
    ]
    """`GetMapping` returns any available mapping data for the given source provider name (so again, this is e.g. the
    name of a Terraform provider if converting from Terraform). Callers may pass "hints" that describe a Pulumi
    package that is expected to provide the mapping and satisfy the request, which implementations may use to
    optimise their efforts to return the best possible mapping. If no matching mapping exists, implementations should
    return an empty byte array result.
    """

class MapperServicer(metaclass=abc.ABCMeta):
    """Mapper is a service for getting mappings from other ecosystems to Pulumi.
    This is currently unstable and experimental.

    Mapper provides methods for retrieving mappings that describe how to map names in some source "provider" (e.g. a
    Terraform provider, if we are converting from Terraform) to names in appropriate Pulumi packages. So when converting
    a Terraform program containing code like `resource "aws_s3_bucket" "b" {}`, for instance, we need to know (among
    other things) that the `aws_s3_bucket` Terraform resource type corresponds to the Pulumi type `aws:s3/bucket:Bucket`,
    and thus lives in the `aws` package. This is the kind of information that a Mapper provides.
    """

    @abc.abstractmethod
    def GetMapping(
        self,
        request: pulumi.codegen.mapper_pb2.GetMappingRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.codegen.mapper_pb2.GetMappingResponse:
        """`GetMapping` returns any available mapping data for the given source provider name (so again, this is e.g. the
        name of a Terraform provider if converting from Terraform). Callers may pass "hints" that describe a Pulumi
        package that is expected to provide the mapping and satisfy the request, which implementations may use to
        optimise their efforts to return the best possible mapping. If no matching mapping exists, implementations should
        return an empty byte array result.
        """

def add_MapperServicer_to_server(servicer: MapperServicer, server: grpc.Server) -> None: ...
