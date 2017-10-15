from behave import *

use_step_matcher("re")


@given("I have two integers a and b")
def step_impl(context):
    context.a = 1
    context.b = 2
    print(f"Input-1 :{context.a}")
    print(f"Input-2 :{context.b}")

