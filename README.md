# Overview

Demo repository for packaging AWS Lambda functions with uv when a project has more than one lambda. Each lambda lives in its own directory under `lambdas/`, with its own dependencies and its own build output (a zip archive).

The entire packaging process is described in [Packaging Python Lambdas with uv and package-python-function](https://dhrimov.dev/blog/python-lambda-packaging-uv-package-python-function).

The script from that post is now a GitHub Action, [Package Python Lambda](https://github.com/marketplace/actions/package-python-lambda), and this repo uses it instead of keeping its own copy. That's covered in the next post: [A GitHub Action to Package Python AWS Lambdas with uv](https://dhrimov.dev/blog/github-action-package-python-aws-lambda-uv).

## Repository layout

- `lambdas/acme-order-notifier` and `lambdas/acme-order-processor` - the two lambdas, each with its own `pyproject.toml` and `uv.lock`.
- `.github/workflows/package.yml` - CI: packages each lambda with [dhrimov/package-python-lambda-gha](https://github.com/dhrimov/package-python-lambda-gha).
- `terraform/` - local build output directory. A placeholder folder for the future infrastructure definitions.

## Packaging in CI

[.github/workflows/package.yml](./.github/workflows/package.yml) packages the lambdas on every pull request and every push to `main`. A matrix runs one job per lambda, in parallel, and each job uploads its zip as a workflow artifact, so you can download it from the run page. To get the zips without pushing anything, run the workflow by hand from the Actions tab.

To add a lambda, add its directory name to the `lambda` list in the matrix.

The workflow only packages. It does not deploy.

## Packaging locally

Clone the action and run its `build.sh`, one lambda at a time. It needs `uv` and `jq` on PATH:

```bash
git clone https://github.com/dhrimov/package-python-lambda-gha ../package-python-lambda-gha

for lambda in lambdas/*/; do
  ../package-python-lambda-gha/build.sh --input "$lambda" --output terraform --python 3.13 --platform aarch64-manylinux2014
done
```

Each call writes a zip named after the lambda into `terraform/`. The build runs in `<lambda>/build`, and that directory is deleted before and after every build.
