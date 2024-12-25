
# Contributing

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. Here are some ways you can contribute to the project:

- [Report a bug](#reporting-bugs)
- [Request a feature](#requesting-features)
- [Ask a question](#asking-questions)
- [Contribute to the code](#contributing-to-the-code)
- Help with documentation
- Sponsor the project
- Star and share the project


## Reporting Bugs
#### Before submitting a bug report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](/issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?


#### How to submit a good bug report?
- Open an [issue](/issues/new/choose) using the **Bug** template.
- Explain the behavior you would expect and the actual behavior.
- Provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once submitted, the team will try to reproduce the issue with your provided steps, and label the issue accordingly.

## Requesting Features
Features requests are tracked as [GitHub issues](/issues).


#### Before Submitting a feature request

- Make sure that you are using the latest version
- Read the [documentation](docs/) carefully and find out if the functionality is already covered.
- Search [issues](/issues) to see if the feature has already been requested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset.


#### How to submit a good feature request?

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- **Explain why this enhancement would be useful** to most template users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

## Asking Questions

If you want to ask a question, we assume that you have read the [documentation](docs).

Before you ask a question, it is best to search for existing [Issues](/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in that issue.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](/issues/new) using the `Question` template.
- Provide as much context as you can about what you're running into.

We will then try to answer your question as soon as possible.

## Contributing to the code

> ### Legal Notice 
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project licence.

Unless your change is trivial (typo, docs tweak etc.), please create an issue to discuss the change before creating a pull request.

If you're looking for something to get your teeth into, check out the
[`help wanted`](/issues?q=is%3Aopen+is%3Aissue+label%3Ahelp+wanted) label on github.

To make contributing as easy and fast as possible, you'll want to run tests and linting locally.

### Prerequisites

You'll need the following prerequisites:

- **Python 3.12+**
- **Poetry**
- **git**
- **make**

### How to contribute

1. Fork the repository on GitHub 
2. Clone your fork locally.
3. Install the project dependencies:

```bash
make poetry install pre-commit
```
4. Create a new branch (wit a descriptive name) for your changes:

```bash
git checkout -b my-new-feature  # use descriptive branch name
```
5. Make your code changes

6. Run tests and linting locally to make sure everything is working as expected.

```bash
make lint test
```
7. Commit your changes and push your branch to GitHub

```bash
git add .
git commit -m "My new feature"  # use descriptive commit message
git push origin my-new-feature-branch
```

8. Create a pull request, and request review from the team
> Please follow the pull request template and fill in as much information as possible. Link to any relevant issues and include a description of your changes.


### Code documentation

When contributing to this project, please make sure that all code is well documented. The following should be documented using properly formatted docstrings:

- Modules
- Class definitions
- Function definitions
- Module-level variables

The project uses [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) formatted according to [PEP 257](https://www.python.org/dev/peps/pep-0257/) guidelines. (See [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for further examples.)

### Project Documentation

Project Documentation is written in Markdown and built using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). API documentation is build from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

To preview the docuementation on your local, run:
```bash
make local
```
