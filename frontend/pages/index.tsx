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


// import React from 'react'
// import ReactDOM from 'react-dom'
// import {Provider} from 'react-redux'
// import {BrowserRouter} from 'react-router-dom'
// import App from './app'
// import configureStore from './store'

// const store = configureStore();

// const Root = () => {
//   return (
//     <Provider store={store}>
//       <BrowserRouter>
//         <App/>
//       </BrowserRouter>
//     </Provider>
//   )
// }

// const renderApplication = () => {
//   ReactDOM.render(
//     <React.StrictMode>
//       <Root />
//     </React.StrictMode>,
//     document.getElementById("root")
//   );
// };

// renderApplication()
