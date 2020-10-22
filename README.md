# Training Provider Catalogue API

This is a reference implementation of a proposed API
enabling Aged Care providers to interact with training providers
in a standardised way.

Specifically, it provides the endpoints allowing Aged Care Providers
(employers) to search and browse the current course catalogue
offered by a Training Provider.

Detailed technical documentation is in the docs/ folder.

DEPLOYMENT.md and DEVELOPMENT.md contain information about running
the software and making changes to it.

There is a test endpoint
with a self-documenting API specification here:

* https://j7ndza0k1j.execute-api.us-east-1.amazonaws.com/dev/catalogue/docs

This is equivalent to what you will have running locally
if you create a local development environment
(per DEPLOYMENT.md)

The test endpoint is continuously deployed
from the `main` branch in this repository,
so should be considered unstable.
It is also completely open
(do not require authentication),
which is not a realistic simulation
of any kind of production environment.
