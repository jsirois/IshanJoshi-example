# Working Example

To run, execute `pants run example.py`.

Notes:
+ The lock file was generated by running `pants generate-lockfiles`.
+ The mongomock library needs setuptools at runtime but does not declare this dependency:
  
  Needs: https://github.com/mongomock/mongomock/blob/4.1.2/mongomock/__version__.py
  
  Does not declare (no `install_requires` for setuptools):
    + https://github.com/mongomock/mongomock/blob/4.1.2/setup.py
    + https://github.com/mongomock/mongomock/blob/4.1.2/setup.cfg

