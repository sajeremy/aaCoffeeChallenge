import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import homeStyles from '@components/styles/Home.module.css'
import testStyles from '@components/styles/Test.module.css'
import Post from  '../components/Post'
import Coffee from '../components/Coffee'
const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
    <div className={homeStyles.mainPage}>
      <div className={homeStyles.leftCol}></div>
      <div className={homeStyles.centerCol}>
        <Post></Post>
      </div>
      <div className={homeStyles.leftCol}>
        <Coffee></Coffee>
      </div>
    </div>
    </>
    )
}