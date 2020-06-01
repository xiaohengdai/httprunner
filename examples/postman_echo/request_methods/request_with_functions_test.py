# NOTICE: Generated By HttpRunner. DO NOT EDIT!
# FROM: examples/postman_echo/request_methods/request_with_functions.yml

from httprunner import HttpRunner, Config, Step, Request


class TestCaseRequestWithFunctions(HttpRunner):
    config = (
        Config("request methods testcase with functions")
        .variables(foo1="session_bar1")
        .base_url("https://postman-echo.com")
        .verify(False)
    )

    teststeps = [
        Step("get with params")
        .with_variables(foo1="bar1", foo2="session_bar2", sum_v="${sum_two(1, 2)}")
        .set_extractor("session_foo2", "body.args.foo2")
        .run_request(
            Request()
            .get("/get")
            .with_params(foo1="$foo1", foo2="$foo2", sum_v="$sum_v")
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
        )
        .assert_equal("status_code", 200)
        .assert_equal("body.args.foo1", "session_bar1")
        .assert_equal("body.args.sum_v", "3")
        .assert_equal("body.args.foo2", "session_bar2"),
        Step("post raw text")
        .with_variables(foo1="hello world", foo3="$session_foo2")
        .run_request(
            Request()
            .post("/post")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "Content-Type": "text/plain",
                }
            )
            .with_data(
                "This is expected to be sent back as part of response body: $foo1-$foo3."
            )
        )
        .assert_equal("status_code", 200)
        .assert_equal(
            "body.data",
            "This is expected to be sent back as part of response body: session_bar1-session_bar2.",
        ),
        Step("post form data")
        .with_variables(**{"foo1": "bar1", "foo2": "bar2"})
        .run_request(
            Request()
            .post("/post")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            .with_data("foo1=$foo1&foo2=$foo2")
        )
        .assert_equal("status_code", 200)
        .assert_equal("body.form.foo1", "session_bar1")
        .assert_equal("body.form.foo2", "bar2"),
    ]


if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()
