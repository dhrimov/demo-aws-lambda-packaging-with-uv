# Overview

Demo repository for packaging AWS Lambda functions with uv when a project has more than one lambda. Each lambda lives in its own directory under `lambdas/`, with its own dependencies and its own build output (a zip archive).

The entire packaging process is described in [Packaging Python Lambdas with uv and package-python-function](https://dhrimov.dev/blog/python-lambda-packaging-uv-package-python-function).

## Repository layout

- `lambdas/acme-order-notifier` and `lambdas/acme-order-processor` - the two lambdas, each with its own `pyproject.toml` and `uv.lock`.
- `build.sh` - packages a single lambda into a zip, using `uv` and `package-python-function`.
- `terraform/` - build output directory. A placeholder folder for the future infrastructure definitions.

## Building a lambda

`build.sh` packages one lambda at a time. Point `--input` at the lambda's directory:

```bash
./build.sh --input lambdas/acme-order-notifier --output terraform --python 3.13 --platform aarch64-manylinux2014
./build.sh --input lambdas/acme-order-processor --output terraform --python 3.13 --platform aarch64-manylinux2014
```

Run `./build.sh --help` for the full list of options. Each command writes a zip named after the lambda into `terraform/`.

The only thing that changes between the two commands is `--input`, so it's easy to loop over all lambdas instead of calling `build.sh` by hand for each one:

```bash
for lambda in lambdas/*/; do
  ./build.sh --input "$lambda" --output terraform --python 3.13 --platform aarch64-manylinux2014
done
```