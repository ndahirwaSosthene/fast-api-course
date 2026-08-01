import time
from fastapi import FastAPI, status, HTTPException, Response
import psycopg2
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor

# step 1: Initialize fastAPI instance
app = FastAPI()

# Post pydantic model
class Post(BaseModel):
    title:  str
    content: str
    published: bool = True
    # rating: Optional[int] = None -> This is an example of how to use an optional parameters without a default

#example of how a post would look like
# my_posts = [
#     {
#         "title" : "title of post 1",
#         "content": "content of post 1",
#         "id": 1
#     },
#     {
#         "title" : "favourite foods",
#         "content": "I like pizza",
#         "id": 2
#     }
# ]


# step 2: setup database and Connect to a PostgreSQL database, and if it fails, keep retrying every 2 seconds until it succeeds.
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='ndah21@g1', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to the database failed")
        print("Error: ", error)
        time.sleep(2)

# step 3: Define all path operations
# path_op 1: Main introductory path
@app.get("/")
def root():
    return {"message" : "Welcome to my API!"}


#path_op 2: See all posts in the database
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM POSTS""")
    posts = cursor.fetchall()
    print(posts)
    return {"data":posts}

#pathop 3: create a post
@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: Post):
    # this way prevents sql injection
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))

    #this is to fetch the final row that was added in the database just like in postgress so that we can print it.
    new_post = cursor.fetchone()
    #Then we finalise by committing the change. If we don't commit the data is not added to the database because the changes are only staged at this point.
    conn.commit()
    return {"data": new_post}

#path_op 4: See a particular post by its ID
@app.get("/posts/{id}")
def get_post(id: int): # response: Response
    cursor.execute("""SELECT * from posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {id} was not found")
    return {"post_detail": post}

#path_op 5: Delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute("""DELETE FROM posts WHERE id = %s returning * """, (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = f"post with ID {id} doesnot exist")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#path_op 6: Update a particular post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, 
                   (post.title, post.content, post.published, (str(id))))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail = f"post with ID {id} doesnot exist")

    return {'data': updated_post}





