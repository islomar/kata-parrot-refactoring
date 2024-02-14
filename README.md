![Run linters and tests workflow](https://github.com/islomar/kata-parrot-refactoring/actions/workflows/run-linters-and-tests.yml/badge.svg)

# Python kata "Parrot refactoring"

- [Parrot refactoring kata](https://github.com/emilybache/Parrot-Refactoring-Kata)
  - Video from Emily Bache about this kata: ["Parrot: Top Code Kata | Conditional to Polymorphism Refactoring Practice"](https://www.youtube.com/watch?v=UxNEHKg_2eA)
- Everything is **Dockerized**. If you run `make` from the root folder of the project, you can see all the actions that you can execute (e.g. running the tests, static analysis, code coverage, etc.)


## HOW to use it
1. Generate a repo using this one as a template, following [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template)
2. Replace the `python-kata-name` placeholder that appears in several files with your own name (e.g. `python-fizzbuzz`). 
   - For example, you can easily do it running `make rename-project new-name=python-fizzbuzz`


## Prerequisites
- You need `Docker` installed.
- **IMPORTANT**: just the first time, run `make local-setup`.
    - This will set up things like configuring Git hooks. The `pre-commit` hook will automatically run the linters and tests, rejecting the commit in case any of them fail.


## Steps and decisions taken in the kata
1. I started running the test coverage: it only showed that `raise ValueError()` was never hit.
   - Because of the use of `mypy` and typing, now it is not possible to pass a non-existing parrot type to the constructor of Parrot, so we could just delete `ValueError("should be unreachable")` without getting a broken pipeline (also the commit would be rejected), the reason being that we are running `make check-typing` in both processes.
2. Running the mutation testing (`make test-run-mutation`) showed 7 mutants surviving: that means that the initial tests are missing several use cases.
3. I have done micro-commits where the baby steps can be easily followed.
   - Parallel changes as a general rule of thumb (expand and contract)
   - Delete anything not needed in the specific classes that arise
   - Finish leaving the Parrot class as an abstract class
4. I could have created a factory method in `Parrot` or in every specific class for creating the different parrots. I find that solution "too complex" for the current needs :-)

## Other options
- https://anthonysciamanna.com/2021/08/27/refactoring-the-parrot-kata.html
- [Software Design Mastery | Nail the Parrot Refactoring Kata in C#](https://www.youtube.com/watch?v=IvFX8Ivit1k)
- https://github.com/trikitrok/parrot-refactoring-kata-java