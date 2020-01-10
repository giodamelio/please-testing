python_library(
name = "my_library",
srcs = ["lib.py"],
deps = ["//third_party:requests"],
)

python_binary(
name = "my_binary",
main = "bin.py",
deps = [":my_library"],
)

python_test(
name = "my_library_test",
srcs = ["lib_test.py"],
deps = [":my_library"],
)
