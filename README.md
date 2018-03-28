# GitHub-contribution-appreciation
A GitHub extension for showing appreciation to someone who you find helpful

## Problem Statement

One of the ways that the Kubernetes community shows appreciation
for the "chopping wood and carrying water" work that contributors
do is to send them chocolate, a shirt, or some other kind of physical
gift as described in [this talk at 2018 OSLS](http://sched.co/DjtU). Not all
open source projects are resourced to give this kind of gift. What
if there was a way for an open source maintainer to give a badge
to a contributor whom they appreciate such that this badge shows
up on the contributor's GitHub profile? It would be a way for
maintainers who don't have the resources to show appreciation and
this appreciation will in turn mean something to the contributor.

## Design and Implementation

We've made a roof of concept design based on GitHub, because almost
everybody uses GitHub nowadays.  This would be easier and cleaner
if it were a feature centralized within GitHub itself.  But our
implementation currently does not actually depend at all on GitHub, but
rather just git repositories themselves.

We have a few design goals:
* easy for a sender to give kudos
* easy for a receiver to get and display kudos
* displayed kudos should be trustworthy
* usable by individuals and projects to give kudos to peers and
  contributors

In order to have a trustworthy, durable kudo linked back to the
sending individual, we've chosen to store the kudo as a public git
commit in a repository either owned by the sending individual or a
shared project repository to which the sender has commit access.

For sending, we've made a simple CLI for the sender which asks a
few questions and based on the answer:
* generates and pushes a git commit containing the kudo to a public repo
* sends an email notification with kudo information to the recipient

For display, the receiver copies a snippet of javascript from their kudo
email into a web page they control (eg: their userid.github.io).  Embedded
in this script is a reference to the giver's git repository and git commit.
When the javascript runs during a page view, the kudo is loaded from the
sender's git repository and displayed.

## Future Work

The initial implementation is simple and crud.  We imagine it can easily be
extended, for example:
* non-cli kudo giving user interface
* fancier display javascript (more "badge" like)
* notificiations through GitHub
* sending a PR to a userid.github.io page instead of requiring the user to
  copy the javascript manually
* more badge types beyond simple thank you messages (eg: metrics/statistics
  like top commiter, top reviewers, etc.)

## Contributing

This is an open source project.  See the [CONTRIBUTING.md](CONTRIBUTING.md)
document for more information.
