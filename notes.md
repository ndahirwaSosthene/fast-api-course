## Voting
**Voting/likes system requirements**
1. User should be able to like a post
2. should only be able to like a post once
3. Retrieving posts should also fetch the total number of like per post

We can use a composite primary key to make sure there is no duplicates of a user liking a post twice.

**vote routing**
We are going to use a vote direction to differentiate between adding and removing a like. A vote direction of 1 means we want to add a vote, a direction of 0 means we want to delete a vote.


Database Migrations

1. Developers can track changes to code and rollback code easily
with GIT. Why can't we do the same for database models/tables

2. Database migrations allow us to incrementally track changes to
database schema and rollback changes to any point in time

3. We will use a tool called Alembic to make changes to our
database
4. Alembic can also automatically pull database models from
Sqlalchemy and generate the proper tables