# Dev containers

Dev containers help you to run your code within 10 minutes!

# Reasons:
By using Dev containers, you will ease life of your coworkers by:

### execution
They can immediately execute your PRs by cloning + `poetry run api`.

### testing
They just need to type `pytest`, all dependencies are installed automatically 
on any architecture.

### documentation
Documentation is automatically created on commits.

### integration
Creation of integration test and automatic execution on push may help
to avoid disgusting and unnexpected errors.

### deploying
1. Once you commit something, tested are executed automatically
so you can ensure all the code is sanitized
2. When is pushed to main, you can have the github actions already prepared
on templates to test, build and deploy images.
3. You may like to have other checks like linters before you deploy