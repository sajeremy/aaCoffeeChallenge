import React from 'react'
import CoffeeListItem from './CoffeeListItem'
import axios from 'axios'

export default function Coffee({test}) {
    console.log('data :>>', test)

    return (
        <div>
            <div>
                <p>Coffees</p>
                <button>New Coffee</button>
            </div>
            <CoffeeListItem></CoffeeListItem>
        </div>
    )
}


export async function getServerSideProps() {

    const res = await fetch("http://localhost:8000/api/coffee")
    const data = await res.json()

    return {
        props: {
            test:data,
        }
    }

}