// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Returns the absolute value of a given float.
 * Example: abs(1) returns 1, and abs(-1) would also return 1, whereas abs(-3.14) would return 3.14.
 */
export function abs(args: AbsArgs, opts?: pulumi.InvokeOptions): Promise<AbsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("std:index:Abs", {
        "a": args.a,
        "b": args.b,
    }, opts);
}

export interface AbsArgs {
    a: number;
    b: number;
}

export interface AbsResult {
    readonly result: number;
}
/**
 * Returns the absolute value of a given float.
 * Example: abs(1) returns 1, and abs(-1) would also return 1, whereas abs(-3.14) would return 3.14.
 */
export function absOutput(args: AbsOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<AbsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("std:index:Abs", {
        "a": args.a,
        "b": args.b,
    }, opts);
}

export interface AbsOutputArgs {
    a: pulumi.Input<number>;
    b: pulumi.Input<number>;
}
