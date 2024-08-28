/* eslint-disable no-unused-vars */
import { Navbar } from "./components/Navbar"
import { Login } from "./pages/Login"
import { Signup } from "./pages/Signup"
import { Routes } from 'react-router-dom';

import { Route ,Navigate} from 'react-router-dom';
import { BrowserRouter as Router } from 'react-router-dom';
function App() {

  return (
  
      <Router>
          <div className=" min-h-screen  bg-gradient-to-br from-transparent from-50% via-[#88baf0]/25 bg-opacity-15 to-[#fde18d]/25">
          <Navbar/>
        <Routes>
          <Route path="/Login" element={<Login/>}/>
          <Route path="/Signup" element={<Signup/>}/>
         
        </Routes> 
         </div>
      </Router>
     

  
   )          
}

export default App
