# github-contribution-appreciation
A GitHub extension for showing appreciation to someone who you find helpful

Problem Statement


One of the ways that the Kubernetes community shows appreciation for the "chopping wood and carrying water" work that contributors do is to send them chocolate or some other kind of physical gift (see their talk at OSLS here: http://sched.co/DjtU). Not all open source projects are resourced to give this kind of gift. What if there was a way for an open source maintainer to give a badge to a contributor whom they appreciate such that this badge shows up on the contributor's github profile? It would be a way for maintainers who don't have the resources to show appreciation and this appreciation will in turn mean something to the contributor.

Design

Distributed design based on github.
Sender (optionally via UI) makes commit (automatic) into a particular badge repo (eg: https://github.com/{johnDoeRepo}/kudos-badge) with structured yaml, eg:
Name: John Doe
GithubID: johnDoe
Message: Thanks for the awesome open source contributions to Project Kudos Badge

Sender notifies receiver (automatic) with a snippet to embed in a web page they own. Snippet includes at least two pieces of data:
Repo url
Commit ID (optionally empty)

Receiver embeds badge snippet in their web page

Sender to Receiver notification:
Could be email (via git commit hook on sender side).
Could be pull request, if the sender knows the target repo.
Easy if target is a project not a user (eg: https://github.com/ciao-project/ciao/pull/218).


>> Our goal is for users and people, not project which already have *stars* on github.


Could assume for ${userid} that the target will be https://${userid}.github.io, which is backed by the repo https://github.com/${userid}/${userid}.github.io/ 
Receiver’s web page (eg: https://johndoe.github.io) on render runs the javascript, which reaches out across the web to the repo url, reads the specific commit, parses its yaml content and displays the results.  If the commit ID is empty, the HEAD commit at the repo is parsed and displayed

________________________

Notes:

This provides minimal security in that the sender of the kudos must have commit permission on the badge giving repository
Yaml format on the commit side could be extended to have badge types or icon url and other things.  
Simply skipped if client side javascript doesn’t yet know those fields.
Initially might be manual on the sender/commit side
Initially might be manual on the receiver side to embed in page


Badge Types:

Kudos - person to person
Metrics - based on statistics of the project (top commiter, top reviewer, etc)
Organization appreciation - organization to person



Icons can be emoji, e.g: 

Trophy https://assets-cdn.github.com/images/icons/emoji/unicode/1f3c6.png 

Heart  https://assets-cdn.github.com/images/icons/emoji/unicode/2764.png 

Thumbs up  https://assets-cdn.github.com/images/icons/emoji/unicode/1f44d.png 

Tada  https://assets-cdn.github.com/images/icons/emoji/unicode/1f389.png 