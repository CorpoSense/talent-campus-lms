/* eslint-disable no-unused-vars */
import { Navbar } from "./components/Navbar"
import { Login } from "./pages/Login"
import { Signup } from "./pages/Signup"
import { Routes } from 'react-router-dom';
import { Hero } from "./components/Hero";
import { Route ,Navigate} from 'react-router-dom';
import { Home } from "./pages/Home";
import { BrowserRouter as Router } from 'react-router-dom';
function App() {

  return (
    // bg-gradient-to-br from-transparent from-40% via-[#88baf0]/60 bg-opacity-15 to-[#fde18d]/60
      <Router>
          <div className=" min-h-screen bg-[#f8f9fa] ">
          <Navbar/>
        <Routes>
          <Route path="/Login" element={<Login/>}/>
          <Route path="/Signup" element={<Signup/>}/>
          <Route path="/" element={<Home/>}/>

        </Routes> 
         </div>
      </Router>
   )          
}

export default App
