## Voting
**Voting/likes system requirements**
1. User should be able to like a post
2. should only be able to like a post once
3. Retrieving posts should also fetch the total number of like per post

We can use a composite primary key to make sure there is no duplicates of a user liking a post twice.

**vote routing**
We are going to use a vote direction to differentiate between adding and removing a like. A vote direction of 1 means we want to add a vote, a direction of 0 means we want to delete a vote.
