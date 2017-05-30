from behave import *

count = 0


@step("I have a step that fails sometimes")
def fail_twice_then_pass(context):
    global count

    count += 1
    print(count)

    assert count > 4
