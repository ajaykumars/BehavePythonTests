from behave import *

use_step_matcher("re")

@when("I add the numbers")
def step_impl(context):
    context.sum = int(context.a) + int(context.b)


@then("I print the addition result")
def step_impl(context):
    print("Sum of", context.a, "and", context.b, "is:",context.sum)
    print("======================================================")