import React from 'react'
import PostListItem from './PostListItem'

const Post = () => {
    return (
        <div>
            <div>
                <h2>Posts</h2>
                <button>New Post</button>
                <select>
                    <option value="asc">asc</option>
                    <option value="dsc">dsc</option>
                </select>
            </div>
            <PostListItem></PostListItem>
        </div>
    )
}

export default Post